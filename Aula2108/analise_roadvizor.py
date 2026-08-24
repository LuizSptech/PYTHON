"""
analise_roadvizor.py

Segundo script do projeto RoadVizor.
Responsável por:
    1. Ler os dados já coletados e salvos em arquivo(s) CSV pelo script de coleta.
    2. Realizar transformações e agregações sobre esses dados
       (uso médio de RAM, pico de CPU, média de uso de disco, etc.).

Uso:
    python analise_roadvizor.py
    python analise_roadvizor.py --padrao "roadvizor*.csv" --janela-ram 60 --janela-disco 30

Os arquivos CSV são lidos com separador ';' (mesmo padrão do script de coleta).
"""

import argparse
import glob
import sys
from pathlib import Path

import pandas as pd

COLUNAS_ESPERADAS = [
    "usuario", "timestamp", "cpu_uso_geral", "qtd_cpu_fisica", "qtd_cpu_logica",
    "ram_total", "ram_uso", "swap_total", "swap_uso",
    "proc_rodando", "proc_esperando",
    "disco_total", "disco_uso",
    "rede_enviada", "rede_recebida",
    "pacote_perdido_entrada", "pacote_perdido_saida",
]


def _corrigir_cabecalho_quebrado(df: pd.DataFrame) -> pd.DataFrame:
    """
    Alguns arquivos foram salvos sem o ';' entre as colunas 'usuario' e
    'timestamp' no cabeçalho (ex.: 'usuariotimestamp;cpu_uso_geral;...').
    Como as LINHAS de dados têm o separador correto, o pandas acaba
    interpretando a coluna 'usuario' como índice do DataFrame.
    Esta função detecta e corrige esse caso.
    """
    if "usuario" not in df.columns and "usuariotimestamp" in df.columns:
        df = df.reset_index()
        df = df.rename(columns={"index": "usuario", "usuariotimestamp": "timestamp"})
    return df


def carregar_dados(padrao: str = "roadvizor*.csv", pasta: str = ".") -> pd.DataFrame:
    """Lê todos os CSVs que casam com o padrão informado e retorna um único DataFrame."""
    arquivos = sorted(glob.glob(str(Path(pasta) / padrao)))
    if not arquivos:
        raise FileNotFoundError(
            f"Nenhum arquivo encontrado com o padrão '{padrao}' em '{pasta}'."
        )

    dataframes = []
    for arquivo in arquivos:
        df = pd.read_csv(arquivo, sep=";")
        df = _corrigir_cabecalho_quebrado(df)
        df.columns = [c.strip() for c in df.columns]
        dataframes.append(df)
        print(f"[OK] {arquivo}: {len(df)} registros lidos")

    dados = pd.concat(dataframes, ignore_index=True)

    # tipagem / limpeza
    dados["timestamp"] = pd.to_datetime(
        dados["timestamp"], format="%d/%m/%Y %H:%M:%S", errors="coerce"
    )
    dados = dados.dropna(subset=["timestamp"])

    colunas_numericas = [c for c in dados.columns if c not in ("usuario", "timestamp")]
    for col in colunas_numericas:
        dados[col] = pd.to_numeric(dados[col], errors="coerce")

    # métricas percentuais derivadas (mais úteis que os valores absolutos em bytes)
    dados["ram_uso_pct"] = dados["ram_uso"] / dados["ram_total"] * 100
    dados["disco_uso_pct"] = dados["disco_uso"] / dados["disco_total"] * 100

    dados = dados.sort_values(["usuario", "timestamp"]).reset_index(drop=True)
    return dados


def filtrar_ultimos_minutos(df: pd.DataFrame, minutos: int, coluna_tempo: str = "timestamp") -> pd.DataFrame:
    """
    Retorna apenas os registros dentro da janela dos últimos N minutos,
    relativos ao timestamp mais recente presente nos dados de cada usuário.
    """
    if df.empty:
        return df
    limite = df[coluna_tempo].max() - pd.Timedelta(minutes=minutos)
    return df[df[coluna_tempo] >= limite]


def _filtrar_ultimos_minutos_por_usuario(df: pd.DataFrame, minutos: int) -> pd.DataFrame:
    """Aplica filtrar_ultimos_minutos independentemente para cada usuário."""
    partes = [filtrar_ultimos_minutos(grupo, minutos) for _, grupo in df.groupby("usuario")]
    if not partes:
        return df.iloc[0:0]
    return pd.concat(partes, ignore_index=True)


def pico_cpu(df: pd.DataFrame, inicio: str = None, fim: str = None) -> pd.Series:
    """
    Pico de uso de CPU (%) em um período, por usuário.
    Se 'inicio'/'fim' não forem informados, considera todo o período disponível.
    Formato esperado para inicio/fim: 'dd/mm/aaaa HH:MM:SS'.
    """
    dados = df
    if inicio:
        dados = dados[dados["timestamp"] >= pd.to_datetime(inicio, format="%d/%m/%Y %H:%M:%S")]
    if fim:
        dados = dados[dados["timestamp"] <= pd.to_datetime(fim, format="%d/%m/%Y %H:%M:%S")]
    return dados.groupby("usuario")["cpu_uso_geral"].max().round(2)


def media_disco_ultimos_minutos(df: pd.DataFrame, minutos: int = 30) -> pd.Series:
    """Média de uso de disco (%) nos últimos N minutos, por usuário."""
    janela = _filtrar_ultimos_minutos_por_usuario(df, minutos)
    return janela.groupby("usuario")["disco_uso_pct"].mean().round(2)


def media_ram_ultimos_minutos(df: pd.DataFrame, minutos: int) -> pd.Series:
    """Uso médio de RAM (%) nos últimos N minutos, por usuário (genérico)."""
    janela = _filtrar_ultimos_minutos_por_usuario(df, minutos)
    return janela.groupby("usuario")["ram_uso_pct"].mean().round(2)


def gerar_relatorio(df: pd.DataFrame, janela_ram: int, janela_disco: int) -> pd.DataFrame:
    """Monta uma tabela-resumo com todas as métricas calculadas, por usuário."""
    resumo = pd.DataFrame({
        f"ram_media_pct_ult_{janela_ram}min": media_ram_ultimos_minutos(df, janela_ram),
        "cpu_pico_pct": pico_cpu(df),
        f"disco_media_pct_ult_{janela_disco}min": media_disco_ultimos_minutos(df, janela_disco),
    })
    resumo["qtd_amostras"] = df.groupby("usuario").size()
    resumo["periodo_inicio"] = df.groupby("usuario")["timestamp"].min()
    resumo["periodo_fim"] = df.groupby("usuario")["timestamp"].max()
    return resumo.reset_index()


def main():
    parser = argparse.ArgumentParser(description="Análise e agregação dos dados do RoadVizor")
    parser.add_argument("--padrao", default="roadvizor*.csv",
                         help="Padrão (glob) dos arquivos CSV a serem lidos")
    parser.add_argument("--pasta", default=".", help="Pasta onde estão os arquivos CSV")
    parser.add_argument("--janela-ram", type=int, default=60,
                         help="Janela em minutos para a média de RAM (padrão: 60 = última hora)")
    parser.add_argument("--janela-disco", type=int, default=30,
                         help="Janela em minutos para a média de disco (padrão: 30)")
    parser.add_argument("--saida", default="relatorio_roadvizor.csv",
                         help="Nome do arquivo CSV de saída com o relatório")
    args = parser.parse_args()

    try:
        dados = carregar_dados(padrao=args.padrao, pasta=args.pasta)
    except FileNotFoundError as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"\nTotal de registros carregados: {len(dados)}")
    print(f"Usuários encontrados: {sorted(dados['usuario'].unique())}\n")

    relatorio = gerar_relatorio(dados, args.janela_ram, args.janela_disco)

    print("=== Relatório de métricas por usuário ===")
    print(relatorio.to_string(index=False))

    relatorio.to_csv(args.saida, sep=";", index=False)
    print(f"\nRelatório salvo em: {args.saida}")


if __name__ == "__main__":
    main()

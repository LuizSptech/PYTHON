"""Camada 03 - relatorios de governanca a partir do CSV silver."""
import os
 
import numpy as np
import pandas as pd
 
ENTRADA = "02-silver/silver_consolidado.csv"
SAIDA = "03-gold"
LIMITE_CONN = 40
os.makedirs(SAIDA, exist_ok=True)
 
 
def zonas_mortas(df):
    r = df.groupby("id_antena").agg(mbps_medio=("mbps", "mean"),
                                    conn_media=("active_conn", "mean")).round(2)
    return r.sort_values("mbps_medio").reset_index()
 
 
def predicao_sobrecarga(df):
    """Regressao linear de active_conn no tempo -> quando atinge o limite."""
    corte = df["timestamp"].max() - pd.Timedelta(hours=5)
    linhas = []
    for ap, g in df[df["timestamp"] >= corte].groupby("id_antena"):
        if len(g) < 3:
            continue
        x = (g["timestamp"] - g["timestamp"].min()).dt.total_seconds().values
        a, b = np.polyfit(x, g["active_conn"].values, 1)
        previsao = None
        if a > 0:
            seg = (LIMITE_CONN - b) / a
            previsao = g["timestamp"].min() + pd.Timedelta(seconds=max(seg, 0))
        linhas.append({"id_antena": ap, "crescimento_conn_por_hora": round(a * 3600, 2),
                       "previsao_atingir_limite": previsao})
    return pd.DataFrame(linhas)
 
 
def eficiencia_hardware(df):
    r = df.groupby("id_antena").agg(mbps=("mbps", "mean"), cpu=("cpu_usage", "mean"))
    r["mbps_por_cpu"] = (r["mbps"] / r["cpu"]).round(4)
    return r.sort_values("mbps_por_cpu").reset_index()  # menor = menos eficiente
 
 
def expurgo(df):
    fw = df.drop_duplicates("timestamp").copy()
    fw["hora"] = fw["timestamp"].dt.floor("h")
    r = fw.groupby("hora").agg(pacotes_bloqueados=("fw_dropped_packets", "sum"),
                               cpu_fw_media=("fw_cpu_usage", "mean")).reset_index()
    r["possivel_ddos"] = r["pacotes_bloqueados"] > r["pacotes_bloqueados"].mean() * 2
    return r
 
 
def mapa_calor(df):
    r = df.groupby("id_antena")["mbps"].sum().rename("mbps_total").reset_index()
    r["percentual"] = (r["mbps_total"] / r["mbps_total"].sum() * 100).round(1)
    return r.sort_values("percentual", ascending=False)
 
 
def main():
    df = pd.read_csv(ENTRADA, parse_dates=["timestamp"])
    relatorios = {
        "zonas_mortas": zonas_mortas,
        "predicao_sobrecarga": predicao_sobrecarga,
        "eficiencia_hardware": eficiencia_hardware,
        "expurgo_seguranca": expurgo,
        "mapa_calor": mapa_calor,
    }
    for nome, fn in relatorios.items():
        fn(df).to_csv(f"{SAIDA}/{nome}.csv", index=False)
        print("gerado:", nome)
 
 
if __name__ == "__main__":
    main()

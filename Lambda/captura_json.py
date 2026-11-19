import json
import requests

def lambda_handler(event, context):
    url = "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/EstatisticasTransacoesPix(Database=@Database)?@Database='202310'&$top=500&$format=json&$select=AnoMes,PAG_PFPJ,REC_PFPJ,PAG_REGIAO,REC_REGIAO,PAG_IDADE,REC_IDADE,FORMAINICIACAO,NATUREZA,FINALIDADE,VALOR,QUANTIDADE"
    try:
        resultado = requests.get(url)
        # Verifica se a requisição foi bem-sucedida
        resultado.raise_for_status()
        # Decodifica o JSON
        dados = resultado.json()
        # Extrai a lista de transações Pix
        transacoes = dados['value']
        return transacoes

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        print(f"Resposta completa da API: {resultado.text}")
        return None

print(lambda_handler(None, None))
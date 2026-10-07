"""Camada 02 - le os JSON brutos, trata, cruza antenas x firewall e gera CSV. """
 

import glob
import json
import os
 
import pandas as pd
 
ENTRADA = "01-bronze"
SAIDA = "02-silver"
os.makedirs(SAIDA, exist_ok=True)
 
 
def carregar():
    registros = []
    for caminho in glob.glob(f"{ENTRADA}/*.json"):
        with open(caminho, encoding="utf-8") as f:
            registros.append(json.load(f))
    return pd.DataFrame(registros)
 
 
def status_carga(linha):
    if linha["active_conn"] > 40:
        return "alta densidade"
    if linha["cpu_usage"] > 80:
        return "gargalo de processamento"
    if linha["ram_usage"] > 75:
        return "OOM"
    return "normal"
 
 
def vazao_mbps(df, col_id, col_bytes):
    """Diferenca entre minuto atual e anterior -> Mbps."""
    df = df.sort_values([col_id, "timestamp"]).copy()
    delta_bytes = df.groupby(col_id)[col_bytes].diff()
    delta_seg = df.groupby(col_id)["timestamp"].diff().dt.total_seconds()
    df["mbps"] = (delta_bytes.clip(lower=0) * 8 / 1_000_000 / delta_seg).round(3)
    return df
 
 
def main():
    df = carregar()
    if df.empty:
        print("sem dados em", ENTRADA)
        return
    df["timestamp"] = pd.to_datetime(df["timestamp"])
 
    antenas = df[df["id_antena"].notna()].copy()
    firewall = df[df["id_firewall"].notna()].copy()
 
    antenas = vazao_mbps(antenas, "id_antena", "bytes_sent")
    antenas["status_carga"] = antenas.apply(status_carga, axis=1)
    firewall = vazao_mbps(firewall, "id_firewall", "bytes_sent")

 
    antenas["minuto"] = antenas["timestamp"].dt.floor("min")
    firewall["minuto"] = firewall["timestamp"].dt.floor("min")
    soma_ap = antenas.groupby("minuto")["bytes_sent"].sum().rename("soma_bytes_antenas")
    fw = firewall.set_index("minuto")[["bytes_sent", "active_sessions", "dropped_packets",
                                      "top_blocked_ip", "cpu_usage"]]
    fw.columns = ["fw_bytes_sent", "fw_active_sessions", "fw_dropped_packets",
                  "fw_top_blocked_ip", "fw_cpu_usage"]
    cruzado = antenas.merge(soma_ap, on="minuto").merge(fw, on="minuto", how="left")
    cruzado["diff_antenas_vs_fw"] = cruzado["soma_bytes_antenas"] - cruzado["fw_bytes_sent"]
    cruzado["consistente"] = (
        cruzado["diff_antenas_vs_fw"].abs() <= 0.05 * cruzado["fw_bytes_sent"]
    )
 
    cruzado["timestamp"] = cruzado["timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")
    cruzado.drop(columns=["minuto", "id_firewall"], errors="ignore").to_csv(
        f"{SAIDA}/silver_consolidado.csv", index=False
    )
    print("silver gerado:", len(cruzado), "linhas")
 
 
if __name__ == "__main__":
    main()

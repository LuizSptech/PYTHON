"""Camada 01 - coleta simulada e envio de JSON ao S3 (01-bronze), a cada 1 min. """
import json
import os
import random
import sys
import time
from datetime import datetime

import boto3
import psutil

BUCKET = os.getenv("BUCKET", "itops-0426130-2026")
PREFIXO = "01-bronze"
INTERVALO = 60

PESOS = {"ap01": 0.10, "ap02": 0.35, "ap03": 0.25, "ap04": 0.20, "ap05": 0.10}
 
s3 = boto3.client("s3")
 
 
def coletar_antena(ap_id):
    net = psutil.net_io_counters()
    peso = PESOS.get(ap_id, 0.1)
    return {
        "id_antena": ap_id,
        "bytes_sent": int(net.bytes_sent * peso),
        "bytes_recv": int(net.bytes_recv * peso),
        "active_conn": random.randint(0, 60),  
        "cpu_usage": round(random.uniform(10, 95), 1),
        "ram_usage": round(random.uniform(20, 90), 1),
    }
 
 
def coletar_firewall(fw_id):
    net = psutil.net_io_counters()
    atacando = random.random() < 0.15
    return {
        "id_firewall": fw_id,
        "active_sessions": random.randint(50, 500) + (2000 if atacando else 0),
        "dropped_packets": random.randint(0, 50) + (5000 if atacando else 0),
        "top_blocked_ip": ".".join(str(random.randint(1, 254)) for _ in range(4)),
        "cpu_usage": round(random.uniform(10, 70) + (25 if atacando else 0), 1),
        "ram_usage": round(random.uniform(20, 80), 1),
        "bytes_sent": net.bytes_sent,
        "bytes_recv": net.bytes_recv,
    }
 
 
def main():
    tipo, dispositivo = sys.argv[1], sys.argv[2]
    while True:
        agora = datetime.now()
        dado = coletar_antena(dispositivo) if tipo == "antena" else coletar_firewall(dispositivo)
        dado["timestamp"] = agora.strftime("%Y-%m-%d %H:%M:%S")
        nome = f"{agora:%Y-%m-%d_%H-%M}_{dispositivo}.json"
        s3.put_object(
            Bucket=BUCKET,
            Key=f"{PREFIXO}/{nome}",
            Body=json.dumps(dado).encode("utf-8"),
            ContentType="application/json",
        )
        print("enviado:", nome)
        time.sleep(INTERVALO)
 
 
if __name__ == "__main__":
    main()
 


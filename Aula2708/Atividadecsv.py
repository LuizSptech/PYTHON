import csv
import psutil
import time

for i in range(6):

    tempo = time.ctime()

    Ram = psutil.virtual_memory().percent
    frequencia = psutil.cpu_percent(interval=1)
    disco = psutil.disk_usage('/')

    horario_captura = tempo

    mensagemCPU = f"{round(frequencia, 2)}%"
    mensagemRAM = f"{round(Ram, 2)}%"
    mensagemDISCO = f"{round(disco.percent, 2)}%"

    with open('./frequencia.csv', 'w', newline='') as csvfile:

        arquivo = csv.writer(csvfile, delimiter=";")

        arquivo.writerow(["timestamp", horario_captura])
        arquivo.writerow(["cpu", mensagemCPU])
        arquivo.writerow(["ram", mensagemRAM])
        arquivo.writerow(["disco", mensagemDISCO])

    time.sleep(10)
import csv;
import psutil;
import time;

tempo = time.ctime()
Ram = psutil.virtual_memory()
memoriaRAM = ((Ram.total-Ram.available)/ Ram.total * 100) ;
frequencia = psutil.cpu_freq(percpu=False)
disco = psutil.disk_usage('/')




horario_captura = tempo
mensagemCPU = (f"{round(frequencia[0],2)}%")
mensagemRAM = (f"{round(memoriaRAM,2)}%")
mensagemDISCO = (f"{round(disco[1],2)}%")


with open('./frequencia.csv','w') as csvfile:
    csv.writer(csvfile, delimiter=";")
    csv.writer(csvfile).writerow(["timestamp",horario_captura])
    csv.writer(csvfile).writerow(["cpu",mensagemCPU])
    csv.writer(csvfile).writerow(["ram",mensagemRAM])
    csv.writer(csvfile).writerow(["disco",mensagemDISCO])
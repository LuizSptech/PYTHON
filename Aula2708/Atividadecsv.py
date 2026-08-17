import csv;
import psutil;
import time;

tempo = time.localtime()
Ram = psutil.virtual_memory()
memoriaRAM = ((Ram.total-Ram.available)/ Ram.total * 100) ;
frequencia = psutil.cpu_freq(percpu=False)
disco = psutil.disk_usage('/')

def tlg():
    for i in range(5):
        print(tempo[i])

tlg()
mensagemCPU = (f"frequencia da cpu {frequencia[0]}")
mensagemRAM = (f"uso de memoria ram {memoriaRAM}")
mensagemDISCO = (f"uso do disco {disco[1]}")


#with open('./frequencia.csv','w') as csvfile:
 #   csv.writer(csvfile).writerow([mensagemCPU])
  #  csv.writer(csvfile).writerow([mensagemRAM])
   # csv.writer(csvfile).writerow([mensagemDISCO])
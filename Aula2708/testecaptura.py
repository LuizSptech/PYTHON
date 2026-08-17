import psutil;


tempo = psutil.cpu_times(percpu=False)#retorna tempo gastos em diversos processos

#vou descobrir ainda
#Porcentagem
porcentoA = psutil.cpu_percent(interval=1)
porcentoB = psutil.cpu_percent(interval=None)
porcentoC = psutil.cpu_percent(interval=1, percpu=True)

frequencia = psutil.cpu_freq(percpu=False)

print(f"frequencia da cpu {frequencia[0]}")


print(f"processo executado em  { tempo[0]}")
print(f"bloqueado {porcentoA}")
print(f"não bloqueado {porcentoB}")
print(f"porcentagem de todos os nucleos {porcentoC[1]}")


Ram = psutil.virtual_memory()
alan = ((Ram.total-Ram.available)/ Ram.total * 100) ;

print(alan)
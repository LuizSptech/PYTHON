compra = [10.0,10.0,10.0,10.0,3.5,0.25]
recebido = [10.0,12.0,12.25,10.24,5.75,0.50]
troco = 0
log = []

for i in range(len(compra)):
    troco = recebido[i] - compra[i]
    log.append(troco)


balas = 0

for i in range(len(log)):
    i += i
    balas+= 1


print(balas)
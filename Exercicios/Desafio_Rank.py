eitcha = ["Java","JavaScript","Python","R","AWS"];
chutes = []
pontuacao = 0
erros = 0;
nomesCertos = []
nomesErraDOS = []


for i in range(5):
    palpite = input("Digite seu palpite: ")
    chutes.append(palpite);

print(chutes)

for i in range(5):
    if (eitcha[i] == chutes[i]):
        pontuacao += 1;
        nomesCertos.append(chutes[i])
else:
    erros += 1;
    nomesErraDOS.append(chutes[i])


print(nomesErraDOS)
print(nomesCertos)
print(pontuacao)
print(erros)
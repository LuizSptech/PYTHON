nome = input("digite seu nome: ");
qtdn = int(input("digite sua quantidade de notas: "));
quantidade = []
for i in range(qtdn):
     resposta = float(input("Digite sua nota: "))
     quantidade.append(resposta)


print(quantidade[:]);

def calculo(a,b):
    conta = 0
    for i in range(0,len(a)):
        conta += a[i]


    print(round(conta/b));
    if conta < 6:
        print("Reprovado")
    else:
        print("Aprovado")


calculo(quantidade, qtdn);











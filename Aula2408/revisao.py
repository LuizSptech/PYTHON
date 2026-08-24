marcas_de_jogos = {'rockstar', 'sega', 'nintendo', 'ubisoft', 'konami','playstation','steam'}

jogos_acao = set(['skyrim','Gta','unchertead','sifu','just cause','mortal kombat'])
jogos_terror = set(['lethal company', 'Dead by the light', 'the forest', 'outlast', 'devour'])
jogos_aventura = set(['Gta','pokemom', 'palword', 'skyrim', 'mario','sonic'])
jogos_Rpg = set(['Destiny', '', 'Baldurs Gate III','Perfect World','Albion online'])



#UNIÃO
Bliblioteca_Alan = marcas_de_jogos | jogos_terror
Bliblioteca_Luiz = marcas_de_jogos | jogos_Rpg
Bliblioteca_Ricardo = marcas_de_jogos | jogos_acao
Bliblioteca_Murilo = marcas_de_jogos | jogos_aventura
Familia_Steam1 = Bliblioteca_Alan.union(Bliblioteca_Ricardo)


#INTERSECÇÃO
Comuns = Bliblioteca_Alan & Bliblioteca_Ricardo

Bliblioteca_Alan.issubset(jogos_terror)
Bliblioteca_Alan.issubset(jogos_Rpg)



print(Familia_Steam1)


print(Comuns)

#PERTINÊNCIA
print('pokemom' in Bliblioteca_Murilo)
print('Gta' in Bliblioteca_Luiz)

#DIFERENÇA SIMÉTRICA
print(jogos_aventura ^ jogos_acao)
print(jogos_acao == jogos_aventura)

#ADICIONANDO / REMOVENDO

jogos_terror.add('the mimic')


jogos_aventura.remove('mario')

#COMPREENSOẼOS DE CONJUNTOS 


num = [1,2,2,3,4,5,6,6,7,8,9,10,10]

par = {item for item in num if item % 2 == 0}

print(par)
print(type(par))








#CRIAR OS PORTFÓLIOS PARA CADA CORRETORA


agora = {
    "nome": "Ágora",
    "Empresas": ["Itaúsa", "Ecorodovias", "Taesa", "B3", "Vale"],
    "Ticket": ["ITSA4", "ECOR3", "TAEE11", "B3SA3", "VALE3"]
}

ativa = {
    "nome": "Ativa",
    "Empresas": ["B3", "Bradesco", "BB Seguridade", "BR Distribuidora",
                 "Taesa", "CTEEP", "Vale", "Telefônica Brasil"],
    "Ticket": ["B3SA3", "BBDC4", "BBSE3", "BRDT3",
               "TAEE11", "TRPL4", "VALE3", "VIVT3"]
}

genial = {
    "nome": "Genial",
    "Empresas": ["CPFL", "Minerva", "Cyrela", "Random", "CTEEP"],
    "Ticket": ["CPFE3", "BEEF3", "SAPT4", "TRPL4"]
}

orama = {
    "nome": "Órama",
    "Empresas": ["Banco ABC", "Bradesco", "Minerva", "CESP", "Engie"],
    "Ticket": ["ABCB4", "BBDC4", "BEEF3", "CESP6", "EGIE3"]
}

#CONVERTER OS PORTFÓLIOS EM CONJUNTOS


#transforma apenas os tickets em conjuntos assim facilitando utilizar os metodos 
set_Emp1 = set(agora["Ticket"])
set_Emp2 = set(ativa["Ticket"])
set_Emp3 = set(genial["Ticket"])
set_Emp4 = set(orama["Ticket"])


# achar ações em comum 4.a

agora_ativa = set_Emp1 & set_Emp2
agora_genial = set_Emp1 & set_Emp3
agora_orama = set_Emp1 & set_Emp4
ativa_genial = set_Emp2 & set_Emp3
ativa_orama = set_Emp2 & set_Emp4
genial_orama = set_Emp3 & set_Emp4



acoes_comuns = set_Emp1 & set_Emp2 & set_Emp3 & set_Emp4;





print(acoes_comuns)





# 4.B/4.C mostrar as ações unicas e mostrar as relações entre os portifolios

print("As ações da Ágora também estão na Ativa:", set_Emp1 <= set_Emp2)
print("As ações da Ativa também estão na Ágora:", set_Emp2 <= set_Emp1)

print("As ações da Ágora também estão na Genial:", set_Emp1 <= set_Emp3)
print("As ações da Genial também estão na Ágora:", set_Emp3 <= set_Emp1)

print("As ações da Ágora também estão na Órama:", set_Emp1 <= set_Emp4)
print("As ações da Órama também estão na Ágora:", set_Emp4 <= set_Emp1)

print("As ações da Ativa também estão na Genial:", set_Emp2 <= set_Emp3)
print("As ações da Genial também estão na Ativa:", set_Emp3 <= set_Emp2)

print("As ações da Ativa também estão na Órama:", set_Emp2 <= set_Emp4)
print("As ações da Órama também estão na Ativa:", set_Emp4 <= set_Emp2)

print("As ações da Genial também estão na Órama:", set_Emp3 <= set_Emp4)
print("As ações da Órama também estão na Genial:", set_Emp4 <= set_Emp3)


# 4.d conjunto de ações unicas

unicas_agora = set_Emp1 - set_Emp2 - set_Emp3 - set_Emp4
unicas_ativa = set_Emp2 - set_Emp1 - set_Emp3 - set_Emp4
unicas_genial = set_Emp3 - set_Emp1 - set_Emp2 - set_Emp4
unicas_orama = set_Emp4 - set_Emp1 - set_Emp2 - set_Emp3


print("Ações únicas da Ágora:", unicas_agora)
print("Ações únicas da Ativa:", unicas_ativa)
print("Ações únicas da Genial:", unicas_genial)
print("Ações únicas da Órama:", unicas_orama)
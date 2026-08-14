import math

#print ('\n'*50)
a1=6.5;
b1=2.5;
# Vamos fazer operações mais elaboradas
# usando as 4 operações simples
soma = a1 + b1;
subtracao = a1-b1;
multiplicacao = a1 * b1
divisao = a1 / b1
#print ("Vamos mostrar todos os resultados")
#print ("a1=", a1)
#print ("b1=", b1)
#print ("a1+b1=",soma)
#print ("a1-b1=",subtracao)
#print ("a*b=",multiplicacao)
#print ("a/b=",divisao)


#EXERCICIO 1




valor = 2;

print(f"Potência ao quadrado: {valor*valor}");
print(f"Potência ao cubo: {valor ** 3}");
print(f"Potência à quarta: {valor ** 4}");



#EXERCICIO 2




# c = float(input("Insira um numero: "));
# d = float(input("Insira um numero: "));

# quadradro = pow(c,2)
# cubo = pow(c,3)
# quarta = pow(c,4)
# de = pow(c,d)

# print(f"c elevado ao quadrado = {quadradro}");
# print(f"c elevado ao cubo = {cubo}");
# print(f"c elevado a quarta = {quarta}");
# print(f"c elevado a d = {de}");



#EXERCICIO 3 


x = 512
raiz_cubica = x ** (1/3);
raiz_quarta = x ** (1/4)

print(f"raiz_quadrada_de_x = {(x ** 0.5)}");
print(f"raiz_cubica_de_x = {raiz_cubica}");
print(f"raiz_quarta_de_x = {raiz_quarta}");



#EXERCICIO 4

w = 3345.61;
piso = (math.floor(w));
teto = (math.ceil(w));
redondo = round(w);

print(piso)
print(teto)
print(redondo)


#EXERCICIO 5

decimal = 20.67

print(round(decimal))

# é considerada uma função in-biuld (criada junto com o python)


#EXERCICIO 6

x1 = 1.456
x2 = 3.678
x3 = 7.5

print(round(x1))
print(round(x2))
print(round(x3))


#EXERCICIO 7

resultado = math.floor(1.456)
print(resultado)
print(type(resultado))
resultado_float = float(math.floor(1.456))
print(resultado_float)
print(type(resultado_float))


#EXERCICIO 8


print(f"""   
    1: {math.pow(2,3)}
    2: {math.pow((-2),3)}
    3: {math.pow(1,0)}
    4: {math.pow((-1),0)}
    5: {math.pow(2,0)}
    6: {math.pow((2/5),3)}
    7: {math.pow(3,-2)}
    8: {math.pow(3,-2)}
    9: {math.pow(math.pow(-1,3),4)}
    10: {math.pow((0.5),3)}
    11: {math.pow((0.25),4)}
    12: {math.pow(0,4)}
    13: {math.pow(1 + 0.41, 2)}
   Não consegui realizar o resto 
    """)
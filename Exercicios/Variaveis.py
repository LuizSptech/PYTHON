# INT
age = 10;
lifes = 3;

# FLOAT


price = 29.90;
height = 1.82;

#STRING

name = "luiz";
city = "São paulo";

#BOOL

online = True;
offline = False;

#DESCOBRINDO TIPO DA VARIAVEL
print(type(name));
print(type(age));
print(type(price));
print(type(offline));


#CONCATENAÇÃO

print("Olá " + name);
print(name, age);


#CONVERSÃO DE TIPOS

number = int("10");
height = float("1.75");
text = str(age);
print("Idade: " + str(age));


#F-STRINGS

print(f"Hi my name is {name} and i am {age} years old");


a = 5;
b = 8;
print(f"{a} + {b} = {a + b}");


#INSERINDO / CONVERSÃO DE ENTRADA

name = input("Write your name: ");
print(name);
print(type(name))

age = int(input("Write your age: "));
print(age);
print(type(age));

print(f"your name is {name} and you are {age} years old")


#ATRIBUIÇÃO MULTIPLA - achei bizzaro

a, b, c  = 10, 20, 30;
a, b = b, c;
print(a);
print(b);


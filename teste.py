"""
x = "Luiz"
y = 26
 
mensagem1 = "meu nome é "+ x +  " tenho "  + str(y) +  " anos!"
mensagem2 = f"meu nome é {x} tenho {y} anos!"

print(mensagem1)
print(mensagem2)
-->

idade = int(input("digite sua idade: "))

if idade <12:
    print("criança")
elif 12<= idade <= 17:
    print("adolescente")
elif idade >= 18:
    print("adulto")


for i in range(5):
    print(i)


frutas = ["maça", "banana" , "uva"]

for fruta in frutas:
    print(fruta)

    
contador = 0

while contador < 5:
    print(contador)
    contador += 1


for i in range(1,11):
    print(i)

CONTADOR
contador = 1
soma = 0

while contador <=10:
    soma = soma + contador
    contador += 1
print(soma)

NUMEROS PRIMOS
numero = int(input("Digite um numero: "))

if numero <=1:
    print("Não é primo!")
else:
    eh_primo = True

    for divisor in range(2, numero):
     if numero % divisor == 0:
       eh_primo = False

    if eh_primo:
     print("É primo!")
    else:
     print("Não é primo!") 

TABUADA
numero = int(input("Digite um numero: "))



for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


n = int(input("Digite um numero "))

contador = 2
soma = 0

while contador <=n:
    soma = soma + contador
    contador += 2

print(soma)


maior = int(input("Digite um numero: "))

for i in range(4):
    numero = int(input("Digite um Numero: "))
    if numero > maior:
        maior = numero

print(maior)

numero = "FizzBuzz"
for i in range(1,31): 

    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

for numero in range(1, 6):
    print(f"Tabuada do {numero}")
    for multiplicador in range(1, 11):
     resultado = numero * multiplicador
     print(f"{numero} x {multiplicador} = {resultado}")
    print()

"""


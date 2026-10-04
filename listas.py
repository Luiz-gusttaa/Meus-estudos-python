
"""
criaçao de lista com adicionar na lista
"""

numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print(numeros)

maior = max(numeros)
menor = min(numeros)

print(f"maior: {maior}, menor:{menor}")

soma = 0

for numero1 in numeros:
    soma = soma + numero1

media = soma / len(numeros)
print(media)

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
     pares += 1
    else:
       impares +=1


print(f"pares: {pares}")
print(f"impares: {impares}")

    





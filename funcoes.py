"""
Criar funçao de soma de pares

"""
""""
def soma_pares(n): 
    contador = 2
    soma = 0

    while contador <=n:
        soma = soma + contador
        contador += 2
    return soma

resultado1 = soma_pares(20)
print(resultado1)

resultado2 = soma_pares(30)
print(resultado2)
"""


"""
Funçao de maior numero

"""

"""
def maior_de_dois(a, b ):
    if a > b:
     return a
    else:
       return b

resultado1 = maior_de_dois(7, 12)
print(resultado1)

resultado2 = maior_de_dois(20, 5)
print(resultado2)
"""

"""
Funçao numeros primos

"""

"""
def eh_numero_primo(numero):
    if numero <=1:
     return False
    else:
     eh_primo = True

     for divisor in range(2, numero):
      if numero % divisor == 0:
       eh_primo = False
     return eh_primo

numero = int(input("Digite um numero: "))

if eh_numero_primo(numero):
  print("é primo!")
else:
  print("Não é Primo!")

"""

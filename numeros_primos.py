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

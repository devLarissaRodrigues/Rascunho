# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Digite uma base: "))
expoente = int(input("Digite um expoente positivo: "))

#Ex: 2**4 = 2*2*2*2
potencia = 1

if expoente >= 0:
  for i in range(expoente):
    potencia *= base

else:
  for i in range(expoente):
    potencia *= (base/1)

print(potencia)
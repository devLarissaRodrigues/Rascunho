# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

populacaoA = int(input("Digite a população A: "))
taxaA = float(input("Digite a taxa de crescimento da população A: "))

populacaoB = int(input("Digite a população B: "))
taxaB = float(input("Digite a taxa de crescimento da população B: "))

anos = 0

if populacaoA < populacaoB:
  
  while populacaoA <= populacaoB:
    populacaoA = populacaoA + (populacaoA * taxaA)
    populacaoB = populacaoB + (populacaoB * taxaB)
    anos += 1

elif populacaoA > populacaoB:

  while populacaoB <= populacaoA:
    populacaoA = populacaoA + (populacaoA * taxaA)
    populacaoB = populacaoB + (populacaoB * taxaB)
    anos += 1

else:
  print("A população do país A já é igual à população do país B")
    

if populacaoA != populacaoB:
  print(anos)
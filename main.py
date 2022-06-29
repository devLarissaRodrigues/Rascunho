sequencia = input("Digite uma sequência que você deseje inverter: ")

nova_sequencia = ""
for item in range(len(sequencia)):
  nova_sequencia = sequencia[item] + nova_sequencia

print(nova_sequencia)
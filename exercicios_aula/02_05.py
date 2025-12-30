# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.


nome = input("Insira seu nome completo: ")
nome_split = nome.lower().split(" ")

if 'calvo' in nome_split:
    print("Essa pessoa é da Familia Calvo")
    
if 'silva' in nome_split:
    print("Essa pessoa é da Familia Silva")
    
if "silva" not in nome_split and "calvo" not in nome_split:
    print("Essa pessoa não é Silva, nem Calvo")
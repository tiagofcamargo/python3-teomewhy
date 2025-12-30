# Altere o programa anterior para considerar a quantidade de garrafas de água


tipo = input("Escolha um tipo de agua: (1) Água mineral Natural / (2) Água mineral com Gás: ")
qtde = int(input("Qual a quantidade de garrafas? "))

valor = 0

if tipo == "1":
    valor = 1.5 * qtde
    print("Total: R$", valor)
elif tipo == "2":
    valor = 2.5 * qtde
    print("Total: R$", valor)
else:
    print("Entre com dados válidos!")
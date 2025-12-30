# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

tipo = input("Escolha um tipo de agua: (1) Água mineral Natural / (2) Água mineral com Gás: ")

if tipo == "1":
    print("Valor: R$1,50")
elif tipo == "2":
    print("Valor: R$2,50")
else:
    print("Entre com um valor válido.")
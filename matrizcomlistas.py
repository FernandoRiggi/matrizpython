#Faça um programa que preencha uma matriz 7 x 7 de inteiros e crie duas listas
#com 7 posições cada que contenham, respectivamente, o maior elemento de cada
#linha e o menor elemento de cada linha. 
matriz = []
i=0
while i<7:
    j=0
    linha = []
    while j<7:
        num = int(input(f"Escolha o valor do elemento [{i},{j}]: "))
        linha.append(num)
        j+=1
    matriz.append(linha)
    del linha
    i+=1
maiorlinha = []
for lin in range(7):
    maior=0
    for col in range(7):
        if maior< matriz[lin][col]:
            maior = matriz[lin][col]
    maiorlinha.append(maior)
menorlinha =[]
for lin in range(7):
    menor = 10**9
    for col in range(7):
        if menor>matriz[lin][col]:
            menor = matriz[lin][col]
    menorlinha.append(menor)
print(f"Os maiores elementos de cada linha são {maiorlinha}")
print(f"Os menores elementos de cada linha são {menorlinha}")

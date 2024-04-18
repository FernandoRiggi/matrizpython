#Escreva um programa que leia inteiros positivos m e n e os elementosde uma matriz A
# de números inteiros de dimensão m x n e ao
# finalmostra a quantidade de linhas e colunas que tem apenas zeros (linhasnulas e colunas nulas).
matriz = []
M = int(input("Entre com a quantidade de linhas da matriz: "))
N = int(input("Entre com a quantidade de colunas da matriz: "))
for i in range(M):
    linhas=[]
    print(f"Informe os elementos da linha {i}")
    for j in range(N):
        elementos = int(input(f"Digite os elementos da coluna {j}: "))
        linhas.append(elementos)
    matriz.append(linhas)
contador_col_nula = 0
for col in range(N):
    nula = True
    for lin in range(M):
        if matriz[lin][col] !=0:
            nula = False
    if nula == True:
        contador_col_nula +=1
contador_lin_nula = 0
for lin in range(M):
    nula = True
    for col in range(N):
        if matriz[lin][col] !=0:
            nula = False
    if nula == True:
        contador_lin_nula +=1
print(f"A quantidade de colunas nulas é = {contador_col_nula}")
print(f"A quantidade de linhas nulas é = {contador_lin_nula}")
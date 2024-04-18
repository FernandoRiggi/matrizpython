#Crie um programa que preencha uma matriz 3x3 de números inteiros e verifique
#se essa matriz forma um quadrado mágico. Um quadrado mágico é formado
#quando a soma dos elementos de cada linha é igual:
#- à soma dos elementos de cada coluna da matriz;
#- à soma dos elementos da diagonal principal;
#- à soma dos elementos da diagonal secundária;
matriz = []
i = 0
while i<3:
    linha = []
    j=0
    while j<3:
        num = int(input(f"Escolha o valor do elemento [{i},{j}]: "))
        linha.append(num)
        j+=1
    matriz.append(linha)
    del linha
    i+=1
matrizlinha = [] #servirá para testar as somas das linhas 
col=0
for lin in range(3):
    soma_linha = 0
    for col in range(3):
        soma_linha += matriz[lin][col]
    matrizlinha.append(soma_linha)
j=0
matrizcoluna = [] # servirá para testar as somas das colunas
while j<3:
    i=0
    somacoluna = 0
    while i<3:
        somacoluna = somacoluna + matriz[i][j]
        i+=1
    matrizcoluna.append(somacoluna)
    j+=1
soma_diagonalp = 0
i=0
while i<3:
    j=0
    while j<3:
        soma_diagonalp += matriz[i][j] #soma diagonal principal
        j+=1
        i+=1
i=0
j=2
soma_diagonals = 0
while i<3:
    while j>=0:
        soma_diagonals += matriz[i][j] #soma diagonal secundária
        j-=1
        i+=1
i=0
quad_mágico = True
while i<3 and quad_mágico == True:
    j=0
    while j<3:
        if matrizlinha[i] != soma_diagonalp:
            quad_mágico = False
        elif matrizlinha[i] != soma_diagonals:
            quad_mágico = False
        elif matrizlinha[i] != matrizcoluna[j]:
            quad_mágico = False
        j+=1
    i+=1
if quad_mágico == True:
    print("A matriz forma um quadrado mágico")
else:
    print("A matriz não forma um quadrado mágico")

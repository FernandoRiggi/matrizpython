#Faça um programa que solicite do usuário um valor N, representando adimensão de uma matriz quadrada (matriz A).
# m seguida, o programadeverá solicitar do usuário os elementos da matriz A e,
#posteriormente,deverá criar a matriz transposta de A (At).
#Ao final, deve ser mostrada amatriz original e sua respectiva transposta.
#Lembre-se que a matriztransposta At será obtida a partir da matriz A trocando-seordenadamente as linhas por colunas
matriz = [] #matriz vazia
N = int(input("Escolha o valor da matriz quadrada: "))
for i in range (N): #linha
    linhas = [] #linhas da matriz
    print(f"Informe os elementos da linha {i}")
    for j in range (N): #coluna
        elementos = int(input(f"Digite os elementos da coluna {j}: "))
        linhas.append(elementos)
    matriz.append(linhas)
matrizt = [] #matriz transposta
i = 0
for i in range(N): #linha
    linhat = [] #linhas da matriz transposta
    for j in range(N): #coluna
        linhat.append(matriz[j][i])
    matrizt.append(linhat)
    del linhat
print(f"A matriz é = {matriz}")
print(f"A matriz transposta é = {matrizt}")
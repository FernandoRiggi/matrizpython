#Crie um programa que solicita do usuário um valor N representando aquantidade linhas e um valor M representando a quantidade de colunasde uma matriz.
# Depois, o programa deverá solicitar do usuário N x Melementos para serem incluídos na matriz.
# Por fim, o programa deverápercorrer a matriz para encontrar e imprimir o seu maior elemento e oseu menor elemento.
matriz = []
N = int(input("Entre com a quantidade de linhas da matriz: "))
M = int(input("Entre com a quantidade de colunas da matriz: "))
for i in range(N):
    Linhas = []
    print(f"Informe os elementos da linha {i}: ")
    for j in range(M):
        elementos = int(input(f"Entre com os elementos da coluna {j}; "))
        Linhas.append(elementos)
    matriz.append(Linhas)
maior = matriz[0][0]
menor = matriz[0][0]
i=0
while i < N:
    j=0
    while j < M:
        if maior < matriz[i][j]:
            maior = matriz[i][j]
        elif menor > matriz[i][j]:
            menor = matriz[i][j]
        j+=1
    i+=1    
print(f"O maior elemento é {maior}")
print(f"O menor elemento é {menor}")
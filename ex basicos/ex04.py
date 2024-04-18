#Faça um programa que crie uma matriz A de tamanho n x n de valoresinteiros informados pelo usuário.
# O programa deverá verificar se A éuma matriz identidade e imprimir uma mensagem informando ousuário. 
#Considere que a matriz identidade possui todos oselementos da diagonal principal iguais a 1 e os demais elementosiguais a 0
matriz = []
N = int(input("Escolha o valora da matriz quadradda: "))
for i in range(N):
    linhas=[]
    print(f"Informe os elementos da linha {i}")
    for j in range(N):
        elementos = int(input(f"Digite os elementos da coluna {j}: "))
        linhas.append(elementos)
    matriz.append(linhas)
identidade = True
for i in range(N):
    for j in range(N):
        if i == j and matriz[i][j]!=1:
             identidade = False
        elif i!= j and matriz[i][j] !=0:
             identidade = False
if identidade == True:
    print("É uma matriz identidade")
else:
    print("Não é uma matriz identidade")
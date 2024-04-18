#Escreva um programa que preencha uma matriz A m x n e uma matrizB n x p, ambas com valores inteiros. 
#Em seguida, o programa devemostrar a matriz A (mxn), a matriz B (nxp) 
#e a matriz C (mxp),representando o produto entre A e B.
matrizA = []
matrizB = []
matrizC = []
mA = int(input("Digite a quantidade de linhas da matriz A: "))
nA = int(input("Digite a quantidade de colunas da matriz A: "))
for i in range(mA):
    linhasA = []
    print(f"Informe os elementos da linha {i}")
    for j in range(nA):
        elementosA = int(input(f"Digite os elementos de [{i} {j}]: "))
        linhasA.append(elementosA)
    matrizA.append(linhasA)
mB = int(input("Digite a quantidade de linhas da matriz B: "))
nB = int(input("Digite a quantidade de colunas da matriz B: "))
for i in range(mB):
    linhasB= []
    print(f"Informe os elementos da linha {i}")
    for j in range(nB):
        elementosB = int(input(f"Digite os elementos de [{i} {j}]: "))
        linhasB.append(elementosB)
    matrizB.append(linhasB)
if nA == mB:
    for i in range(mA):
        linhasC = []
        for j in range(nB):
            soma =0
            for k in range(nA):
                soma = soma + (matrizA[i][k]*matrizB[k][j])
            linhasC.append(soma)
        matrizC.append(linhasC)
print(f"A matriz A é = {matrizA}")
print(f"A matriz B é = {matrizB}")
print(f"A matriz C é = {matrizC}")
#Crie um programa que preencha uma matriz 10 x 20 de números inteiros e some
#cada uma das linhas, armazenando o resultado das somas em uma lista. Em
#seguida, o programa deverá multiplicar cada elemento da matriz pelo elemento da
#linha correspondente na lista e mostrar a matriz resultante
matriz = []
i = 0
while i<10:
    j=0
    linha = []
    while j<20:
        num = int(input(f"Escolha o valor do elemento [{i},{j}]: "))
        linha.append(num)
        j+=1
    matriz.append(linha)
    del linha
    i+=1
somalinhas=[]
for lin in range(10):
    soma=0
    for col in range(20):
        soma += matriz[lin][col]
    somalinhas.append(soma)
print(f"A soma dos elementos de cada linha é = {somalinhas}")
matrizmult=[]
for lin in range(10):
    mult =[]
    for col in range(20):
        elementosmult = matriz[lin][col]*lin
        mult.append(elementosmult)
    matrizmult.append(mult)
    del mult
print(f"A matriz resultante de cada elemento multiplicado pelo valor de sua linha é = {matrizmult}")
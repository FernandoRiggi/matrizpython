#Na teoria dos sistemas, o elemento MINMAX de uma matriz é o maior elemento
#da linha em que se encontra o menor elemento da matriz. Elabore um programa
#que carregue uma matriz 4 x 5 com números reais, identifique e mostre o
#MINMAX e a sua posição na matriz. 
matriz = []
i = 0
while i<4:
    j=0
    linha=[]
    while j<5:
        num = int(input(f"Escolha o valor do elemento [{i},{j}]: "))
        linha.append(num)
        j+=1
    matriz.append(linha)
    del linha
    i+=1
menor = matriz[0][0]
for lin in range(4):
    for col in range(5):
        if menor>=matriz[lin][col]:
            menor = matriz[lin][col]
            linha_menor = lin
maior = matriz[linha_menor][0]
for col in range(5):
    if maior < matriz[linha_menor][col]:
        maior = matriz[linha_menor][col]
for lin in range(4):
    for col in range(5):
        if maior == matriz[lin][col]:
            linha = lin
            coluna = col
print(f"O elemento MINMAX é {maior} e sua posição é [{linha},{coluna}]")
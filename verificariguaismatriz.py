#Escrever um programa que preencha 2 matrizes (a e b) de 3 linhas x 4 colunas com
#números aleatórios e não repetidos (entre 0 e 100). Em seguida, verifique a
#existência de números iguais nas duas matrizes, imprimindo-os. No exemplo a
#seguir apenas o número 4 aparece em ambas matrizes. 
A = []
B=[]
i=0
linhas = []
while i <3:
    linha=[]
    j=0
    while j<4:
        num = int(input(f"Para a matriz A, escolha o valor do elemento [{i},{j}]: "))
        if num not in linhas:
            linha.append(num)
            linhas.append(num)
            j+=1
        else: 
            print("Número repetido, escolha outro")
    A.append(linha)
    i+=1
i=0
linhas2=[]
while i<3:
    linha=[]
    j=0
    while j<4:
        num= int(input(f"Para a matriz B, escolha o valor do elemento [{i},{j}]: "))
        if num not in linhas2:
            linha.append(num)
            linhas2.append(num)
            j+=1
        else:
            print("Número repetido, escolha outro")
    B.append(linha)
    i+=1
iguais =0
listaiguais = []
i = 0
while i<3:
    j=0
    while j<4:
        k=0
        while k<3:
            z=0
            while z<4:
                if A[i][j]==B[k][z]:
                    iguais+=1
                    listaiguais.append(A[i][j])
                z+=1
            k+=1
        j+=1
    i+=1
print(f"Matriz A: {A}")
print(f"Matriz B: {B}")
if len(listaiguais)>0:
    print(f"A quantidade de números iguais é = {iguais} e os números iguais são {listaiguais}")
else:
    print("Não há números iguais nas matrizes")

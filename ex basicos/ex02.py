#Faça um programa que solicite do usuário um valor N, representando adimensão de uma matriz quadrada (matriz A). 
#Em seguida, o programadeverá solicitar do usuário os elementos da matriz A e, 
#posteriormente,deverá verificar se A é simétrica. 
#A matriz será simétrica se e somente setodo elemento A[i,j] = A[j,i].
matriz = []
N = int(input("Digite o valor da dimensão da matriz quadrada: "))
linha = N
coluna = N
for i in range (linha):
    linhas=[]
    print(f"Informe os elementos da linha {i}")
    for j in range (coluna):
        elementos = int(input(f"Entre com os elementos da coluna {j}: "))
        linhas.append(elementos)
    matriz.append(linhas)
i = 0
simetria = True
while i < linha:
    j = 0
    while j < coluna and simetria ==True:
        if matriz[i][j] != matriz[j][i] and i!=j:
            simetria = False
        elif matriz[i][j] == matriz[j][i] and i!=j:
            simetria = True
        j+=1    
    i+=1
if simetria == True:
    print("Matriz simétrica")
if simetria == False:
    print("Matriz não é simétrica")
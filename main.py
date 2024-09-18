from random import random

lA = int(input("Digite o nº de linhas de A: "))
cA = int(input("Digite o nº de colunas de A: "))

lB = int(input("Digite o nº de linhas de B: "))
cB = int(input("Digite o nº de colunas de B: "))

def questao_1(lA,cA,lB,cB):
 #CADASTRO DE MATRIZES
    A = [None]* lA
    for i in range(len(A)):
        A[i] = [None]*cA

    B = [None]* lB
    for i in range(len(B)):
        B[i] = [None]*cB

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = int(random()*11)

    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = int(random()*11)

    print(A)
    print(B)

    x = int(input("Digite x: "))
    y = int(input("Digite y: "))

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = A[i][j] * x

    print('Matriz A')
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end='    ')
        print()
    print()
    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = B[i][j] * y

    print('Matriz B')
    for i in range(len(B)):
        for j in range(len(B[i])):
            print(B[i][j], end='    ')
        print()

def questao_2(lA,cA,lB,cB):
 #CADASTRO DE MATRIZES
    A = [None]* lA
    for i in range(len(A)):
        A[i] = [None]*cA

    B = [None]* lB
    for i in range(len(B)):
        B[i] = [None]*cB

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = int(random()*11)

    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = int(random()*11)


    print('Matriz A')
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end='    ')
        print()
    print()
    
    print('Matriz B')
    for i in range(len(B)):
        for j in range(len(B[i])):
            print(B[i][j], end='    ')
        print()
    print()
    
    #Cadastro da Matriz C
    C = [None]*cA
    for i in range(len(C)):
        C[i] = [None]*lA

    for i in range(len(C)):
        for j in range(len(C[i])):
            C[i][j] = A[j][i]
    
    print("Matriz C")
    for i in range(len(C)):
        for j in range(len(C[i])):
            print(C[i][j], end='    ')
        print()
    print()
    
    #Cadastro da Matriz D
    D = [None]*cB
    for i in range(len(D)):
        D[i] = [None]*lB

    for i in range(len(D)):
        for j in range(len(D[i])):
            D[i][j] = B[j][i]
    
    print("Matriz D")
    for i in range(len(D)):
        for j in range(len(D[i])):
            print(D[i][j], end='    ')
        print()
    print()
 
def questao_3(lA,cA,lB,cB):
 if lA != lB or cA != cB:
    print("As linhas e colunas de A devem ser iguais as linhas e colunas de B")
 else:

 #CADASTRO DE MATRIZES A e B
    A = [None]* lA
    for i in range(len(A)):
        A[i] = [None]*cA

    B = [None]* lB
    for i in range(len(B)):
        B[i] = [None]*cB

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = int(random()*11)

    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = int(random()*11)

 #Impressão das Matrizes A e B

    print('Matriz A')
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end='    ')
        print()
    print()
    
    print('Matriz B')
    for i in range(len(B)):
        for j in range(len(B[i])):
            print(B[i][j], end='    ')
        print()
    print()
    
 #Cadastro da Matriz A + B
    AB = [None]*lA
    for i in range(len(AB)):
        AB[i] = [None]*cB
    
    for i in range(len(AB)):
        for j in range(len(AB[i])):
            AB[i][j] = (A[i][j]+B[i][j])
    
    print("Matriz A + B")
    for i in range(len(AB)):
        for j in range(len(AB[i])):
            print(AB[i][j],end ='  ')
        print()
    print()

def questao_4(lA,cA):
 #CADASTRO DE MATRIZES
    A = [None]* lA
    for i in range(len(A)):
        A[i] = [None]*cA

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = int(random()*11)
        
    print("Matriz A")
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end='    ')
        print()
    print()
    if lA == cA:
        print("Diagonal Principal")
        for i in range(len(A)):
            for j in range(len(A[i])):
                if i == j:
                    print(A[i][j],end='  ')
                else:
                    print(end='  ')
            print()
        print()

        print("Diagonal Secundária")
        for i in range(len(A)):
            for j in range(len(A[i])):
                if (i+j) == len(A)-1:
                    print(A[i][j],end='  ')
                else:
                    print(end='  ')
            print()
        print()
    else:
        maior = A[0][0]
        posmaiorlinha = 0
        posmaiorcoluna = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] > maior:
                    maior = A[i][j]
                    posmaiorlinha = i
                    posmaiorcoluna = j
        print(f"O maior vale {maior} e está na linha {posmaiorlinha+1} e na coluna {posmaiorcoluna+1}")

def questao_5(lB,cB):
#CADASTRO DE MATRIZES
    B = [None]* lB
    for i in range(len(B)):
        B[i] = [None]*cB

    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = int(random()*11)
        
    print("Matriz B")
    for i in range(len(B)):
        for j in range(len(B[i])):
            print(B[i][j], end='  ')
        print()
    print()
    if lB == cB:
        print("Diagonal Principal")
        for i in range(len(B)):
            for j in range(len(B[i])):
                if i == j or j > i:
                    print(B[i][j],end='  ')
                else:
                    print(end='   ')
            print()
        print()
    else:
        menor = B[0][0]
        posmenorlinha = 0
        posmenorcoluna = 0
        for i in range(len(B)):
            for j in range(len(B[i])):
                if B[i][j] < menor:
                    menor = B[i][j]
                    posmenorlinha = i
                    posmenorcoluna = j
        print(f"O menor vale {menor} e está na linha {posmenorlinha+1} e na coluna {posmenorcoluna+1}")











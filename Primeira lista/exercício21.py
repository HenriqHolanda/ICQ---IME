import numpy as np

def leitura_matriz():
    # Solicitar ao usuário as dimensões da matriz
    num_linhas = int(input("Digite o número de linhas da matriz: "))
    num_colunas = int(input("Digite o número de colunas da matriz: "))
    
    #No python não precisa usar as dimensões na hora de declarar a matriz
    matriz = []
    
    print("Digite os elementos da matriz linha por linha:")
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            #Como é complexo, eu tenho que receber dois números agora, ai utilzo o split pra receber esses dois numeros
            #Esse map(float) ai é porque eles inicialmente vem no tipo string ai tem que mudar para um número de ponto flutuante
            parte_real, parte_imaginaria = map(float, input(f"Digite o elemento da linha {i+1} e coluna {j+1}: ").split())
            linha.append(complex(parte_real, parte_imaginaria))
        matriz.append(linha)
    
    return matriz

print("Matriz 1: ")
matriz1 = leitura_matriz()

print("Matriz 2: ")
matriz2 = leitura_matriz()

matriz3 = np.kron(matriz1, matriz2)

print(f"o produto tensorial entre a matriz1 e a matriz2 {matriz3}")
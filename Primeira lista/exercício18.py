def traco(m):
    # Inicializa o traço como 0
    traco = 0
    
    # Loop sobre os elementos da diagonal principal e adiciona-os ao traço
    for i in range(min(len(m), len(m[0]))):
        traco += m[i][i]
    
    return traco

def leitura_matriz():
    # Solicitar ao usuário as dimensões da matriz
    num_linhas = int(input("Digite o número de linhas da matriz: "))
    num_colunas = int(input("Digite o número de colunas da matriz: "))
    
    #No python não precisa usar as dimensões na hora de declarar a matriz
    matriz = []
    
    # Solicitar ao usuário os elementos da matriz
    print("Digite os elementos da matriz linha por linha:")
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = float(input(f"Digite o elemento da linha {i+1} e coluna {j+1}: "))
            linha.append(elemento)
        matriz.append(linha)
    
    return matriz

print("Matriz 1: ")
matriz1 = leitura_matriz()

print(f"o traço da matriz é: {traco(matriz1)}")
def soma(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return "Impossível realizar a soma devido as dimensões."
    
    resultado = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[0])):
            linha.append(m1[i][j] + m2[i][j])
        resultado.append(linha)
    
    return resultado

def multiplicacao_escalar(m, escalar):
    resultado = []
    for linha in m:
        linha_resultado = [elemento * escalar for elemento in linha]
        resultado.append(linha_resultado)
    
    return resultado


#inversa é o mesmo código da multiplicação por escalar só que com -1
def inversa(m):
    resultado = []
    for linha in m:
        linha_resultado = [-elemento for elemento in linha]
        resultado.append(linha_resultado)
    
    return resultado

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

print("Matriz 2: ")
matriz2 = leitura_matriz()

print(f"A soma das matrizes é igual a: {soma(matriz1, matriz2)}")

print(f"A inversa da matriz 1 é igual a: {inversa(matriz1)}")

print(f"A inversa da matriz 2 é igual a: {inversa(matriz2)}")

print(f"A multiplicação da matriz 1 por 2 é igual a: {multiplicacao_escalar(matriz1, 2)}")

print(f"A multiplicação da matriz 1 por 2 é igual a: {multiplicacao_escalar(matriz2, 2)}")

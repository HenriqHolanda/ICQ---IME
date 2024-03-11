import numpy as np

#A numpy tem uma funções pra encontrar a adjunta, conjugada e a transposta

def transposta_conjugada_dagger(m):
    
    transposta = np.transpose(m)
    conjugada = np.conj(m)
    dagger = np.transpose(np.conj(m))
    
    return transposta, conjugada, dagger

# Para receber valores complexos, eu vou mudar um pouco o código da questão passada
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

m_complexa = leitura_matriz()

# Encontrar a transposta, conjugada e adjunta (dagger) da m complexa
transposta, conjugada, dagger = transposta_conjugada_dagger(m_complexa)

# Imprimir os resultados
print("\nmatriz Transposta:")
print(transposta)

print("\nmatriz Conjugada:")
print(conjugada)

print("\nmatriz Dagger:")
print(dagger)
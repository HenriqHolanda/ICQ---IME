import numpy as np
import matplotlib.pyplot as plt


def mult_c_r(c, r):
    # Multiplicação do número c pelo número r
    resultante = c * r

    c_real = c.real
    c_imaginaria = c.imag
    resultante_real = resultante.real
    resultante_imaginaria = resultante.imag


    v1 = np.array([c_real, c_imaginaria])
    v2 = np.array([resultante_real, resultante_imaginaria])
    
    # Plotando os vetores
    plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vetor 1')
    plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Resultante')    
    
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.axhline(0, color='k', linestyle='--', linewidth=1)
    plt.axvline(0, color='k', linestyle='--', linewidth=1)
    plt.xlabel('Eixo Real')
    plt.ylabel('Eixo Imaginário')
    plt.grid(True)
    plt.legend()
    plt.title('Multiplicação de um Número c por um Número r real')
    plt.show()


#testando a função
c = 1 + 1j
r = 3

#Chamando a função para multiplicar o número c pelo número r
mult_c_r(c, r)


def mult_c_b(c, b):
    # Multiplicação do número c pelo número b imaginário
    resultante = c * b

    c_real = c.real
    c_imaginaria = c.imag
    resultante_real = resultante.real
    resultante_imaginaria = resultante.imag


    v1 = np.array([c_real, c_imaginaria])
    v2 = np.array([resultante_real, resultante_imaginaria])
    

    plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vetor 1')
    plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Resultante')    
    

    plt.xlim(-10, 10)
    plt.ylim(-5, 5)
    plt.axhline(0, color='k', linestyle='--', linewidth=1)
    plt.axvline(0, color='k', linestyle='--', linewidth=1)
    plt.xlabel('Eixo Real')
    plt.ylabel('Eixo Imaginário')
    plt.grid(True)
    plt.legend()
    plt.title('Multiplicação de um Número c por um Número b imaginário')
    plt.show()


#Fazendo outro teste
c = 1 + 3j
b = 3j

#Chamando a função para multiplicar o número c pelo número b imaginario
mult_c_b(c, b)


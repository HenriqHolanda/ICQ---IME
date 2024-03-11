import matplotlib.pyplot as plt

#Para calcular a soma dos vetores e mostrar elas graficamente vamos utilizar a biblioteca matplotlib

v1 = [2, -1]
v2 = [1, 1]


resultante = [v1[0] + v2[0], v1[1] + v2[1]]

#Quiver para plotar os vetores
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vetor 1')
plt.quiver(v1[0], v1[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vetor 2')
plt.quiver(0, 0, resultante[0], resultante[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Resultante')


plt.xlim(-1, 4)
plt.ylim(-2, 2)
plt.axhline(0, color='k', linestyle='-', linewidth=1)
plt.axvline(0, color='k', linestyle='-', linewidth=1)
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)
plt.legend()
plt.title('Adição de vetores')
plt.show()
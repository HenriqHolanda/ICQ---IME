import numpy as np
import matplotlib.pyplot as plt

#Para pegar a representação polar vamos precisar da biblioteca numpy pois ela tem a função arctan e np.liang.norm

# Definindo os vetores
v1 = np.array([2, -1])
v2 = np.array([1, 1])

# Convertendo para representação polar
teta1 = np.arctan2(v1[1], v1[0])
teta2 = np.arctan2(v2[1], v2[0])

r1 = np.linalg.norm(v1)
r2 = np.linalg.norm(v2)

# Calculando a soma dos vetores
resultante = v1 + v2
tetares = np.arctan2(resultante[1], resultante[0])
rres = np.linalg.norm(resultante)

# Plotando os vetores na representação polar
plt.figure(figsize=(8, 8))

# Vetor 1
plt.polar([0, teta1], [0, r1], marker='o', label='Vetor 1')
# Vetor 2
plt.polar([0, teta2], [0, r2], marker='o', label='Vetor 2')
# Soma dos vetores
plt.polar([0, tetares], [0, rres], marker='o', label='Resultante')


plt.legend()
plt.title('Soma dos vetores em cord polar')
plt.grid(True)
plt.show()
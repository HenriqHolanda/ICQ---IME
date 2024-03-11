import numpy as np
import matplotlib.pyplot as plt

n1 = input("Insira o numero complexo na forma a+bj: ")

z1 = complex(n1)

def soma(z, n):
    ans = z + n

    ans_real = ans.real
    ans_imaginaria = ans.imag

    v = np.array([ans_real, ans_imaginaria])
    return v

v1 = soma(z1, 1)
v2 = soma(z1, 2)
v3 = soma(z1, 3)
v4 = soma(z1, 4)
v5 = soma(z1, 5)
v6 = soma(z1, 6)
v7 = soma(z1, 7)
v8 = soma(z1, 8)
v9 = soma(z1, 9)
v10 = soma(z1, 10)

plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'{z1} somado 1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'{z1} somado 2')
plt.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'{z1} somado 3')
plt.quiver(0, 0, v4[0], v4[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'{z1} somado 4')
plt.quiver(0, 0, v5[0], v5[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'{z1} somado 5')
plt.quiver(0, 0, v6[0], v6[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'{z1} somado 6')
plt.quiver(0, 0, v7[0], v7[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'{z1} somado 7')
plt.quiver(0, 0, v8[0], v8[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'{z1} somado 8')
plt.quiver(0, 0, v9[0], v9[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'{z1} somado 9')
plt.quiver(0, 0, v10[0], v10[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'{z1} somado 10')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='k', linestyle='--', linewidth=1)
plt.axvline(0, color='k', linestyle='--', linewidth=1)
plt.xlabel('Eixo Real')
plt.ylabel('Eixo Imaginário')
plt.grid(True)
plt.legend()
plt.title('Multiplicação de um Número c por um Número r real')
plt.show()
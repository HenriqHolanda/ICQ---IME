from sympy import I, re, im

def f(x): #Definindo f(x)
    return x**2 + 2*x + 2

z1 = -1 + I

parte_real = re(f(z1))
parte_imaginaria = im(f(z1))

print(f"O valor de f(-1 + i) é igual a: {parte_real} + {parte_imaginaria}i = 0")
print("Logo -1 + i é solução do polinômio")
import sympy

x = sympy.symbols('x') #Definindo a variável do problema
equação = sympy.Eq(x**4 + 2*x**2 + 1, 0) #Definindo a equação do nosso interesse

resposta = sympy.solve(equação, x) #sympy.solve me retorna uma lista com todas as soluções do problema.

print(f"as soluções são: {resposta}")
print("Note que não temos soluções reais!")
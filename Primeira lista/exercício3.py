from sympy import I, re, im

#Da biblioteca sympy podemos trabalhar com o número imaginário

c1 = 3 - I
c2 = 1 + 4*I

soma = c1 + c2
produto = c1 * c2

#testando o re() e o im()

parte_reals = re(soma)
parte_imaginarias = im(soma)

parte_realp = re(produto)
parte_imaginariap = im(produto)

print(f"c1 + c2 é igual a: {parte_reals} + {parte_imaginarias}I")
print(f"c1 * c2 é igual a: {parte_realp} + {parte_imaginariap}I")
# Solicitar ao usuário dois números complexos no formato a+bj
c1 = complex(input("Digite o primeiro complexo no formato a+bj: "))
c2 = complex(input("Digite o segundo complexo no formato a+bj: "))

# Realizar testes de propriedades
print("\nTeste A:")
print(c1.conjugate() + c2.conjugate() == (c1 + c2).conjugate())

print("\nTeste B:")
print(c1.conjugate() * c2.conjugate() == (c1 * c2).conjugate())
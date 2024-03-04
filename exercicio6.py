# Solicitar ao usuário dois números complexos no formato a+bj
str1 = input("Digite o primeiro complexo no formato a+bj: ")
str2 = input("Digite o segundo complexo no formato a+bj: ")

# Converter as strings para números complexos
c1 = complex(str1)
c2 = complex(str2)

# Realizar testes de propriedades
print("\nTeste A:")
print(abs(c1) * abs(c2) == abs(c1 * c2))

print("\nTeste B:")
print(abs(c1 + c2) <= abs(c1) + abs(c2))

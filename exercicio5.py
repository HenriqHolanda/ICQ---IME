# Solicitar ao usuário três números complexos no formato a+bj
str1 = input("Digite o primeiro complexo no formato a+bj: ")
str2 = input("Digite o segundo complexo no formato a+bj: ")
str3 = input("Digite o terceiro complexo no formato a+bj: ")

# Converter as strings para números complexos
c1 = complex(str1)
c2 = complex(str2)
c3 = complex(str3)

# Realizar testes de propriedades
print("\nTeste da Comutatividade na Soma:")
print(c1 + c2 == c2 + c1)

print("\nTeste da Comutatividade no Produto:")
print(c1 * c2 == c2 * c1)

print("\nTeste da Associatividade na Soma:")
print((c1 + c2) + c3 == c1 + (c2 + c3))

print("\nTeste da Associatividade no Produto:")
print((c1 * c2) * c3 == c1 * (c2 * c3))

print("\nTeste da Distributividade:")
print(c1 * (c2 + c3) == (c1 * c2) + (c1 * c3))

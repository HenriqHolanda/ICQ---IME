# Solicitar ao usuário três números complexos no formato a+bj
n1 = input("Insira o primeiro numero na forma a+bj: ")
n2 = input("Insira o segundo complexo na forma a+bj: ")
n3 = input("Insira o terceiro complexo na forma a+bj: ")

#Como o input é do tipo string, temos que converter para número complexo que é o nosso interesse
z1 = complex(n1)
z2 = complex(n2)
z3 = complex(n3)


print("\nTeste Comutatividade na Soma:")
ver1 = (z1 + z2 == z2 + z1) #Variável booleana
print(ver1)

print("\nTeste Comutatividade no Produto:")
ver2 = (z1 * z2 == z2 * z1) #Variável booleana
print(ver2)

print("\nTeste Associatividade na Soma:")
ver3 = ((z1 + z2) + z3 == z1 + (z2 + z3)) #Variável booleana
print(ver3)

print("\nTeste Associatividade no Produto:")
ver4 = ((z1 * z2) * z3 == z1 * (z2 * z3)) #Variável booleana
print(ver4)

print("\nTeste Distributividade:")
ver5 = (z1 * (z2 + z3) == (z1 * z2) + (z1 * z3)) #Variável booleana
print(ver5)
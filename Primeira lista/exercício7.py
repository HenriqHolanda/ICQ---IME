n1 = input("Insira o primeiro numero na forma a+bj: ")
n2 = input("Insira o segundo complexo na forma a+bj: ") 

z1 = complex(n1)
z2 = complex(n2)

#para conseguir o conjugado podemos utilizar o conjugate()

print("\nteste 1:")
ver1 = ((z1.conjugate() + z2.conjugate()) == (z1 + z2).conjugate() )
print(ver1)

print("\nteste2")
ver2 = (z1.conjugate() * z2.conjugate() == (z1 * z2).conjugate())
print(ver2)
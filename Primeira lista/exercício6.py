n1 = input("Insira o primeiro numero na forma a+bj: ")
n2 = input("Insira o segundo complexo na forma a+bj: ") 

z1 = complex(n1)
z2 = complex(n2)

#Para conseguir o valor absoluto em python podemos utilizar abs()

print("\nteste 1:")
ver1 = (abs(z1)*abs(z2) == (abs(z1*z2)))
print(ver1)

print("\nteste2")
ver2 = (abs(z1 + z2) <= abs(z1) + abs(z2))
print(ver2)
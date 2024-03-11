#Note que ad - bc no caso do enunciado é diferente de 0, logo podemos fazer a transformada de moebius

def R(x):
    return 1 / x

n1 = input("Insira o numero na forma a+bj: ")

z1=complex(n1)

print(f"{R(z1)}")
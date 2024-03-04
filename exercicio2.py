potencia_escolhida = int(input("Escolha a potência de i a ser calculada: "))

resultado_mod_4 = potencia_escolhida % 4

if resultado_mod_4 == 0:
    print("O resultado da potência é 1")
elif resultado_mod_4 == 1:
    print("O resultado da potência é i")
elif resultado_mod_4 == 2:
    print("O resultado da potência é -1")
else:
    print("O resultado da potência é -i")

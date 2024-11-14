def Numero_Primo(nro):
    while nro >= 2:
        if nro == 2 or nro == 3:
            print(f"{nro} é primo!")
        elif nro % 2 == 0:
            print(f"{nro} não é primo!")
        elif nro % 2 != 0 and nro % 3 != 0 and not nro % 5 == 0:
            print(f"{nro} é primo!")
        else:
            print(f"{nro} não é primo")
        nro -= 1

nro = int(input("Digite um número: "))
Numero_Primo(nro)

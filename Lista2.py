def Calculadora(nro1, nro2, operador):
    if operador == "+":
        return print(f"A soma é de {nro1 + nro2}")
    elif operador == "-":
        return print(f"A subtração é de {nro1 - nro2}")
    elif operador == "*":
        return print(f"A multiplicação é de {nro1 * nro2}")
    elif operador == "/":
        return print(f"A divisão é de {nro1 / nro2}")
    else:
        return print("Operador não identificado!")
nro1 = int(input("Digite um número: "))
nro2 = int(input("Digite outro número: "))
operador = input("Digite o operador(+, -, *, /): ")
Calculadora(nro1, nro2, operador)
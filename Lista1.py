def IMC(peso, altura):
    resultado = peso /(altura ** 2)
    return print(f"Seu IMC é {resultado}")
peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC(peso, altura)
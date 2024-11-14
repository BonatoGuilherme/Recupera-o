clientes_A = ["Ana", "Bruno", "Carla", "Diego", "Elisa"]
clientes_B = ["Ana", "Bruno", "Carla", "Felipe", "Laura"]

Ambos = set(clientes_A) & set(clientes_B)
print(f"Clientes que estao em ambos conjuntos: {Ambos}")
ApenasA = set(clientes_A) - set(clientes_B)
print(f"Clientes que estão apenas em clientes_A: {ApenasA}")
Apenas_Um_conjunto = set(clientes_A) ^ set(clientes_B)
print(f"Clientes que estão em apenas um dos conjuntos: {Apenas_Um_conjunto}")

tamanho_AUC = len(Apenas_Um_conjunto)
tamanho_AB = len(clientes_A + clientes_B)
porcentagem = (tamanho_AUC / tamanho_AB) * 100
print(f"A porcentagem de clientes únicos: {porcentagem}%")
q_notas = int(input("Digite quantas notas são:"))
resp=0
som_pesos=0
for i in range (q_notas):
    nota=float(input(f"Digite a {i+1}ª nota: "))
    pesos=float(input(f"Digite o {i+1}º peso: "))
    som_pesos = som_pesos + pesos
    mult = nota*pesos
    resp = resp + mult
print(resp/som_pesos)



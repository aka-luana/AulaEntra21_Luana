notas = []

for i in range(3):
    notas.append(float(input("Entre com a nota: ")))

print(f"A média é {sum(notas)/3:.2f}")
entrada1 = input().split()
entrada2 = input().split()
x1, y1 = entrada1
x2, y2 = entrada2
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)
distancia = (((x2 - x1)**2) + ((y2 - y1)**2)) ** 0.5
print(f"{distancia:.4f}")
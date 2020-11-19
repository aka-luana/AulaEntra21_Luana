a, b, c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

if ((a < b + c) and (b < a + c) and (c < a + b)):
    print(f"Perimetro = {a + b + c:.1f}")
else:
    print(f"Area = {((a + b) * c) / 2:.1f}")

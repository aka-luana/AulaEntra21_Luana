entrada = input().split()
a, b, c = entrada
a = int(a)
b = int(b)
c = int(c)
maiorAB = ((a + b + abs(a - b)) / 2)
final = ((maiorAB + c + abs(maiorAB - c)) / 2)
print(f"{int(final)} eh o maior")
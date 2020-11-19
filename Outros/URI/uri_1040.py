n1, n2, n3, n4 = input().split(" ")

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media1 = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print(f"Media: {media1:.1f}")
if   (media1 >= 7):
    print("Aluno aprovado.")
elif (media1 >= 5 and media1 <= 6.9):
    print("Aluno em exame.")
    nExame = float(input())
    print(f"Nota do exame: {nExame:.1f}")
    if ((media1 + nExame) / 2 >= 5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {((media1 + nExame) / 2):.1f}")
else:
    print("Aluno reprovado.")


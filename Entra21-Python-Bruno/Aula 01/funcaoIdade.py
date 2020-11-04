def devolveIdade(ano):
    return(2020 - ano)

ano = int(input("Qual o seu ano de nascimento? "))
print(f"Você tem {devolveIdade(ano)} anos")
idade = int(input())

resto = idade
ano   = int(resto / 365)
resto = resto - (ano * 365)
mes   = int(resto / 30)
resto = resto - (mes * 30)

print(f"""{ano} ano(s)
{mes} mes(es)
{int(resto)} dia(s)""")
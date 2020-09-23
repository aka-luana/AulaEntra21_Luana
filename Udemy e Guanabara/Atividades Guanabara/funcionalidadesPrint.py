print("Eu não quero que quebre a linha", end = " ")
print("bua bua bua")
# end = " " junta os prints

num = 3.989595441516
print("Que o {} só com 2 números após o ponto.".format(num), end = " ")
print("{:.2f}".format(num))
# {:.Nf} limita as casas decimais. atenção: ele arredeonda!

nome = input("Qual o seu nome? ")
print("Prazer em te conhecer {:#^10}!".format(nome))
# {:N} -> {:6}: separa quantas casas for necessárias
# {:>N} -> {:>6}: faz o alinhamento a direita (>)
# {:<N} -> {:<6}: faz o alinhamento a esquerda (<)
# {:^N} -> {:^6}: faz o ficar centralizado (^)
# {:sinal^N} -> {:#^6}: adiciona o sinal na frase
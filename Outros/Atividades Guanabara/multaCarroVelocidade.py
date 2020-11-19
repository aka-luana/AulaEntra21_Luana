velocidade = int(input("Qual a velocidade do carro? "))

if (velocidade > 80):
    velocidade = (velocidade - 80) * 7
    print(f"VOCÊ SERÁ MULTADO! O VALOR SERÁ DE R${velocidade:.2f}")
else:
    print("DENTRO DO PERMITIDO!")
largura = float(input("Qual a largura da parede? "))
altura  = float(input("Qual a altura da parede? "))

print("Sua parede tem a dimensão de {}X{} e sua área é de {:.2f}m².".format(largura, altura, largura * altura))
print("Para pintar essa parede, você precisará de {:.2f}l de tinta.".format((largura * altura)/2))
dias = float(input("Usou qunatos dias? ")) 
km   = float(input("Rodou quantos km? "))

print("O total a ser pago é de R${:.2f}".format((60*dias)+(km*0.15)))
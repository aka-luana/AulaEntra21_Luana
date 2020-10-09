# list comprehension

x = [1, 2, 3, 4, 5]
y = [i ** 2 for i in x] # Valor a adicionar + laço + condição
z = [i for i in x if i%2 == 1] # Só os impares

#Mesma coisa que fazer:
#for i in x:
#    y.append(i ** 2)

#for i in x:
#    if i%2 == 1:
#        z.append(i)

print(x)
print(y)
print(z)
#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

dictPessoa = {}

nome      = input("Digite o nome do funcionário: ")
sobrenome = input("Digite o sobrenome do funcionário: ")
cpf       = int(input("Digite o cpf do funcionário: "))
salario   = float(input("Digite o salário do funcionário: R$ "))

dictPessoa = {'nome':nome, 'sobrenome': sobrenome, 'cpf': cpf, 'salario': salario}

for chave in dictPessoa:
    print(chave, '-', dictPessoa[chave])
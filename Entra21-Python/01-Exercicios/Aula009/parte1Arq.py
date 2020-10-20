def cadastroPessoa():
    nome = input("Digite o nome: ")
    if(nome.isspace() or nome == ''):
        while(nome.isspace() or nome == ''):
            nome = input("Nome em branco. Digite novamente: ")

    sobrenome = input("Digite o sobrenome: ")
    if(sobrenome.isspace() or sobrenome == ''):
        while(sobrenome.isspace() or sobrenome == ''):
            sobrenome = input("Sobrenome em branco. Digite novamente: ")

    idade = input("Digite a idade: ")
    if(idade.isspace() or idade == ''):
        while(idade.isspace() or idade == ''):
            idade = input("Idade em branco. Digite novamente: ")
    idade = int(idade)

    if (idade >= 18):
        dictPessoa = {'Nome':nome, 'Sobrenome':sobrenome, 'Idade':idade}
        arquivoPessoas = open('pessoas.txt', 'a')
        arquivoPessoas.write(f"{dictPessoa['Nome']};{dictPessoa['Sobrenome']};{dictPessoa['Idade']};")
        arquivoPessoas.close()
        
        arqPessoas = open('pessoas.txt', 'r')
        numeroCadastro = 0
        for contador in arqPessoas:
            numeroCadastro = numeroCadastro + 1
        arqPessoas.close()

        dictPessoa = {'ID':numeroCadastro}
        arquivoPessoas = open('pessoas.txt', 'a')
        arquivoPessoas.write(f"{dictPessoa['ID']} \n")
        print(f"Cadastrado com sucesso! Seu é é {numeroCadastro}")
    else:
        print("Não é possivel cadastrar menores de 18 anos")
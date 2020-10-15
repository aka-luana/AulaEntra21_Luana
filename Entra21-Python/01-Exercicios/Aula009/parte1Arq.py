def cadastroPessoa():
    nome = input("Digite o nome: ")
    if(nome.isspace()):
        while(nome.isspace()):
            nome = input("Nome em branco. Digite novamente: ")

    sobrenome = input("Digite o sobrenome: ")
    if(sobrenome.isspace()):
        while(sobrenome.isspace()):
            sobrenome = input("Sobrenome em branco. Digite novamente: ")

    idade = input("Digite a idade: ")
    if(idade.isspace()):
        while(idade.isspace()):
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
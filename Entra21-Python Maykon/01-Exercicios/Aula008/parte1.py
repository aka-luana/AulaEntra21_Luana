listaPessoa   = []

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
        listaPessoa.append({'Nome':nome, 'Sobrenome':sobrenome, 'Idade':idade})
        print(f"Cadastrado com sucesso!")
    else:
        print("Não é possivel cadastrar menores de 18 anos")
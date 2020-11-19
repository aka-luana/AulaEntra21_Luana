#--- Exercício 2  - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

UM     = 1
DOIS   = 2
TRES   = 3
QUATRO = 4
CINCO  = 5

escolhaUser = None

while(escolhaUser != 5):
    print("""
    ***** CADASTRO FUNCIONÁRIOS *****



    {}. Cadastrar funcionário"
    {}. Listar funcionários"
    {}. Editar funcionário"
    {}. Deletar funcionário"
    {}. Sair
    
    
    
    *********************************""".format(UM, DOIS, TRES, QUATRO, CINCO))
    
    escolhaUser = int(input("    Digite a opção desejada: "))

    if escolhaUser == UM:
        print("    Foi escolhida a opção '1' -> Cadastrar funcionário.")
    elif escolhaUser == DOIS:
        print("    Foi escolhida a opção '2' -> Listar funcionários.")
    elif escolhaUser == TRES:
        print("    Foi escolhida a opção '3' -> Editar funcionário.")
    elif escolhaUser == QUATRO:
        print("    Foi escolhida a opção '4' -> Deletar funcionário.")
    elif(escolhaUser == CINCO):
        print("    Foi escolhida a opção '5' -> Sair.")
    else:
        print("    Opção inválida.")


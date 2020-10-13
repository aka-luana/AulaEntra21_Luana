from E01 import cadastroPessoa
import E02

def main():
        print("""
1) Cadastrar Pessoa
2) Cadastrar endereço
3) Listar Pessoas cadastradas
4) Listar Endereços cadastrados
5) Sair
""")

main()
entradaUser = int(input())
while(entradaUser != 5):
    main()
    if (entradaUser == 1):
        cadastroPessoa()
    elif (entradaUser == 2):
        cadastroEndereco()
    elif (entradaUser == 3):
        listarPessoas()
    elif (entradaUser == 4):
        listarEnderecos()
    else:
        print ("Opção inválida.")
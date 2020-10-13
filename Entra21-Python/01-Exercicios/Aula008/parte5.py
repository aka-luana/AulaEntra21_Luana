import parte1
import parte2
import parte3
import parte4

def main():
    print("-" * 45)
    print("""
        1) Cadastrar Pessoa
        2) Cadastrar endereço
        3) Listar Pessoas cadastradas
        4) Listar Endereços cadastrados
        5) Sair
    """)
    print("-" * 45)
    entradaUser = int(input("Digite a opção desejada: "))
    if (entradaUser == 1):
        parte1.cadastroPessoa()
    elif (entradaUser == 2):
        parte2.cadastroEndereco()
    elif (entradaUser == 3):
        parte3.listarPessoas()
    elif (entradaUser == 4):
        parte4.listarEnderecos()
    elif (entradaUser == 5):
        print("Até a próxima.")
        entradaUser = 5
    else:
        print("Opção inválida")
    while(entradaUser != 5):
        main()

main()
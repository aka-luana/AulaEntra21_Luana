import parte1Arq
import parte2Arq
import parte3Arq
import parte4Arq

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
        parte1Arq.cadastroPessoa()
    elif (entradaUser == 2):
        parte2Arq.cadastroEndereco()
    elif (entradaUser == 3):
        parte3Arq.listarPessoas()
    elif (entradaUser == 4):
        parte4Arq.listarEnderecos()
    elif (entradaUser == 5):
        print("Até a próxima.")
        entradaUser = 5
    else:
        print("Opção inválida")
    while(entradaUser != 5):
        main()

main()
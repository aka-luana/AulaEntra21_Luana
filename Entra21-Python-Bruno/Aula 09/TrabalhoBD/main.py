import bancoCliente
from pessoas import pessoa
from veiculos import veiculo

if __name__ == "__main__":
    while True:
        valor = int(input(
            """
            ********************
                    MENU
            ********************
            1 - Cadastrar cliente e carro
            2 - Visualizar cadastro
            3 - Editar cadastro
            4 - Excluir cadastro
            0 - Sair
            Digite a operação desejada: """))

        if (valor == 1):
            criaTabelaPessoa()
            criaTabelaVeiculos()
            insereDadosPessoas(pessoa)
            insereDadosVeiculos(veiculo)
        elif (valor == 2):
            dataSaver.cadastroConta()
        elif (valor == 3):
            banco.mostraSaldo()
        elif (valor == 4):
            banco.deposito()
        elif (valor == 5):
            banco.procurarPessoa()
        elif(valor == 0):
            print("Agradecemos a sua visita!")
            break
        else:
            print("Opção inválida.")
import bancoCliente
import pessoas
import veiculos

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
            bancoCliente.criaTabelaPessoa()
            bancoCliente.criaTabelaVeiculos()
            p = pessoas.infoPessoa(pessoas.Pessoa)
            bancoCliente.insereDadosPessoas(p)
            v = veiculos.infoVeiculo(veiculos.Veiculo)
            bancoCliente.insereDadosVeiculos(v)
            bancoCliente.criaTabelaPessoaVeiculo()
            bancoCliente.insereDadosPessoaVeiculo()
        elif (valor == 2):
            bancoCliente.visualizarCadastro()
        elif (valor == 3):
            pass
        elif (valor == 4):
            pass
        elif(valor == 0):
            print("Agradecemos a sua visita!")
            break
        else:
            print("Opção inválida. Tente novamente.")
import bancoCliente
import pessoas
import veiculos

if __name__ == "__main__":
    while True:
        valor = input(
            """
            ********************
                    MENU
            ********************
            1 - Cadastrar cliente e carro
            2 - Visualizar cadastro
            3 - Editar cadastro
            4 - Excluir cadastro
            0 - Sair
            Digite a operação desejada: """)

        if (valor == "1"):
            bancoCliente.criaTabelaPessoa()
            bancoCliente.criaTabelaVeiculos()
            p = pessoas.infoPessoa(pessoas.Pessoa)
            bancoCliente.insereDadosPessoas(p)
            v = veiculos.infoVeiculo(veiculos.Veiculo)
            bancoCliente.insereDadosVeiculos(v)
        elif (valor == "2"):
            bancoCliente.visualizarCadastro()
        elif (valor == "3"):
            bancoCliente.editarCadastro()
        elif (valor == "4"):
            bancoCliente.excluirCadastro()
        elif(valor == "0"):
            print("            Agradecemos a sua visita!")
            break
        else:
            try:
                int(valor)
                print("            Opção inválida. Digite somente as opções do menu.")
            except:
                print("            Opção inválida. Somente números.")
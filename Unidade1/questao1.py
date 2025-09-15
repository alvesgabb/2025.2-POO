""" Crie um programa que simule um sistema de gerenciamento de estoque de uma loja. O programa deve permitir:

Adicionar um novo produto ao estoque (nome e quantidade).

Remover um produto pelo nome.

Atualizar a quantidade de um produto existente.

Exibir todos os produtos no estoque.

Dica: Utilize um loop para permitir que o usuário faça várias operações até escolher sair. """

import funcoes1

def menu():
    while True:
        print("\n===== MENU ESTOQUE =====")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Atualizar quantidade")
        print("4 - Exibir estoque")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            funcoes1.adicionar_produto()
        elif opcao == "2":
            funcoes1.remover_produto()
        elif opcao == "3":
            funcoes1.atualizar_quantidade()
        elif opcao == "4":
            funcoes1.exibir_estoque()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")


menu()

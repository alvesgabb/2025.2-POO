""" Crie um programa que gerencie uma lista de tarefas. Cada tarefa deve ser representada por um dicionário contendo:
Título da tarefa
Descrição
Status (Pendente ou Concluído)
O programa deve permitir:
Adicionar uma nova tarefa.
Marcar uma tarefa como concluída.
Listar todas as tarefas, separando as concluídas das pendentes.
Dica: Armazene as tarefas em uma lista de dicionários e percorra a lista para exibição. """

import funcoes3
def menu():
    while True:
        print("\n===== MENU DE TAREFAS =====")
        print("1 - Adicionar tarefa")
        print("2 - Concluir tarefa")
        print("3 - Listar tarefas")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            funcoes3.adicionar_tarefa()
        elif opcao == "2":
            funcoes3.concluir_tarefa()
        elif opcao == "3":
            funcoes3.listar_tarefas()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
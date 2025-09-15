""" Crie um programa que permita cadastrar alunos e suas quatro notas (N1,N2,N3,N4) em um dicionário. O programa deve permitir:

Adicionar um aluno e suas quatro notas.
Atualizar as notas de um aluno existente.
Remover um aluno do cadastro.

Exibir todos os alunos e suas notas.
Calcular e exibir a média das notas de cada aluno.

Dica: Utilize um dicionário, onde a chave seja o nome do aluno e o valor seja uma lista com as quatro notas.
Para testes iniciais, podem usar o dicionário abaixo:
alunos = {

    "Ana": [8.5, 7.0, 9.2, 6.8],

    "Julia": [5.5, 6.0, 7.5, 8.0],

    "Carla": [9.0, 8.5, 10.0, 9.8],

    "Kaio": [6.5, 7.2, 5.8, 6.9],

    "Beatriz": [7.8, 8.2, 7.0, 8.5]

} """
import funcoes2

def menu():
    while True:
        print("\n1 - Adicionar aluno")
        print("2 - Atualizar notas")
        print("3 - Remover aluno")
        print("4 - Exibir alunos e notas")
        print("5 - Exibir médias")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            funcoes2.adicionar_aluno()
        elif opcao == "2":
           funcoes2.atualizar_notas()
        elif opcao == "3":
           funcoes2.remover_aluno()
        elif opcao == "4":
            funcoes2.exibir_alunos()
        elif opcao == "5":
            funcoes2.exibir_medias()
        elif opcao == "6":
            break
        else:
            print("Opção inválida.")

menu()
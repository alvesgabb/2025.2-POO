
alunos = {
    "Paula": [8.5, 7.0, 9.2, 6.8],
    "Julia": [5.5, 6.0, 7.5, 8.0],
    "Gal": [9.0, 8.5, 10.0, 9.8],
    "Lucas": [6.5, 7.2, 5.8, 6.9],
    "Kaio": [7.8, 8.2, 7.0, 8.5]
}


def adicionar_aluno():
    nome = input("Nome do aluno: ")
    notas = []
    for i in range(1,5):
        nota = float(input(f"Nota N{i}: "))
        notas.append(nota)
    alunos[nome] = notas
    print(f"Aluno {nome} adicionado!")


def atualizar_notas():
    nome = input("Nome do aluno a atualizar: ")
    if nome in alunos:
        notas = []
        for i in range(1,5):
            nota = float(input(f"Nova nota N{i}: "))
            notas.append(nota)
        alunos[nome] = notas
        print(f"Notas do aluno {nome} atualizadas!")
    else:
        print("Aluno não encontrado.")


def remover_aluno():
    nome = input("Nome do aluno a remover: ")
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno {nome} removido!")
    else:
        print("Aluno não encontrado.")


def exibir_alunos():
    for nome, notas in alunos.items():
        print(f"{nome}: {notas}")


def exibir_medias():
    for nome, notas in alunos.items():
        media = sum(notas)/len(notas)
        print(f"{nome}: {media:.2f}")

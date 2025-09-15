
tarefas = []

def adicionar_tarefa():
    titulo = input("Digite o título da tarefa: ").strip()
    descricao = input("Digite a descrição da tarefa: ").strip()
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente"
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")


def concluir_tarefa():
    if not tarefas:
        print("Não há tarefas cadastradas.")
        return
    print("\nTarefas pendentes:")
    for i, tarefa in enumerate(tarefas):
        if tarefa["status"] == "Pendente":
            print(f"{i+1} - {tarefa['titulo']}")
    opcao = input("Digite o número da tarefa que deseja concluir: ")
    if opcao.isdigit():
        indice = int(opcao) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["status"] = "Concluído"
            print(f"Tarefa '{tarefas[indice]['titulo']}' marcada como concluída!")
        else:
            print("Número inválido.")
    else:
        print("Digite um número válido.")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n--- Tarefas Pendentes ---")
    for tarefa in tarefas:
        if tarefa["status"] == "Pendente":
            print(f"Título: {tarefa['titulo']}\nDescrição: {tarefa['descricao']}\n")
    
    print("--- Tarefas Concluídas ---")
    for tarefa in tarefas:
        if tarefa["status"] == "Concluído":
            print(f"Título: {tarefa['titulo']}\nDescrição: {tarefa['descricao']}\n")
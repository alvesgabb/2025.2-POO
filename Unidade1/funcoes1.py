estoque = {}

def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip()
    if nome == "":
        print("Nome inválido.")
        return

    if nome in estoque:
        print("Produto já existe no estoque!")
    else:
        quantidade = input("Digite a quantidade: ")
        if quantidade.isdigit():   # verifica se o valor digitado é número
            estoque[nome] = int(quantidade)
            print(f"Produto '{nome}' adicionado com sucesso!")
        else:
            print("Erro: Digite apenas números para a quantidade.")

def remover_produto():
    nome = input("Digite o nome do produto a remover: ").strip()
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido do estoque.")
    else:
        print("Produto não encontrado.")

def atualizar_quantidade():
    nome = input("Digite o nome do produto a atualizar: ").strip()
    if nome in estoque:
        quantidade = input("Digite a nova quantidade: ")
        if quantidade.isdigit():
            estoque[nome] = int(quantidade)
            print(f"Quantidade do produto '{nome}' atualizada para {quantidade}.")
        else:
            print("Erro: Digite apenas números para a quantidade.")
    else:
        print("Produto não encontrado.")

def exibir_estoque():
    if not estoque:
        print("Estoque vazio.")
    else:
        print("\n--- Estoque Atual ---")
        for nome, quantidade in estoque.items():
            print(f"{nome}: {quantidade}")
        print("----------------------")
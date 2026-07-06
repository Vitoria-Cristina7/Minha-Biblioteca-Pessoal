from datetime import datetime

livros = []

# RF01 - Cadastrar Livros
def cadastrar_livro():
    titulo = input("Digite o título: ")
    autor = input("Digite o autor: ")
    genero = input("Digite o gênero: ")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "status": "Quero Ler",
        "emprestado": False,
        "amigo": "",
        "data": ""
    }

    livros.append(livro)
    print("Livro cadastrado.")

# RF02 - Listar e filtrar livros
def listar_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return
    
    print("\n1 - Listar todos")
    print("2 - Filtrar por status")
    print("3 - Filtrar por autor")
    print("4 - Filtrar por gênero")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        for livro in livros:
            print()
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Gênero:", livro["genero"])
            print("Status:", livro["status"])
            print("Emprestado:", livro["emprestado"])

    elif opcao == "2":
        status = input("Digite o status: ")

        for livro in livros:
            if livro["status"] == status:
                print()
                print("Título:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Gênero:", livro["genero"])
                print("Status:", livro["status"])

    elif opcao == "3":
        autor = input("Digite o autor: ")

        for livro in livros:
            if livro["autor"] == autor:
                print()
                print("Título:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Gênero:", livro["genero"])
                print("Status:", livro["status"])

    elif opcao == "4":
        genero = input("Digite o gênero: ")

        for livro in livros:
            if livro["genero"] == genero:
                print()
                print("Título:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Gênero:", livro["genero"])
                print("Status:", livro["status"])

    else:
        print("Opção inválida.")

# RF03 - Atualizar status
def atualizar_status():
    titulo = input("Digite o título do livro: ")

    for livro in livros:
        if livro["titulo"] == titulo:

            print("1 - Quero Ler")
            print("2 - Lendo")
            print("3 - Lido")

            opcao = input("Escolha o novo status: ")

            if opcao == "1":
                livro["status"] = "Quero Ler"
            elif opcao == "2":
                livro["status"] = "Lendo"
            elif opcao == "3":
                livro["status"] = "Lido"
            else:
                print("Opção inválida.")
                return

            print("Status atualizado.")
            return

    print("Livro não encontrado.")

# RF04 - Registrar empréstimo
def emprestar_livro():
    titulo = input("Digite o título do livro: ")

    for livro in livros:
        if livro["titulo"] == titulo:

            if livro["emprestado"] == True:
                print("Livro já está emprestado.")
                return

            amigo = input("Nome do amigo: ")
            data = input("Data para devolução (dd/mm/aaaa): ")

            livro["emprestado"] = True
            livro["amigo"] = amigo
            livro["data"] = data

            print("Empréstimo registrado.")
            return

    print("Livro não encontrado.")

# RF05 - Registrar devolução
def devolver_livro():
    titulo = input("Digite o título do livro: ")

    for livro in livros:
        if livro["titulo"] == titulo:

            if livro["emprestado"] == False:
                print("Esse livro não está emprestado.")
                return

            hoje = datetime.now()
            data_devolucao = datetime.strptime(livro["data"], "%d/%m/%Y")

            if hoje > data_devolucao:
                print("Livro devolvido com atraso.")
            else:
                print("Livro devolvido no prazo.")

            livro["emprestado"] = False
            livro["amigo"] = ""
            livro["data"] = ""

            return

    print("Livro não encontrado.")
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

  


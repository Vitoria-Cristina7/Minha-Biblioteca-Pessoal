from datetime import datetime

livros = []

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
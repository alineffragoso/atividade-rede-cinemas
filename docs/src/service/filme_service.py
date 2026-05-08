from src.repository.filme_repository import FilmeRepository


class FilmeService:

    def __init__(self):

        self.repository = FilmeRepository()

    def cadastrar(self, filme):

        if filme.titulo == "":

            print("Título inválido")
            return

        self.repository.salvar(filme)

        print("Filme cadastrado")

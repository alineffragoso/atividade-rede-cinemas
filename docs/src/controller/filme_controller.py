from src.model.filme import Filme
from src.service.filme_service import FilmeService


class FilmeController:

    def __init__(self):

        self.service = FilmeService()

    def cadastrar_filme(self):

        filme = Filme(
            "Vingadores",
            180,
            "Ação"
        )

        self.service.cadastrar(filme)

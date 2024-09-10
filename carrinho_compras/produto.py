class Produto:

    def __init__(self, nome: str, preco: float = 0):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self) -> str:
        return self.nome

    @property
    def preco(self) -> float:
        return self.preco

    @nome.setter
    def nome(self, novo_nome) -> None:
        self.nome = novo_nome

    @preco.setter
    def preco(self, novo_preco) -> None:
        self.preco = novo_preco

    def __str__(self) -> str:
        produto_impresso = f"""
            {self.nome = }
            {self.preco = }
        """
        return produto_impresso

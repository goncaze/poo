class Produto:

    def __init__(self, nome: str, preco: float = 0):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def preco(self) -> float:
        return self._preco

    @nome.setter
    def nome(self, novo_nome) -> None:
        self._nome = novo_nome

    @preco.setter
    def preco(self, novo_preco) -> None:
        self._preco = novo_preco

    def __str__(self) -> str:
        produto_impresso = f"""
            {self._nome = }
            {self._preco = }
        """
        return produto_impresso

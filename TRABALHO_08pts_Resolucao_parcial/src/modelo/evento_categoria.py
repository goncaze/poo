class EventoCategoria:

    def __init__(self, id: int = 0, categoria: str = "", descricao: str = "") -> None:
        self._id: int = id
        self._categoria: str = categoria
        self._descricao: str = descricao

    @property
    def categoria(self) -> int:
        return self._categoria

    @categoria.setter
    def categoria(self, nova_categoria: str) -> None:
        self._categoria = nova_categoria

    @property
    def descricao(self) -> int:
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao: str) -> None:
        self._descricao = nova_descricao

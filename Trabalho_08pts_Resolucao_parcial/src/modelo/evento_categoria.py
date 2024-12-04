class EventoCategoria:

    auto_incrementar = 0

    def __init__(self, categoria: str = "", descricao: str = "") -> None:
        EventoCategoria.auto_incrementar += 1
        self._id: int = EventoCategoria.auto_incrementar
        self._categoria: str = categoria
        self._descricao: str = descricao

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, novo_id: str) -> None:
        self._id = novo_id

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

    def __str__(self) -> str:
        return f"\tid: {self.id}\tCategoria: {self.categoria}\tDescricao: { self.descricao}"

from src.modelo.data_categoria import DataCategoria


class Data:

    auto_incrementar = 0

    def __init__(self, data: str = "", data_categoria: DataCategoria = None):
        Data.auto_incrementar += 1
        self._id: int = Data.auto_incrementar
        self._data: str = data
        self._data_categoria: DataCategoria = data_categoria


    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, nova_id: str) -> None:
        self._id = nova_id

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, nova_data: str) -> None:
        self._data = nova_data

    @property
    def data_categoria(self) -> int:
        return self._data_categoria

    @data_categoria.setter
    def data_categoria(self, nova_data_categoria: int) -> None:
        self._data_categoria = nova_data_categoria

    def __str__(self):
        return f"""
        {self._id}\t{self._data}\t{self._data_categoria.categoria}
    """

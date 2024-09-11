class Pedido:
    def __init__(self, data: str, valor_total: float) -> None:
        self._data = data
        self._valor_total = valor_total
        self._itens_pedidos = "??????"

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, nova_data) -> str:
        self._data = nova_data

    def __str__(self) -> str:
        return f"""
            {self._data = }
            {self._valor_total = }
        """

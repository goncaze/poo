class DataCategoria:

  auto_incrementar = 0

  def __init__(self, categoria: str = "", descricao: str="")->None:
    DataCategoria.auto_incrementar += 1
    self._id: int = DataCategoria.auto_incrementar
    self._categoria: str = categoria
    self._descricao: str = descricao

  @property
  def id(self)->int:
    return self._id

  @property
  def categoria(self)->int:
    return self._categoria

  @categoria.setter
  def categoria(self, nova_categoria:str)->None:
    self._categoria = nova_categoria

  @property
  def descricao(self)->int:
    return self._descricao

  @descricao.setter
  def descricao(self, nova_descricao:str)->None:
    self._descricao = nova_descricao

  def __str__(self)->str:
    return f"""
      {self.id = }
      {self.categoria = }
      {self.descricao = }
    """


# Testando a classe
if __name__ == "__main__":
  d = DataCategoria(categoria='Cat', descricao='desc')
  print(d)
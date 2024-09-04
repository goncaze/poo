class Produto:

    def __init__(self, nome:str, preco:float) -> None:
        """ 
            Classe que representa mercadorias \n
            \t 1. nome -> nome do produto (str)
            \t 2. preco -> valor do produto (float) \n

            Ex.: obj_produto = Produto('titulo', 1.99)
        """     
        self._nome = nome
        self._preco = preco


    def __str__(self) -> str:
        mensagem = f"""
            {self.nome = }
            {self.preco = }
        """
        return mensagem

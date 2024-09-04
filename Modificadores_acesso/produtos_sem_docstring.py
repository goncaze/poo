class Produto1:

    def __init__(self, nome:str, preco:float) -> None:   
        self._nome = nome
        self._preco = preco        

    def __str__(self) -> str:
        mensagem = f"""
            {self.nome = }
            {self.preco = }
        """
        return mensagem

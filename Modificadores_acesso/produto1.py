class Produto1:

    def __init__(self, nome:str, preco:float) -> None:   
        self.nome = nome
        self.preco = preco        

    def __str__(self) -> str:
        mensagem = f"""
            OBSERVAÇÃO: sem docstring! \n
            {self.nome = }
            {self.preco = }
        """
        return mensagem

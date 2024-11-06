import os
from src.controller.data_categoria_controller import DataCategoriaController
from src.controller.data_controller import DataController

data_cat_ctlr = DataCategoriaController()
data_ctlr = DataController()

menu_p = """
    ----------------------------------------------
    Menu principal de operações
    ----------------------------------------------
    [1] – Operações com categorias de data
    [2] - Operações com datas
    [3] - Operações com categorias de evento
    [4] - Operações com categorias de evento_data
    [0] – Encerrar aplicativo
  """


def menu_principal(menu_p: str) -> None:

    while True:
        # Limpar a tela
        os.system("cls")

        print(menu_p)
        print()  # Linha vazia
        selecao = input("Opção: ")

        match selecao:
            case "0":  # [0] – Encerrar aplicativo
                break
            case "1":  # [1] – Operações com categorias de data
                data_cat_ctlr.menu_data_categoria()
            case "2":  # [2] - Operações com datas
                data_ctlr.menu_data()
            case "3":  # [3] - Operações com categorias de evento
                pass
            case "4":  # [4] - Operações com categorias de evento_data
                pass


if __name__ == "__main__":
    menu_principal(menu_p)

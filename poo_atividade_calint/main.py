from os import system
# from modelo.data_categoria import DataCategoria
from operacoes import operacao_data_categoria as odc


# menu_principal = """
#     ----------------------------------------------
#     Menu principal de operações
#     ----------------------------------------------
#     [1] - Operações com categorias de data
#     [2] - Operações com datas
#     [3] - Operações com categorias de evento
#     [4] - Operações com categorias de evento_data
#     [0] - Encerrar aplicativo
#   """

def principal():
    menu_principal = """
        ----------------------------------------------
        Menu principal de operações
        ----------------------------------------------
        [1] - Operações com categorias de data
        [2] - Operações com datas
        [3] - Operações com categorias de evento
        [4] - Operações com categorias de evento_data
        [0] - Encerrar aplicativo
      """

    while(True):
        # Limpar a tela
        system("cls")
        

        print(menu_principal)
        print() # Linha vazia
        selecao = input("Opção: ")

        match selecao:
          case '0': # [0] – Encerrar aplicativo
            break
          case '1': # [1] – Operações com categorias de data
            odc.menu_data_categoria()
          case '2': # [2] - Operações com datas
            pass
          case '3': # [3] - Operações com categorias de evento
            pass
          case '4': # [4] - Operações com categorias de evento_data
            pass
          

if __name__ == "__main__":
    principal()
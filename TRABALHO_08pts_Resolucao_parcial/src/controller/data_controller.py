import os
from src.modelo.data_categoria import DataCategoria
from src.modelo.data import Data
from src.data import data_db
from src.controller.data_categoria_controller import DataCategoriaController


class DataController:
    def __init__(self):
        self.lista_data = data_db.lista_data
        self.data_cat_ctrl = DataCategoriaController()

    def ver_datas(self) -> None:
        print("\t_____________________________________________")
        print("\t LISTA DE DATAS CADASTRADAS")
        cabecalho = """
        ----------------------------------------------
        Id\tData\t\tCategoria
        ----------------------------------------------
        """
        print(cabecalho)
        for data in self.lista_data:
            print(data)

    def validar_menu_str(self, menu: str) -> str:

        while True:

            print(menu)

            opcao = input("\n Selecione: ")

            if opcao == "1" or opcao == "2":
                return opcao
            else:
                print("\n\t Por favor, digite um valor válido.")
                input("\n\t Tecle ENTER para continuar.")
                os.system("cls")

    def validar_menu_decimal(self, menu: str) -> int:

        while True:

            print(menu)

            opcao = input("\n Selecione: ")

            if opcao.isdecimal():
                return int(opcao)
            else:
                print("\n\t Por favor, digite um valor válido.")
                input("\n\t Tecle ENTER para continuar.")
                os.system("cls")

    def selecionar_data(self) -> Data:
        """Função para selecionar uma data cadastrada"""

        os.system("cls")
        menu = """
            -----------------------------------------
            \tSelecionar data
            -----------------------------------------
            [1] - Listar datas cadastradas
            [2] - Selecionar por id
        """

        # opcao = input("\n Selecione: ")
        opcao = self.validar_menu_str(menu)

        if opcao == "1":
            self.ver_datas()

        id = self.validar_menu_decimal(" Informe o id desejado ")

        for data in self.lista_data:
            if data.id == id:
                self.lista_data.remove(data)
                return data

    def atualizar_datas(self, data_selecionada: Data) -> None:

        data_selecionada.data_categoria = self.data_cat_ctrl.selecionar_data_categoria()
        self.lista_data.append(data_selecionada)

    def inserir_data(self) -> str:
        os.system("cls")
        print("\t_____________________________________________")
        print("\t CADASTRAR DATA")
        print("\t_____________________________________________")

        data_str = input("\n\tQual data? Resp.: ")

        data_cat: DataCategoria = self.data_cat_ctrl.selecionar_data_categoria()

        data = Data(data=data_str, data_categoria=data_cat)

        self.lista_data.append(data)

    def existe_data_categoria(self) -> bool:
        # Checar se existe ao menos uma categoria
        return len(self.data_cat_ctrl.lista_dt_cat) > 0

    def deletar_data(self) -> None:

        os.system("cls")
        print(
            """
            ---------------------------------------------------------------
            \tSelecionar data para deletar
            ---------------------------------------------------------------
            [1] - Listar datas cadastradas
            [2] - Selecionar por id
        """
        )

        opcao = input("\n\t Opção: ")

        match opcao:
            case "1":
                self.ver_datas()
                id = int(input("\n\tDigite o id a ser deletado: "))
            case "2":
                id = int(input("\n\tDigite o id a ser deletado: "))
            case _:
                input("Opção inválida! ")

        for data in self.lista_data:
            if data.id == id:
                self.lista_data.remove(data)

    def menu_data(self) -> None:
        """Menu de Operações para data"""

        menu = """
        ----------------------------------------------
        \tMenu de operações Data_Categoria
        ----------------------------------------------
        [1] - Ver datas
        [2] - Inserir data
        [3] - Atualizar data
        [4] - Deletar data
        [0] - Voltar
        """

        while True:
            # Limpar a tela
            os.system("cls")

            print(menu)
            print()  # Linha vazia
            selecao = input("\tOpção: ")

            match selecao:
                case "0":  # [0] – Voltar
                    break
                case "1":  # [1] – Ver data
                    os.system("cls")
                    self.ver_datas()
                    input(
                        "\n Tecle Enter para continuar "
                    )  # Interromper momentâneamente o loop while
                case "2":  # [2] - Inserir data
                    os.system("cls")
                    if self.existe_data_categoria():
                        self.inserir_data()
                        print("\n\t Data cadastrada! ")
                    else:
                        print("\n\t Ainda não existe uma categoria de data! ")
                    input(
                        "\n Tecle Enter para continuar "
                    )  # Interromper momentâneamente o loop while
                case "3":  # [3] - Atualizar data
                    data_selecionada = self.selecionar_data()
                    self.atualizar_datas(data_selecionada)
                    input(
                        "\n Tecle Enter para continuar "
                    )  # Interromper momentâneamente o loop while
                case "4":  # [4] - Deletar data
                    self.deletar_data()

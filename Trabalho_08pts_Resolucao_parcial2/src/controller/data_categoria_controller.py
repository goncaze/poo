import os
from src.modelo.data_categoria import DataCategoria
from src.data import data_categoria_db as data_cat_db
from src.data.data_db import lista_data


class DataCategoriaController:

    def __init__(self):
        self.lista_dt_cat = data_cat_db.lista_data_cat
        self.lista_data = lista_data

    def bucar_data_por_categoria(self, dt_cat: DataCategoria) -> bool:
        for data in self.lista_data:
            resultado = True if data.data_categoria == dt_cat else False
        return resultado

    def ver_datas_categorias(self) -> None:
        os.system("cls")

        print("\t___________________________________________________________________")
        print("\t LISTA DE CATEGORIAS DE DATA CADASTRADAS")
        print("\t___________________________________________________________________")
        # print("\t Id\tCategoria\t\t\tDescrição")
        # print("\t----------------------------------------------------")
        for data_cat in self.lista_dt_cat:
            print(data_cat)
            print(
                "\t..................................................................."
            )
        print("\t___________________________________________________________________")

    def validar_menu_str(self, menu: str) -> str:
        os.system("cls")

        while True:

            print(menu)

            opcao = input("\n\t Selecione: ")

            if opcao == "1" or opcao == "2":
                return opcao
            else:
                print("\n\t Por favor, digite um valor válido.")
                input("\n\t Tecle ENTER para continuar.")
                os.system("cls")

    def validar_menu_decimal(self, menu: str) -> int:

        while True:

            print(menu)

            opcao = input("\n\t Digite: ")

            if opcao.isdecimal():
                return int(opcao)
            else:
                print("\n\t Por favor, digite um valor válido.")
                input("\n\t Tecle ENTER para continuar.")
                os.system("cls")

    def selecionar_data_categoria(self) -> DataCategoria:
        """Função para selecionar uma data_categoria cadastrada"""
        os.system("cls")

        menu = """
            -----------------------------------------
            \tSelecionar categoria de data
            -----------------------------------------
            [1] - Listar categorias cadastradas
            [2] - Selecionar por id
        """

        while True:
            opcao = self.validar_menu_str(menu)

            if opcao == "1":
                self.ver_datas_categorias()

            id = self.validar_menu_decimal("\t Informe o id desejado ")

            for data_cat in self.lista_dt_cat:
                if data_cat.id == id:

                    return data_cat

    def atualizar_datas_categorias(self, data_categoria: DataCategoria) -> None:

        data_categoria.categoria = input("Categoria: ")
        data_categoria.descricao = input("Descrição: ")

    def inserir_data_categoria(self) -> None:
        os.system("cls")
        print("\t____________________________________________________")
        print("\t Inserir categoria de data")
        print("\t----------------------------------------------------")
        categoria = input("\n\tDigite a categoria da data: ")
        descricao = input("\tDigite a descriçao dessa categoria: ")

        data_categoria = DataCategoria(categoria=categoria, descricao=descricao)
        self.lista_dt_cat.append(data_categoria)

    def deletar_data_categoria(self) -> str:
        """Função para selecionar uma data_categoria cadastrada"""
        os.system("cls")

        print(
            """
            ---------------------------------------------------------------
            \tSelecionar categoria de data para deletar
            ---------------------------------------------------------------
            [1] - Listar categorias cadastradas
            [2] - Selecionar por id
        """
        )

        resultado = """\n\n
            __________________________________________________
            Impossíve excluir essa Categoria!
            Ainda existe data cadastrada nesta categoria.
            __________________________________________________ 
        \n\n"""

        opcao = input("\n Opção: ")

        match opcao:
            case "1":
                self.ver_datas_categorias()
                id = int(input("\n\tDigite o id a ser deletado: "))
            case "2":
                id = int(input("\n\tDigite o id a ser deletado: "))

        for data_cat in self.lista_dt_cat:
            if data_cat.id == id:
                if self.bucar_data_por_categoria(data_cat):
                    return resultado
                else:
                    self.lista_dt_cat.remove(data_cat)
                    resultado = "\n\n\t\t Categoria excluída com sucesso! \n\n"
                    return resultado

    def menu_data_categoria(self) -> None:
        """Menu de Operações para data_categoria"""

        menu_data_categoria = """
        ----------------------------------------------
        \tMenu de operações Data_Categoria
        ----------------------------------------------
        [1] - Ver categorias de data
        [2] - Inserir categorias de data
        [3] - Atualizar categorias de data
        [4] - Deletar categorias de data
        [0] - Voltar
        """

        while True:
            # Limpar a tela
            os.system("cls")

            print(menu_data_categoria)
            print()  # Linha vazia
            selecao = input("Opção: ")

            match selecao:
                case "0":  # [0] – Voltar
                    break
                case "1":  # [1] – Ver categorias de data
                    os.system("cls")
                    self.ver_datas_categorias()
                    input(
                        "\n Tecle Enter para continuar "
                    )  # Interromper momentâneamente o loop while
                case "2":  # [2] - Inserir categorias de data
                    os.system("cls")
                    self.inserir_data_categoria()
                    input(
                        "\n Tecle Enter para continuar "
                    )  # Interromper momentâneamente o loop while
                case "3":  # [3] - Atualizar categorias de data
                    data_categoria = self.selecionar_data_categoria()
                    self.atualizar_datas_categorias(data_categoria)
                    input(
                        "\n Tecle Enter para continuar "
                    )  # Interromper momentâneamente o loop while
                case "4":  # [4] - Deletar categorias de data
                    print(self.deletar_data_categoria())
                    input(
                        "\n Tecle Enter para continuar "
                    )  # Interromper momentâneamente o loop while

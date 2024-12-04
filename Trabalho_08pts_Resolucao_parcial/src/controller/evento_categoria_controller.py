import os
from src.modelo.evento_categoria import EventoCategoria
from src.data import evento_categoria_db as evento_cat_db

# from src.data import evento as evento_cat_db


class EventoCategoriaController:

    def __init__(self):
        self.lista_evento_cat = evento_cat_db.lista_evento_cat
        # self.lista_data = lista_data

    def bucar_data_por_categoria(self, dt_cat: EventoCategoria) -> bool:
        for data in self.lista_data:
            resultado = True if data.data_categoria == dt_cat else False
        return resultado

    def ver_eventos_categorias(self) -> None:
        os.system("cls")

        print("\t___________________________________________________________________")
        print("\t LISTA DE CATEGORIAS DE EVENTOS CADASTRADAS")
        print("\t___________________________________________________________________")
        # print("\t Id\tCategoria\t\t\tDescrição")
        # print("\t----------------------------------------------------")
        for evento_cat in self.lista_evento_cat:
            print(evento_cat)
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

    def selecionar_evento_categoria(self) -> EventoCategoria:
        """Função para selecionar uma evento_categoria cadastrada"""
        os.system("cls")

        menu = """
            -----------------------------------------
            \tSelecionar categoria de evento
            -----------------------------------------
            [1] - Listar categorias cadastradas
            [2] - Selecionar por id
        """

        while True:
            opcao = self.validar_menu_str(menu)

            if opcao == "1":
                self.ver_eventos_categorias()

            id = self.validar_menu_decimal("\t Informe o id desejado ")

            for evento_cat in self.lista_evento_cat:
                if evento_cat.id == id:

                    return evento_cat

    def atualizar_eventos_categorias(self, data_categoria: EventoCategoria) -> None:

        data_categoria.categoria = input("Categoria: ")
        data_categoria.descricao = input("Descrição: ")

    def inserir_evento_categoria(self) -> None:
        os.system("cls")
        print("\t____________________________________________________")
        print("\t Inserir categoria de evento")
        print("\t----------------------------------------------------")
        categoria = input("\n\tDigite a categoria do evento: ")
        descricao = input("\tDigite a descrição dessa categoria: ")

        data_categoria = EventoCategoria(categoria=categoria, descricao=descricao)
        self.lista_evento_cat.append(data_categoria)

    def deletar_evento_categoria(self) -> str:
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
                self.ver_eventos_categorias()
                id = int(input("\n\tDigite o id a ser deletado: "))
            case "2":
                id = int(input("\n\tDigite o id a ser deletado: "))

        for evento_cat in self.lista_evento_cat:
            if evento_cat.id == id:
                # if self.bucar_data_por_categoria(evento_cat):
                #     return resultado
                # else:
                self.lista_evento_cat.remove(evento_cat)
                resultado = "\n\n\t\t Categoria excluída com sucesso! \n\n"
                return resultado

    def menu_evento_categoria(self) -> None:
        """Menu de Operações para data_categoria"""

        menu_evento_categoria = """
        ----------------------------------------------
        \tMenu de operações Evento_Categoria
        ----------------------------------------------
        [1] - Ver categorias de evento
        [2] - Inserir categorias de evento
        [3] - Atualizar categorias de evento
        [4] - Deletar categorias de evento
        [0] - Voltar
        """

        while True:
            # Limpar a tela
            os.system("cls")

            print(menu_evento_categoria)
            print()  # Linha vazia
            selecao = input("Opção: ")

            match selecao:
                case "0":  # [0] – Voltar
                    break
                case "1":  # [1] – Ver categorias de data
                    os.system("cls")
                    self.ver_eventos_categorias()
                    input(
                        "\n Tecle Enter para continuar "
                    )  # Interromper momentâneamente o loop while
                case "2":  # [2] - Inserir categorias de data
                    os.system("cls")
                    self.inserir_evento_categoria()
                    input(
                        "\n Tecle Enter para continuar "
                    )  # Interromper momentâneamente o loop while
                case "3":  # [3] - Atualizar categorias de data
                    data_categoria = self.selecionar_evento_categoria()
                    self.atualizar_eventos_categorias(data_categoria)
                    input(
                        "\n Tecle Enter para continuar "
                    )  # Interromper momentâneamente o loop while
                case "4":  # [4] - Deletar categorias de data
                    print(self.deletar_evento_categoria())
                    input(
                        "\n Tecle Enter para continuar "
                    )  # Interromper momentâneamente o loop while

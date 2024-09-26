from os import system
from modelo.data_categoria import DataCategoria



def ver_datas_categorias(lista:list[DataCategoria])->None:
    """Função para ver as data_categorias cadastradas"""

    for item in lista:
        print(item)



def selecionar_data_categoria(lista:list[DataCategoria])->DataCategoria:
    """Função para selecionar uma data_categoria cadastrada"""

    system('cls')
    print("""                   
        -----------------------------------------
        \tSelecionar categoria de data
        -----------------------------------------
        [1] - Listar categorias cadastradas
        [2] - Selecionar por id
    """)

    opcao = input("\n Opção: ")

    match opcao:
        case '1':
          ver_datas_categorias(lista)
          id = int(input("Digite o id desejado: "))
        case '2':
          id = int(input("Digite o id desejado: "))

    for item in lista:
        if item.id == id:
          lista.remove(item)
          return item
    

 
def atualizar_datas_categorias(data_categoria: DataCategoria, lista :list[DataCategoria])->None:
    """Função para atualizar uma data_categoria cadastrada"""

    data_categoria._categoria = input("Categoria: ")
    data_categoria._descricao = input("Descrição: ")
    lista.append(data_categoria)



def inserir_data_categoria(datas_categorias:list[DataCategoria])->None:  
    """Função para inserir uma data_categoria"""

    system("cls") 
    categoria = input("Digite a categoria da data: ")
    descricao = input("Digite a descriçao dessa categoria: ")

    data_categoria = DataCategoria(categoria=categoria, descricao=descricao)
    datas_categorias.append(data_categoria)



def deletar_data_categoria(lista:list[DataCategoria])->None:
    """Função para selecionar uma data_categoria cadastrada"""

    system('cls')
    print("""                   
        ---------------------------------------------------------------
        \tSelecionar categoria de data para deletar
        ---------------------------------------------------------------
        [1] - Listar categorias cadastradas
        [2] - Selecionar por id
    """)

    opcao = input("\n Opção: ")

    match opcao:
        case '1':
          ver_datas_categorias(lista)
          id = int(input("\n\tDigite o id a ser deletado: "))
        case '2':
          id = int(input("\n\tDigite o id a ser deletado: "))

    for item in lista:
        if item.id == id:
          lista.remove(item)



def menu_data_categoria()->None:
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

    lista:list[DataCategoria] = []

    while(True):
        # Limpar a tela
        system("cls")

        print(menu_data_categoria)
        print() # Linha vazia
        selecao = input("Opção: ")

        match selecao:
            case '0': # [0] – Voltar
                break
            case '1': # [1] – Ver categorias de data
                system("cls")
                ver_datas_categorias(lista)
                input("\n Tecle Enter para continuar ") # Interromper momentâneamente o loop while
            case '2': # [2] - Inserir categorias de data
                system("cls")
                inserir_data_categoria(lista)
                input("\n Tecle Enter para continuar ") # Interromper momentâneamente o loop while
            case '3': # [3] - Atualizar categorias de data
                data_categoria = selecionar_data_categoria(lista)
                atualizar_datas_categorias(data_categoria, lista)
                input("\n Tecle Enter para continuar ") # Interromper momentâneamente o loop while
            case '4': # [4] - Deletar categorias de data
                deletar_data_categoria(lista)            
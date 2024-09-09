# importação da biblioteca OS para limpeza de tela
import os
##
# Um MÓDULO Python é um arquivo com a extensão .py que 
# contém definições e implementações de funções, variáveis 
# e classes. Ex.: gato.py, peixe.py, etc.

# importação da classe Cachorro a partir do módulo cachorro.py
from cachorro import Cachorro
# importação da classe Gato a partir do módulo gato.py
from gato import Gato
# importação da classe Elefante a partir do módulo elefante.py
from elefante import Elefante
# importação da classe Peixe a partir do módulo peixe.py
from peixe import Peixe
# importação da classe Gato a partir do módulo passaro.py
from passaro import Passaro


# declaração de uma lista vazia
lista_de_animais = []

# menu das opções da aplicação
menu = """
    [0] - Encerrar
    [1] - Tamanho da lista
    [2] - Imprimir lista
    [3] - Inserir animal
    [4] - Quantidade de animais por espécie.
"""

# menu das opções de espécies
menu_animais = """
    [0] - Cachorro
    [1] - Elefante
    [2] - Gato
    [3] - Pássaro
    [4] - Peixe
"""


# função para determinar o tamanho da lista. Recebe lista como argumento.
def tamanho_da_lista(lista_de_animais: list) -> int:
    # len é a função built-in de Python para aferir o tamanho da lista
    tamanho = len(lista_de_animais)
    # retornar a informação do tamanho da lista
    return tamanho


# função para imprimir a lista. Recebe lista como argumento.
def imprimir_lista(lista_de_animais: list):
    # laço de repetição para percorrer uma lista
    # para cada animal contido na lista de animais
    for animal in lista_de_animais:
        # faça a impressão do objeto animal
        print(animal)


# função para inserir um objeto de animal na lista de animais
# Recebe lista como argumento.
def inserir_animal(lista_de_animais: list):
    # limpar a tela do terminal com o comando cls
    os.system("cls")
    # imprimir o menu de espécies
    print(menu_animais)
    # capturar a escolha do usuário
    opcao = input("Qual espécie deseja inserir na lista: ")

    # corresponder com a escolha do usuário
    match opcao:

        # caso corresponder com zero
        case "0":
            # instanciar um objeto da classe Cachorro
            animal = Cachorro()
            # incluir objeto na lista de animais
            lista_de_animais.append(animal)

        # caso corresponder com um
        case "1":
            # instanciar um objeto da classe Elefante
            animal = Elefante()
            # incluir objeto na lista de animais
            lista_de_animais.append(animal)

        # caso corresponder com dois
        case "2":
            # instanciar um objeto da classe Gato
            animal = Gato()
            # incluir objeto na lista de animais
            lista_de_animais.append(animal)

        # caso corresponder com três
        case "3":
            # instanciar um objeto da classe Passaro
            animal = Passaro()
            # incluir objeto na lista de animais
            lista_de_animais.append(animal)

        # caso corresponder com quatro
        case "4":
            # instanciar um objeto da classe Peixe  
            animal = Peixe()
            # incluir objeto na lista de animais
            lista_de_animais.append(animal)

        # caso corresponder com nenhuma opção disponível
        case _:
            # informar que a opção é inválida
            print(f"\n\t A opção {opcao} não é válida! \n")


# determinar a quantidade de espécies diferentes na lista
def quantidade_especie(lista_animais:list):
    
    # variáveis do tipo int para contabilizar cada espécie
    cao, elefante, gato, passaro, peixe = 0,0,0,0,0

    # laço de repetiçao para perrcorar a lista de animais
    for animal in lista_animais:      

        ##
        # formas de como determinar o tipo de um objeto:
        # isinstance(animal, Gato)  
        # animal.__class__.__name__ == "Gato"
        # type(animal).__name__ == "Gato"

        # corresponder ao tipo do objeto
        match type(animal).__name__:

            # caso corresponder com Cachorro
            case "Cachorro":
                # some mais um desse tipo
                cao += 1

            # caso corresponder com Elefante
            case "Elefante":
                # some mais um desse tipo
                elefante += 1

            # caso corresponder com Gato
            case "Gato":
                # some mais um desse tipo
                gato += 1

            # caso corresponder com Passaro
            case "Passaro":        
                # some mais um desse tipo
                passaro += 1

            # caso corresponder com Peixe
            case "Peixe":
                # some mais um desse tipo
                peixe += 1


    # hora de imprmir a quantidade de animais por espécie          
    print("\n\tQuantidade de animais por espécie:\n")
    print(f"\t{ cao = }")
    print(f"\t{ elefante = }")
    print(f"\t{ gato = }")
    print(f"\t{ passaro = }")
    print(f"\t{ peixe = }")


# laço de repetição infinito
while True:

    # limpar a tela do terminal
    os.system("cls")
    
    # imprimir menu de opções
    print(menu)
    # imprimir uma linha vazia
    print()

    # capturar a escolha do usuário deste aplicativo
    opcao_selecionada = input("Opção: ")
    
    # corresponder à opção selecionada pelo usuário
    match opcao_selecionada:

        # caso corresponder com zero
        case "0":
            os.system("cls")
            print("Encerrando a aplicação")
            print()
            # interromper laço infinito
            break

        # caso corresponder com um                
        case "1":
            os.system("cls")
            tamanho = tamanho_da_lista(lista_de_animais)
            print(f"Tamanho da lista: {tamanho}")
            input()

        # caso corresponder com dois                 
        case "2":
            os.system("cls")
            imprimir_lista(lista_de_animais)
            input()

        # caso corresponder com três               
        case "3":
            os.system("cls")
            inserir_animal(lista_de_animais)

        # caso corresponder com quatro               
        case "4":
            os.system("cls")
            quantidade_especie(lista_de_animais)
            input()

            
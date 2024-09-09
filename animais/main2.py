import os
from cachorro import Cachorro
from gato import Gato
from elefante import Elefante
from peixe import Peixe
from passaro import Passaro


classes_de_animais = [Cachorro, Gato, Elefante, Peixe, Passaro]
lista_de_animais = []


menu = """
    [0] - Encerrar
    [1] - Tamanho da lista
    [2] - Imprimir lista
    [3] - Inserir animal
    [4] - Quantidade de animais por espécie.
"""


def menu_animais(classes_de_animais:list)->str:
    i = 0
    menu = ""

    while i < len(classes_de_animais):
        menu += f"\t{[i]} - {classes_de_animais[i].__name__} \n"
        i += 1

    return menu



def tamanho_da_lista(lista_de_animais: list) -> int:
    tamanho = len(lista_de_animais)
    return tamanho



def imprimir_lista(lista_de_animais: list):
    for animal in lista_de_animais:
        print(animal)



def inserir_animal(lista_de_animais: list):
    os.system("cls")

    print(menu_animais(classes_de_animais))

    opcao = input("Qual espécie deseja inserir na lista: ")

    indice = int(opcao)
    animal = classes_de_animais[indice]()
    lista_de_animais.append(animal)



def quantidade_especie(lista_animais:list):
    cao, elefante, gato, passaro, peixe = 0,0,0,0,0

    for animal in lista_animais:      
        # isinstance(animal, Gato)  
        # animal.__class__.__name__ == "Gato"
        # type(animal).__name__ == "Gato"
        match type(animal).__name__:
            case "Cachorro":
                cao += 1                                        
            case "Elefante":
                elefante += 1
            case "Gato":
                gato += 1
            case "Passaro":        
                passaro += 1
            case "Peixe":
                peixe += 1

    print("\n\tQuantidade de animais por espécie:\n")
    print(f"\t{ cao = }")
    print(f"\t{ elefante = }")
    print(f"\t{ gato = }")
    print(f"\t{ passaro = }")
    print(f"\t{ peixe = }")
    


while True:
    os.system("cls")
    
    print(menu)
    print()
    opcao_selecionada = input("Opção: ")
    
    match opcao_selecionada:
        case "0":
            os.system("cls")
            print("Encerrando a aplicação")
            print()
            break
        case "1":
            os.system("cls")
            tamanho = tamanho_da_lista(lista_de_animais)
            print(f"Tamanho da lista: {tamanho}")
            input()
        case "2":
            os.system("cls")
            imprimir_lista(lista_de_animais)
            input()
        case "3":
            os.system("cls")
            inserir_animal(lista_de_animais)
        case "4":
            os.system("cls")
            quantidade_especie(lista_de_animais)
            input()
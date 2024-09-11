import os
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-a", "--arquivo_txt")

args = parser.parse_args()


def remover_ponto_barra(nome_arquivo: str) -> str:
    if nome_arquivo.startswith(".\\"):
        return nome_arquivo[2:]
    else:
        return nome_arquivo


def nomear_classe(nome_arquivo: str) -> str:
    ponto_posicao = nome_arquivo.find(".")
    nome_classe = nome_arquivo[0:ponto_posicao]

    return nome_classe


def ler_atributos(nome_arquivo: str) -> list:
    atributos = []

    with open(file=nome_arquivo, mode="r", encoding="utf-8") as f:
        for line in f:
            atributos.append(line.strip())
            print(line, end="")

        print("\n\n")
    return atributos


def gerar_classe(nome_classe: str, atributos: list):
    with open(file=f"{nome_classe}.py", mode="w", encoding="utf-8") as f:
        f.write(f"class {nome_classe.capitalize()}: \n")
        f.write("\n")
        f.write("\tdef __init__(self")  # , end="")
        for atributo in atributos:
            f.write(f", {atributo}")  # , end="")
        f.write("): \n")

        for atributo in atributos:
            f.write(f"\t\tself._{atributo} = {atributo} \n")

        for atributo in atributos:
            f.write("\n")
            f.write("\t@property \n")
            f.write(f"\tdef {atributo}(self): \n")
            f.write(f"\t\treturn self._{atributo} \n")
            f.write("\n")
            f.write(f"\t@{atributo}.setter \n")
            f.write(f"\tdef {atributo}(self, new_{atributo}): \n")
            f.write(f"\t\tself._{atributo} = new_{atributo} \n")


def listar_selecionar_arquivo(arquivos: list) -> str:
    i = 0
    filtro = []
    print("\n\tArquivos disponíveis: \n")
    for arquivo in arquivos:
        if arquivo.lower().endswith(".txt"):
            print(f"\t[{i}] {arquivo}")
            filtro.append(arquivo)
            i += 1

    numero_arquivo = input("\nDigite o número do arquivo: ")
    nome_arquivo = filtro[int(numero_arquivo)]
    return nome_arquivo


if not (args.arquivo_txt is None):
    os.system("cls")
    nome_arquivo = remover_ponto_barra(args.arquivo_txt)
    atributos = ler_atributos(nome_arquivo)
    nome_classe = nomear_classe(nome_arquivo)
    gerar_classe(nome_classe, atributos)
else:
    os.system("cls")
    arquivos = os.listdir()
    nome_arquivo = listar_selecionar_arquivo(arquivos)
    atributos = ler_atributos(nome_arquivo)
    nome_classe = nomear_classe(nome_arquivo)
    gerar_classe(nome_classe, atributos)

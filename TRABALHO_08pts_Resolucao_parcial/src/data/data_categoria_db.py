from src.modelo.data_categoria import DataCategoria

lista_data_cat: list[DataCategoria] = []

data_cat = DataCategoria("Letivo", "aula normal")
lista_data_cat.append(data_cat)
data_cat = DataCategoria("Recesso", "recesso natalino")
lista_data_cat.append(data_cat)

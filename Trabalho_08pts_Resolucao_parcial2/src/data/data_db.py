from src.modelo.data import Data
from src.data import data_categoria_db as data_categoria_db


lista_data: list[Data] = []

data = Data("06/11/2024", data_categoria_db.lista_data_cat[0])
lista_data.append(data)
data = Data("25/12/2024", data_categoria_db.lista_data_cat[0])
lista_data.append(data)
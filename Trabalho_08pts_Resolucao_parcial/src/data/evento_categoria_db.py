from src.modelo.evento_categoria import EventoCategoria

lista_evento_cat: list[EventoCategoria] = []

evento_cat = EventoCategoria("Reunião", "Qualquer reunião")
lista_evento_cat.append(evento_cat)
evento_cat = EventoCategoria("Formatura", "Cerimônia de formatura")
lista_evento_cat.append(evento_cat)

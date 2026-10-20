# -*- coding: utf-8 -*-
"""
Una sola instancia de la Pila, compartida por todos los controllers.
La cima es la pagina actual; debajo estan las anteriores.
"""
from tda.pila import Pila

pila_historial = Pila()

# -*- coding: utf-8 -*-
"""
TDA: Pila (LIFO - Ultimas Entradas, Primeras Salidas)
-------------------------------------------------------
Como una pila de platos: solo se agrega y se quita por UN extremo, la
CIMA. El ultimo elemento que se apila es el primero que se recupera.
En el navegador, la cima de la pila es siempre la pagina actual.

Apilar y desapilar cuestan O(1): list.append() y list.pop() (sin
argumento) trabajan sobre el final de la lista y no desplazan nada.
"""


class Pila:
    def __init__(self):
        self._datos = []

    def __len__(self):
        return len(self._datos)

    def apilar(self, elemento):
        """Pone un elemento en la CIMA de la pila."""
        self._datos.append(elemento)

    def desapilar(self):
        """
        Quita y regresa el elemento de la CIMA (el ultimo que entro).
        Si la pila esta vacia, regresa None en vez de lanzar un error.
        """
        if self.esta_vacia():
            return None
        return self._datos.pop()

    def cima(self):
        """Consulta el elemento de la cima SIN quitarlo."""
        if self.esta_vacia():
            return None
        return self._datos[-1]

    def esta_vacia(self):
        return len(self._datos) == 0

    def tamano(self):
        return len(self._datos)

    def obtener_descendente(self):
        """Regresa todos los elementos del mas reciente al mas antiguo."""
        return list(reversed(self._datos))

    def vaciar(self):
        """Elimina todos los elementos de la pila."""
        self._datos.clear()

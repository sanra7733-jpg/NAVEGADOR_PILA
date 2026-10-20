import web

from controllers.estado import pila_historial

render = web.template.render('views', base='layout')


class RegresarPagina:
    def GET(self):
        # Historial vacio: no hay nada de donde regresar
        if pila_historial.esta_vacia():
            return render.regresar_pagina('vacio', None, None)

        # Solo hay una pagina: es la actual y no existe una anterior
        if pila_historial.tamano() == 1:
            return render.regresar_pagina('sin_anterior', pila_historial.cima(), None)

        # Se quita la actual (cima) y la anterior pasa a ser la nueva cima
        abandonada = pila_historial.desapilar()
        return render.regresar_pagina('ok', pila_historial.cima(), abandonada)

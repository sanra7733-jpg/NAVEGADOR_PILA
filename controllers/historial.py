import web

from controllers.estado import pila_historial

render = web.template.render('views', base='layout')


class Historial:
    def GET(self):
        paginas = pila_historial.obtener_descendente()
        return render.historial(paginas, pila_historial.tamano())

import web

from controllers.estado import pila_historial

render = web.template.render('views', base='layout')


class PaginaActual:
    def GET(self):
        return render.pagina_actual(pila_historial.cima())

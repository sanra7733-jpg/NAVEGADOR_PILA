import web

from controllers.estado import pila_historial

render = web.template.render('views', base='layout')


class VerificarHistorial:
    def GET(self):
        entrada = web.input(eliminado='')
        return render.verificar_historial(
            pila_historial.esta_vacia(), pila_historial.tamano(), entrada.eliminado
        )

    def POST(self):
        if pila_historial.esta_vacia():
            destino = '/verificar_historial'
        else:
            pila_historial.vaciar()
            destino = '/verificar_historial?eliminado=1'

        web.ctx.status = '303 See Other'
        web.header('Location', destino)
        return ''

import web

from controllers.estado import pila_historial

render = web.template.render('views', base='layout')


class VisitarPagina:
    def GET(self):
        return render.visitar_pagina(None)

    def POST(self):
        entrada = web.input(url='')
        url = entrada.url.strip()

        if not url:
            return render.visitar_pagina("Escribe la direccion de la pagina a visitar.")

        pila_historial.apilar(url)

        # Redirect RELATIVO a mano (en Codespaces web.seeother te saca a localhost)
        web.ctx.status = '303 See Other'
        web.header('Location', '/pagina_actual')
        return ''

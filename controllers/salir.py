import web

render = web.template.render('views', base='layout')


class Salir:
    def GET(self):
        return render.salir()

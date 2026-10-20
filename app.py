import web

# Evita que el servidor de desarrollo espere una resolucion DNS inversa
# por cada peticion (hacia lento cada click dentro de Codespaces).
import http.server
http.server.BaseHTTPRequestHandler.address_string = lambda self: self.client_address[0]

urls = (
    '/', 'controllers.index.Index',
    '/visitar_pagina', 'controllers.visitar_pagina.VisitarPagina',
    '/regresar_pagina', 'controllers.regresar_pagina.RegresarPagina',
    '/pagina_actual', 'controllers.pagina_actual.PaginaActual',
    '/historial', 'controllers.historial.Historial',
    '/verificar_historial', 'controllers.verificar_historial.VerificarHistorial',
    '/salir', 'controllers.salir.Salir',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

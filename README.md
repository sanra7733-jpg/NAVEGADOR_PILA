# Navegador web (simulacion con Pila - LIFO)

Ejercicio: un navegador administra las paginas visitadas con una
**Pila**: la ultima pagina registrada es la primera en recuperarse
(LIFO). La cima de la pila es siempre la pagina actual.

Misma estructura que los ejercicios anteriores (web.py + controllers +
views + tda).

## Estructura

```
navegador_pila/
├── app.py
├── controllers/
│   ├── estado.py               # la unica instancia de la Pila (pila_historial)
│   ├── index.py                # menu principal
│   ├── visitar_pagina.py       # apilar
│   ├── regresar_pagina.py      # desapilar
│   ├── pagina_actual.py        # cima
│   ├── historial.py            # recorrido descendente
│   ├── verificar_historial.py  # esta_vacia / vaciar
│   └── salir.py
├── tda/
│   └── pila.py                 # el TDA: Pila (LIFO)
├── temporal/app.py
└── views/                      # una vista por pantalla
```

## Opciones del menu -> donde estan

| Opcion | Ruta | TDA |
|---|---|---|
| 1. Visitar una pagina web | `/visitar_pagina` | `Pila.apilar()` |
| 2. Regresar a la pagina anterior | `/regresar_pagina` | `Pila.desapilar()` + `Pila.cima()` |
| 3. Mostrar la pagina actual | `/pagina_actual` | `Pila.cima()` |
| 4. Historial en orden descendente | `/historial` | `Pila.obtener_descendente()` |
| 5. Verificar si esta vacio / eliminar | `/verificar_historial` | `Pila.esta_vacia()`, `Pila.vaciar()` |
| 6. Salir | `/salir` | - |

## Como funciona "regresar"

Si visitas A, B, C, la pila queda [A, B, C] y la pagina actual es C.
Al regresar se desapila C y la nueva cima, B, pasa a ser la pagina
actual. Si solo queda una pagina no hay anterior y se avisa; si el
historial esta vacio tambien se avisa.

## Como correrlo

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

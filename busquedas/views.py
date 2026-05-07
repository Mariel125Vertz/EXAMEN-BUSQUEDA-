from django.shortcuts import render

from .ucs import buscar_solucion_ucs
from .bfs import buscar_solucion_BFS
from .bpi import DFS_prof_iter

from .arbol import Nodo


def reconstruir_camino(nodo, inicio):

    camino = []

    while nodo.get_padre() is not None:

        camino.append(nodo.get_datos())

        nodo = nodo.get_padre()

    camino.append(inicio)

    camino.reverse()

    return camino


def index(request):

    resultado_ucs = None
    resultado_bfs = None
    resultado_bpi = None

    # =========================
    # UCS - CARRETERAS
    # =========================

    conexiones_ucs = {

        'JILOYORK': {
            'CDMX': 125,
            'QUERETARO': 513
        },

        'CDMX': {
            'QUERETARO': 423,
            'HIDALGO': 491
        },

        'HIDALGO': {
            'MONTERREY': 346
        },

        'QUERETARO': {
            'MONTERREY': 603,
            'AGUASCALIENTES': 599
        },

        'MONTERREY': {},

        'AGUASCALIENTES': {}
    }

    # =========================
    # BFS - VUELOS
    # =========================

    conexiones_bfs = {

        'JILOYORK': {
            'CELAYA',
            'CDMX',
            'QUERETARO'
        },

        'CELAYA': {
            'JILOYORK'
        },

        'CDMX': {
            'ZACATECAS',
            'OAXACA'
        },

        'QUERETARO': {
            'MONTERREY',
            'TAMAULIPAS'
        },

        'ZACATECAS': {
            'MONTERREY'
        },

        'MONTERREY': {},

        'TAMAULIPAS': {},

        'OAXACA': {}
    }

    # =========================
    # BPI
    # =========================

    conexiones_bpi = {

        'JILOYORK': {
            'CELAYA',
            'CDMX',
            'QUERETARO'
        },

        'CELAYA': {
            'SINALOA'
        },

        'CDMX': {
            'OAXACA'
        },

        'QUERETARO': {
            'MONTERREY'
        },

        'SINALOA': {
            'SONORA'
        },

        'SONORA': {
            'ZACATECAS'
        },

        'ZACATECAS': {},

        'MONTERREY': {},

        'OAXACA': {}
    }

    if request.method == 'POST':

        estado_inicial = request.POST.get(
            'inicio'
        ).upper()

        estado_final = request.POST.get(
            'final'
        ).upper()

        # =========================
        # UCS
        # =========================

        nodo_inicial = Nodo(
            estado_inicial
        )

        nodo_ucs = buscar_solucion_ucs(
            conexiones_ucs,
            nodo_inicial,
            estado_final
        )

        if nodo_ucs:

            resultado_ucs = {

                'camino':
                reconstruir_camino(
                    nodo_ucs,
                    estado_inicial
                ),

                'costo':
                nodo_ucs.get_costo()
            }

        else:

            resultado_ucs = {

                'camino':
                'Ruta no encontrada',

                'costo':
                '-'
            }

        # =========================
        # BFS
        # =========================

        nodo_bfs = buscar_solucion_BFS(
            conexiones_bfs,
            estado_inicial,
            estado_final
        )

        if nodo_bfs:

            resultado_bfs = reconstruir_camino(
                nodo_bfs,
                estado_inicial
            )

        else:

            resultado_bfs = 'Ruta no encontrada'

        # =========================
        # BPI
        # =========================

        nodo_inicio_bpi = Nodo(
            estado_inicial
        )

        nodo_bpi = DFS_prof_iter(
            nodo_inicio_bpi,
            estado_final,
            conexiones_bpi
        )

        if nodo_bpi:

            resultado_bpi = reconstruir_camino(
                nodo_bpi,
                estado_inicial
            )

        else:

            resultado_bpi = 'Ruta no encontrada'

    return render(request, 'index.html', {

        'resultado_ucs':
        resultado_ucs,

        'resultado_bfs':
        resultado_bfs,

        'resultado_bpi':
        resultado_bpi
    })
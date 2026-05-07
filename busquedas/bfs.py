from .arbol import Nodo


def buscar_solucion_BFS(conexiones, estado_inicial, solucion):

    nodos_visitados = []

    nodos_frontera = []

    nodo_inicial = Nodo(estado_inicial)

    nodos_frontera.append(nodo_inicial)

    while len(nodos_frontera) != 0:

        nodo = nodos_frontera.pop(0)

        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:

            return nodo

        else:

            dato_nodo = nodo.get_datos()

            lista_hijos = []

            for un_hijo in conexiones.get(dato_nodo, []):

                hijo = Nodo(un_hijo)

                hijo.set_padre(nodo)

                lista_hijos.append(hijo)

                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):

                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

    return None
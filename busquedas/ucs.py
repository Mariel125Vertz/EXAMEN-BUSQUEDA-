from .arbol import Nodo


def buscar_solucion_ucs(conexiones, nodo_inicial, solucion):

    nodos_visitados = []

    nodos_frontera = []

    nodo_inicial.set_costo(0)

    nodos_frontera.append(nodo_inicial)

    while len(nodos_frontera) != 0:

        nodos_frontera = sorted(
            nodos_frontera,
            key=lambda x: x.get_costo()
        )

        nodo = nodos_frontera.pop(0)

        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:

            return nodo

        else:

            dato_nodo = nodo.get_datos()

            lista_hijos = []

            for un_hijo in conexiones.get(dato_nodo, {}):

                hijo = Nodo(un_hijo)

                hijo.set_padre(nodo)

                costo = conexiones[dato_nodo][un_hijo]

                hijo.set_costo(
                    nodo.get_costo() + costo
                )

                lista_hijos.append(hijo)

                if not hijo.en_lista(nodos_visitados):

                    if hijo.en_lista(nodos_frontera):

                        for n in nodos_frontera:

                            if n.igual(hijo) and n.get_costo() > hijo.get_costo():

                                nodos_frontera.remove(n)

                                nodos_frontera.append(hijo)

                    else:

                        nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

    return None
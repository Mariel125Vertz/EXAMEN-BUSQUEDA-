from .arbol import Nodo


def DFS_prof_iter(nodo, solucion, conexiones):

    for limite in range(1, 100):

        visitados = []

        sol = buscar_solucion_DFS_Rec(
            nodo,
            solucion,
            visitados,
            limite,
            conexiones
        )

        if sol is not None:
            return sol

    return None


def buscar_solucion_DFS_Rec(
        nodo,
        solucion,
        visitados,
        limite,
        conexiones):

    visitados.append(nodo.get_datos())

    if nodo.get_datos() == solucion:

        return nodo

    if limite <= 0:

        return None

    dato_nodo = nodo.get_datos()

    lista_hijos = []

    for un_hijo in conexiones.get(dato_nodo, []):

        if un_hijo not in visitados:

            hijo = Nodo(un_hijo)

            hijo.set_padre(nodo)

            lista_hijos.append(hijo)

    nodo.set_hijos(lista_hijos)

    for nodo_hijo in nodo.get_hijos():

        sol = buscar_solucion_DFS_Rec(
            nodo_hijo,
            solucion,
            visitados,
            limite - 1,
            conexiones
        )

        if sol is not None:

            return sol

    return None
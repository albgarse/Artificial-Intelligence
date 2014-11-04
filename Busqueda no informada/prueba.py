from arbol import Nodo

def buscar_solucion(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial
    else:
        # expandir nodos sucesores (hijos)
        dato_nodo = nodo_inicial.get_datos()
        hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
        hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
        hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])
        nodo_inicial.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

        for nodo_hijo in nodo_inicial.get_hijos():
            if not nodo_hijo.get_datos() in visitados:
                sol = buscar_solucion(nodo_hijo, solucion, visitados)
                if sol != None:
                    return sol

        return None


if __name__ == "__main__":
    print "recursiva"
    estado_inicial=[4,2,3,1]
    solucion=[1,2,3,4]
    nodo_solucion = None
    visitados=[]

    nodo_inicial = Nodo(estado_inicial)

    nodo = buscar_solucion(nodo_inicial, solucion, visitados)

    # mostrar resultado (al reves)
    while nodo.padre != None:
        print nodo
        nodo = nodo.padre

    print nodo
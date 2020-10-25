# Puzle Lineal con busqueda en profundidad (DEPTH FIRST SEARCH) Recuersivo para prescindir de la lista de frontera
from arbol import Nodo

def buscar_solucion_DFS(nodo_inicial, solucion,visitados):
    visitados.append(nodo_inicial.getDatos())
    if nodo_inicial.getDatos()== solucion:
        #Solcuion encontrada
        return nodo_inicial
    else:
        #expandir nodos hijos
        dato_nodo= nodo_inicial.getDatos()
        hijo = [dato_nodo[1],dato_nodo[0],dato_nodo[2],dato_nodo[3]]
        hijo_izquierdo = Nodo(hijo)
        hijo=[dato_nodo[0],dato_nodo[2],dato_nodo[1],dato_nodo[3]]
        hijo_central = Nodo(hijo)
        hijo=[dato_nodo[0],dato_nodo[1],dato_nodo[3],dato_nodo[2]]
        hijo_derecho = Nodo(hijo)
        nodo_inicial.setHijos([hijo_izquierdo,hijo_central,hijo_derecho])
        for nodo_hijo in nodo_inicial.getHijos():
            if (not nodo_hijo.getDatos() in visitados):
                # llamada recursiva
                sol=buscar_solucion_DFS(nodo_hijo,solucion,visitados)
                if sol!=None:
                    return sol
        return None



if __name__=="__main__":
    estado_inicial= [4,2,3,1]
    solucion= [1,2,3,4]
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    #mostrar resultado
    resultado=[]
    nodo=buscar_solucion_DFS(nodo_inicial,solucion,visitados)
    while nodo.getPadre()!=None:
        resultado.append(nodo.getDatos())
        nodo = nodo.getPadre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print (resultado)

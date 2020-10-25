# Puzle Lineal con busqueda en amplitud (BREAD FIRST SEARCH)
from arbol import Nodo

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado= False
    nodos_visitados=[]
    nodos_frontera=[]
    nodoInicial=Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera)!=0:
        #extraer nodo y añadirlo a visitados
        nodo=nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        if nodo.getDatos()== solucion:
            #Solcuion encontrada
            solucionado= True
            return nodo
        else:
            #expandir nodos hijos
            dato_nodo= nodo.getDatos()

            #operador izquierdo
            hijo = [dato_nodo[1],dato_nodo[0],dato_nodo[2],dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            if (not hijo_izquierdo.enLista(nodos_visitados))and (not hijo_izquierdo.enLista(nodos_frontera)):
                nodos_frontera.append(hijo_izquierdo)
            #operador central
            hijo=[dato_nodo[0],dato_nodo[2],dato_nodo[1],dato_nodo[3]]
            hijo_central = Nodo(hijo)
            if (not hijo_central.enLista(nodos_visitados))and (not hijo_central.enLista(nodos_frontera)):
                nodos_frontera.append(hijo_central)
            #operador derecho
            hijo=[dato_nodo[0],dato_nodo[1],dato_nodo[3],dato_nodo[2]]
            hijo_derecho = Nodo(hijo)
            if (not hijo_derecho.enLista(nodos_visitados))and (not hijo_derecho.enLista(nodos_frontera)):
                nodos_frontera.append(hijo_derecho)

            nodo.setHijos([hijo_izquierdo,hijo_central,hijo_derecho])

if __name__=="__main__":
    estado_inicial= [4,2,3,1]
    solucion= [1,2,3,4]
    nodo_solucion = buscar_solucion_BFS(estado_inicial,solucion)
    #mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.getPadre()!=None:
        resultado.append(nodo.getDatos())
        nodo = nodo.getPadre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print (resultado)

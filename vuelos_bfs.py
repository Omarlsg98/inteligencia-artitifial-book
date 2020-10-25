# Conexiones vuelo con busqueda en amplitud (BREAD FIRST SEARCH)
from arbol import Nodo

def buscar_solucion_BFS(conexiones,estado_inicial, solucion):
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
            #expandir nodos hijos (ciudades con conexion)
            dato_nodo= nodo.getDatos()
            lista_hijos=[]

            for un_hijo in conexiones[dato_nodo]:
                hijo=Nodo(un_hijo)
                lista_hijos.append(hijo)
                if (not hijo.enLista(nodos_visitados))and (not hijo.enLista(nodos_frontera)):
                    nodos_frontera.append(hijo)

            nodo.setHijos(lista_hijos)

if __name__=="__main__":
    conexiones ={
        'Malaga':{'Salamanca','Madrid','Barcelona'},
        'Sevilla':{'Santiago','Madrid'},
        'Granada':{'Valencia'},
        'Valencia':{'Barcelona'},
        'Madrid':{'Salamanca','Sevilla','Malaga','Barcelona','Santander'},
        'Salamanca':{'Malaga','Madrid'},
        'Santiago':{'Sevilla','Santander','Barcelona'},
        'Santander':{'Santiago','Madrid'},
        'Zaragoza':{'Barcelona'},
        'Barcelona':{'Zaragoza','Santiago','Madrid','Malaga','Valencia'}
    }
    estado_inicial= 'Granada'
    solucion= 'Santiago'
    nodo_solucion = buscar_solucion_BFS(conexiones,estado_inicial,solucion)
    #mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.getPadre()!=None:
        resultado.append(nodo.getDatos())
        nodo = nodo.getPadre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print (resultado)

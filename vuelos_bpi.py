# Vuelos con busqueda de profundidad iterativa (DEPTH FIRST SEARCH) Recuersivo
from arbol import Nodo

def DFS_prof_iter(nodo,solucion):
    for limite in range(0,100):
        visitados=[]
        sol=buscar_solucion_DFS_Rec(nodo,solucion,visitados,limite)
        if sol!= None:
            return sol

def buscar_solucion_DFS_Rec(nodo_inicial, solucion,visitados,limite):
   if limite>0:
        visitados.append(nodo_inicial.getDatos())
        if nodo_inicial.getDatos()== solucion:
            #Solcuion encontrada
            return nodo_inicial
        else:
            #expandir nodos hijos
            dato_nodo= nodo_inicial.getDatos()
            lista_hijos=[]
            for un_hijo in conexiones[dato_nodo]:
                hijo=Nodo(un_hijo)
                lista_hijos.append(hijo)
                if (not hijo.getDatos() in visitados):
                    lista_hijos.append(hijo)
            nodo_inicial.setHijos(lista_hijos)

            for nodo_hijo in nodo_inicial.getHijos():
                if (not nodo_hijo.getDatos() in visitados):
                    # llamada recursiva
                    sol=buscar_solucion_DFS_Rec(nodo_hijo,solucion,visitados,limite-1)
                    if sol!= None :
                        return sol

   return None



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
    estado_inicial= 'Malaga'
    solucion= 'Santiago'
    nodo_inicial = Nodo(estado_inicial)
    #mostrar resultado
    nodo=DFS_prof_iter(nodo_inicial,solucion)
    if nodo!=None:
        resultado=[]
        while nodo.getPadre()!=None:
            resultado.append(nodo.getDatos())
            nodo = nodo.getPadre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print (resultado)
    else:
        print ('Solucion no encontrada')

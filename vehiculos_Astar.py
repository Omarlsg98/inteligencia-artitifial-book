# Seleccionar la mejor combinacion de proveedores con busqueda A*

from arbol import Nodo

# Incompleto

def buscar_solucion_UCS(informacion, estado_inicial):
        depth = 0;
        nodos_visitados=[]
        nodos_frontera=[]
        nodo_inicial=Nodo(estado_inicial)
        nodo_inicial.setCoste(0)
        nodos_frontera.append(nodo_inicial)
        while (depth!=3) and len(nodos_frontera)!=0:
            #Ordenar la lista de nodos frontera
            nodos_frontera=sorted(nodos_frontera,key= lambda Nodo: Nodo.calcularTotalCost(informacion))
            #extraer nodo y añadirlo a visitados
            nodo=nodos_frontera.pop(0)
            nodos_visitados.append(nodo)
            #expandir nodos hijos (empresas restantes)
            dato_nodo= nodo.getDatos()
            lista_hijos=[]
            if dato_nodo=="inicio":
                for i in range(4):
                    hijo=Nodo("Empresa" + (i+1))
                    #añadir el coste al nodo
                    coste = informacion[i][depth]
                    hijo.setCoste(nodo.getCoste()+coste)
                    lista_hijos.append(hijo)

                if (not hijo.enLista(nodos_visitados)):
                    #si no ha sido visitado y esta en la lista de frontera
                    # lo sustituimos con el nuevo valor de coste si es menor
                    if (hijo.enLista(nodos_frontera)):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.getCoste()> hijo.getCoste():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)

                nodo.setHijos(lista_hijos)


if __name__=="__main__":
    informacion=[
         [20,30,20,40],
         [50,50,40,50],
         [60,55,50,60],
         [100,80,60,70]
    ]
    estado_inicial= 'inicio'
    nodo=buscar_solucion_UCS(informacion,estado_inicial)
    #mostrar resultado
    print (nodo.mostrarRecorrido(estado_inicial))
    print ('Coste: '+str(nodo.getCoste()))



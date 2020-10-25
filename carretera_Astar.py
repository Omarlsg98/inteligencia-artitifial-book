# Viajes en carretera con busqueda A*
from arbol import Nodo
from math import sin,cos,acos
#
# def compara(x,y):
#     c1 =calcularCosteTotalCiudad(x)
#     c2=calcularCosteTotalCiudad(y)
#     return c1-c2
# Todo se compara dentro de la misma clase de nodo


def buscar_solucion_UCS(conexiones, estado_inicial,solucion):
        solucionado= False
        nodos_visitados=[]
        nodos_frontera=[]
        nodo_inicial=Nodo(estado_inicial)
        nodo_inicial.setCoste(0)
        nodos_frontera.append(nodo_inicial)
        while (not solucionado) and len(nodos_frontera)!=0:
            #Ordenar la lista de nodos frontera
            nodos_frontera=sorted(nodos_frontera,key= lambda Nodo: Nodo.calcularTotalCost(coord,solucion))
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
                    #añadir el coste al nodo
                    coste = conexiones[dato_nodo][un_hijo]
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
    conexiones ={
        'Malaga':{'Granada':125,'Madrid':513},
        'Sevilla':{'Madrid':513},
        'Granada':{'Malaga':125,'Madrid':423,'Valencia':491},
        'Valencia':{'Granada':491,'Madrid':356,'Zaragoza':309,'Barcelona':346},
        'Madrid':{'Salamanca':203,'Sevilla':514,'Malaga':513,'Granada':423,'Barcelona':603,'Santander':437,'Valencia':356,'Zaragoza':313,'Santiago':599},
        'Salamanca':{'Santiago':390,'Madrid':203},
        'Santiago':{'Salamanca':390,'Madrid':599},
        'Santander':{'Madrid':437,'Zaragoza':394},
        'Zaragoza':{'Barcelona':296,'Valencia':309,'Madrid':313},
        'Barcelona':{'Zaragoza':296,'Madrid':603,'Valencia':346}
    }
    coord={
         'Malaga':(36.43,-4.24),
        'Sevilla':(37.23,-5.59),
        'Granada':(37.11,-3.35),
        'Valencia':(39.28,-0.22),
        'Madrid':(40.23,-3.41),
        'Salamanca':(40.57,-5.40),
        'Santiago':(42.52,-8.33),
        'Santander':(43.28,-3.48),
        'Zaragoza':(41.39,-0.52),
        'Barcelona':(41.23,2.11)
    }
    estado_inicial= 'Malaga'
    solucion= 'Santiago'
    nodo=buscar_solucion_UCS(conexiones,estado_inicial,solucion)
    #mostrar resultado
    print (nodo.mostrarRecorrido(estado_inicial))
    print ('Coste: '+str(nodo.getCoste()))



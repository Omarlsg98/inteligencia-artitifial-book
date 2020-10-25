# VRP con algoritmo voraz de los ahorros (Clarke y Wrigth)

import math
from operator import itemgetter

def distancia(coord1,coord2):
    lat1=coord1[0]
    lat2=coord2[0]
    lon1=coord1[1]
    lon2=coord2[1]
    return math.sqrt((lat1-lat2)**2+(lon1-lon2)**2)

def en_ruta(rutas,ciudad):
    ruta=None
    for r in rutas :
        if ciudad in r:
            ruta=r
    return ruta

def peso_ruta(ruta):
    total=0
    for ciudad in ruta:
        total+=pedidos[ciudad]
    return total

def vrp_voraz():
    #Calcular ahorros
    savings={}
    for c1 in coord:
        for c2 in coord:
            if c1!=c2:
                if not (c2,c1)in savings:
                    distanciaC1C2=distancia(coord[c1],coord[c2])
                    distanciaC1Almacen= distancia(coord[c1],almacen)
                    distanciaC2Almacen= distancia(coord[c2],almacen)
                    savings[c1,c2]=distanciaC1Almacen+distanciaC2Almacen-distanciaC1C2 # funcion para hallar los ahorros
    #ordenar ahorros
    savings = sorted(savings.items(), key =itemgetter(1), reverse= True)

    #costruir rutas
    rutas=[]
    for parCiudades, ahorro in savings:
        rutaC1= en_ruta(rutas,parCiudades[0]) # posicion 0 ciudad c1 posicion 1 ciudadd c2
        rutaC2= en_ruta(rutas,parCiudades[1])
        if rutaC1==None and rutaC2==None: ##clasifica si esta uno en ruta, ninguno o ambos
            #ninguna de las dos tiene ruta. la creamos
            nuevaRuta=[parCiudades[0],parCiudades[1]]
            if peso_ruta(nuevaRuta)<=max_carga:
                rutas.append(nuevaRuta)
        elif rutaC1!=None  and rutaC2==None:
            #ciudad 1 esta en ruta, pero ciudad 2 no, por lo cual agregamos c2 a la ruta de c1
            if rutaC1[0]==parCiudades[0]: #si la ciudad esta en el primer puesto
                if peso_ruta(rutaC1)+peso_ruta([parCiudades[1]])<=max_carga:
                    rutas[rutas.index(rutaC1)].insert(0,parCiudades[1]) ##añade al principio de la ruta la ciudad 2
            elif rutaC1[len(rutaC1)-1]==parCiudades[0]: #Ciudad esta en el ultimo puesto
                 if peso_ruta(rutaC1)+peso_ruta([parCiudades[1]])<=max_carga:
                    rutas[rutas.index(rutaC1)].append(parCiudades[1]) ##añade al final de la ruta la ciudad 2
        elif rutaC1==None  and rutaC2!=None:
            #ciudad 1 no esta en ruta, pero ciudad 2 si, por lo cual agregamos c1 a la ruta de c2
            if rutaC2[0]==parCiudades[1]: #si la ciudad esta en el primer puesto
                if peso_ruta(rutaC2)+peso_ruta([parCiudades[0]])<=max_carga:
                    rutas[rutas.index(rutaC2)].insert(0,parCiudades[0]) ##añade al principio de la ruta la ciudad 2
            elif rutaC2[len(rutaC2)-1]==parCiudades[1]: #Ciudad esta en el ultimo puesto
                 if peso_ruta(rutaC2)+peso_ruta([parCiudades[0]])<=max_carga:
                    rutas[rutas.index(rutaC2)].append(parCiudades[0]) ##añade al final de la ruta la ciudad 2
        elif rutaC1!=None  and rutaC2!=None and rutaC1!=rutaC2: # ambas ciudades estan en una ruta, se intentan conectar por las puntas
            if rutaC1[0]==parCiudades[0] and  rutaC2[len(rutaC2)-1]==parCiudades[1]:
                 if peso_ruta(rutaC2)+peso_ruta(rutaC1)<=max_carga:
                    rutas[rutas.index(rutaC2)].extend(rutaC1)
                    rutas.remove(rutaC1)
            elif rutaC2[0]==parCiudades[1] and  rutaC1[len(rutaC1)-1]==parCiudades[0]:
                 if peso_ruta(rutaC2)+peso_ruta(rutaC1)<=max_carga:
                    rutas[rutas.index(rutaC1)].extend(rutaC2)
                    rutas.remove(rutaC2)
    return rutas


if __name__=="__main__":
    pedidos={
         'Malaga':10,
        'Sevilla':13,
        'Granada':7,
        'Valencia':11,
        'Madrid':15,
        'Salamanca':8,
        'Santiago':6,
        'Santander':7,
        'Zaragoza':8,
        'Barcelona':14
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
    almacen=(40.23,-3.40)
    max_carga=40
    #Mostrar resultados
    rutas =vrp_voraz()
    for ruta in rutas:
        print (ruta)



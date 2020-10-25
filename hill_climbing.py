# Travelling Salesman Problem (recorrer todas las ciudades) con hill climbing

import math
import random

def distancia(coord1,coord2):
    lat1=coord1[0]
    lat2=coord2[0]
    lon1=coord1[1]
    lon2=coord2[1]
    return math.sqrt((lat1-lat2)**2+(lon1-lon2)**2)


def evalua_ruta(ruta):
    total=0
    for i in range(0,len(ruta)-1):
        ciudad1= ruta[i]
        ciudad2=ruta[i+1]
        total= total+distancia(coord[ciudad1],coord[ciudad2])
    ciudad1= ruta[i+1]
    ciudad2=ruta[0]
    total= total+distancia(coord[ciudad1],coord[ciudad2])
    return total

def hill_climbing():
    #Crear ruta inicial aleatoria
    ruta=[]
    for ciudad in coord:
        ruta.append(ciudad)
    random.shuffle(ruta)

    mejora = True
    while mejora:
        mejora=False
        dist_actual = evalua_ruta(ruta)

        #buscar y evaluar vecino
        for i in range(0,len(ruta)):
            if mejora: # si se encuentra mejora, que no se siga ejecutando el for loop
                break
            for j in range(0,len(ruta)):
                if i !=j:
                    rutaTmp= ruta[:] #Clonar la ruta en una temporal
                    ciudadTmp= rutaTmp[i] # se intercambian ciudades en orden
                    rutaTmp[i]=rutaTmp[j]
                    rutaTmp[j]=ciudadTmp
                    dist = evalua_ruta(rutaTmp)
                    if dist<dist_actual:
                        #Se encontro a un mejor vecino
                        mejora = True
                        ruta =rutaTmp[:]
                        break
    return ruta


if __name__=="__main__":

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
    #Mostrar resultados
    ruta =hill_climbing()
    print (ruta)
    print ('Distancia total: '+str(evalua_ruta(ruta)))



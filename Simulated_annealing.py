# Travelling Salesman Problem (recorrer todas las ciudades) contemplado simulado

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

def simulated_annealing(ruta):
    T=20 # la funcion de evaluacion es la temperatura, por lo cual es un algoritmo metaheuristico ( no depende del problema)
    T_min=0
    velocidad_enfriamiento=100

    while T>T_min:

        dist_actual = evalua_ruta(ruta)
        for i in range(1,velocidad_enfriamiento):
            #intercambiamos dos ciudades aleatoriamente
            i=random.randint(0,len(ruta)-1)
            j=random.randint(0,len(ruta)-1)
            rutaTmp= ruta[:] #Clonar la ruta en una temporal
            ciudadTmp= rutaTmp[i] # se intercambian ciudades en orden
            rutaTmp[i]=rutaTmp[j]
            rutaTmp[j]=ciudadTmp
            dist = evalua_ruta(rutaTmp)
            delta=dist_actual-dist
            if dist<dist_actual:
                #Se encontro a un mejor vecino
                ruta =rutaTmp[:]
                break
            elif random.random()< math.exp(delta/T):
                ruta =rutaTmp[:]
                break
        #enfriamos linealmente T
        T-=0.001
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
    #Crear ruta inicial aleatoria
    ruta_inicial=[]
    for ciudad in coord:
        ruta_inicial.append(ciudad)
    random.shuffle(ruta_inicial)
    ruta =simulated_annealing(ruta_inicial)
    print (ruta)
    print ('Distancia total: '+str(evalua_ruta(ruta)))



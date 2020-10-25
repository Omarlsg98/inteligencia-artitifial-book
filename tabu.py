# Travelling Salesman Problem (recorrer todas las ciudades) con busqueda tabu

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

def busqueda_tabu(ruta):
    #Crear ruta inicial aleatoria
    mejor_ruta=ruta
    memoria_tabu= {}
    persistencia = 5 # numero de iteraciones que no se puede romper el tabu
    mejora= False
    iteraciones = 10

    while iteraciones>0:
        iteraciones-=1
        mejora = False
        dist_actual= evalua_ruta(ruta)
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
                    #Comprobar si el movimiento es tabu, se verifica ambas opciones de clave y si el valor es mayor a 0
                    tabu =False
                    if rutaTmp[i]+'_'+rutaTmp[j] in memoria_tabu:
                        if memoria_tabu[rutaTmp[i]+'_'+rutaTmp[j]]>0:
                            tabu=True
                    if rutaTmp[j]+'_'+rutaTmp[i] in memoria_tabu:
                        if memoria_tabu[rutaTmp[j]+'_'+rutaTmp[i]]>0:
                            tabu=True

                    if dist<dist_actual:
                        if tabu:
                            #Comprobamos criterio de aspiracion
                            #aunque sea movimiento tabu
                            if evalua_ruta(rutaTmp)<evalua_ruta(mejor_ruta):
                                mejor_ruta=rutaTmp[:]
                                ruta=rutaTmp[:]
                                #Almacenamos en memoria tabu
                                memoria_tabu[rutaTmp[i]+'_'+rutaTmp[j]]= persistencia
                                mejora=True
                                break
                        else:
                            #Se encontro a un mejor vecino
                            mejora = True
                            ruta =rutaTmp[:]
                            if evalua_ruta(rutaTmp)<evalua_ruta(mejor_ruta):
                                mejor_ruta=ruta[:]
                            #almacenamos en memoria tabu
                            memoria_tabu[rutaTmp[i]+'_'+rutaTmp[j]]= persistencia
                            break
        #rebajar persistencia a los movimientos tabu
        if len(memoria_tabu)>0:
            for key in memoria_tabu:
                if memoria_tabu[key]>0:
                    memoria_tabu[key]-=1

    return mejor_ruta


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
    ruta =busqueda_tabu(ruta_inicial)
    print (ruta)
    print ('Distancia total: '+str(evalua_ruta(ruta)))



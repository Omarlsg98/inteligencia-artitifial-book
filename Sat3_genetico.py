import math
import random

def poblacion_inicial(max_poblacion,num_vars):
    # crear poblacion inicial aleatorio
    poblacion=[]
    for i in range(max_poblacion):
        gen=[]
        for j in range(num_vars):
            if random.random()>0.5:
                gen.append(1)
            else:
                gen.append(0)
        poblacion.append(gen[:])
    return poblacion
def adaptacion_3sat(gen, solucion):
    #contar clausulas correctas
    n=3
    cont = 0
    clausulaOk= True
    for i in range(len(gen)): #como es sat 3, revisa de a 3 variables y si las 3 coinciden con la solucion la clausula esta bien
        n=n-1
        if (gen[i]!=solucion[i]):
            clausulaOk=False
        if n==0:
             if clausulaOk:
                 cont=cont+1
             n=3
             clausulaOk=True
    if n>0:
        if clausulaOk:
            cont+=1
    return cont
def evalua_poblacion(poblacion,solucion):
    #evalua todos los genes de la poblacion
    scores_adaptacion= []
    for i in range(len(poblacion)):
        scores_adaptacion.append(adaptacion_3sat(poblacion[i],solucion))
    return scores_adaptacion

def seleccion(poblacion,solucion):
    puntajesAdaptacion = evalua_poblacion(poblacion,solucion)
    #suma de todas las puntuaciones
    total=0
    for i in range(len(puntajesAdaptacion)):
        total+=puntajesAdaptacion[i]
    #Escogemos dos elementos
    #Se escoge el elemento que supere en puntuacion acumulada random hasta él
    val1 =random.randint(0,total)
    val2 =random.randint(0,total)
    sum_sel=0 #acumulado
    for i in range(len(puntajesAdaptacion)):
        sum_sel+=puntajesAdaptacion[i]
        if sum_sel>=val1:
            gen1=poblacion[i]
            break
    sum_sel=0 #acumulado
    for i in range(len(puntajesAdaptacion)):
        sum_sel+=puntajesAdaptacion[i]
        if sum_sel>=val2:
            gen2=poblacion[i]
            break
    return gen1,gen2

def cruce(gen1,gen2):
    #Cruza 2 genes y obtiene 2 descendientes
    nuevo_gen1=[]
    nuevo_gen2=[]
    corte = random.randint(0,len(gen1))
    nuevo_gen1[0:corte]=gen1[0:corte]
    nuevo_gen1[corte:]=gen2 [corte:]
    nuevo_gen2[0:corte]=gen2[0:corte]
    nuevo_gen2[corte:]=gen1 [corte:]
    return nuevo_gen1,nuevo_gen2

def mutacion(prob,gen):
    #muta un gen con una probabilidad dada
    if random.random()<prob:
        cromosoma=random.randint(0,len(gen)-1)
        if gen[cromosoma]==0:
            gen[cromosoma]=1
        else:
            gen[cromosoma]=0
    return gen

def elimina_peores_genes (poblacion,solucion):
    #Elimina los dos peores genes
    puntajesAdaptacion = evalua_poblacion(poblacion,solucion)
    indiceMenor=puntajesAdaptacion.index(min(puntajesAdaptacion))
    del poblacion[indiceMenor]
    del puntajesAdaptacion[indiceMenor]
    indiceMenor=puntajesAdaptacion.index(min(puntajesAdaptacion))
    del poblacion[indiceMenor]
    del puntajesAdaptacion[indiceMenor]

def mejor_gen(poblacion,solucion):
    #Devuelve el mejor gen de la poblacion
     puntajesAdaptacion = evalua_poblacion(poblacion,solucion)
     indiceMayor=puntajesAdaptacion.index(max(puntajesAdaptacion))
     return poblacion[indiceMayor]

def algoritmo_genetico():
    max_iter=10
    max_poblacion=150
    num_cromosomas=10
    probabilidad_mutacion=0.1
    fin=False
    solucion = poblacion_inicial(1,num_cromosomas)[0]
    poblacion= poblacion_inicial(max_poblacion,num_cromosomas)

    iteraciones = 0
    while not fin:
        iteraciones+=1
        for i in range(int(len(poblacion)/2)):
            gen1 , gen2=seleccion(poblacion,solucion)
            nuevo_gen1, nuevo_gen2=cruce(gen1,gen2)
            nuevo_gen1=mutacion(probabilidad_mutacion,nuevo_gen1)
            nuevo_gen2=mutacion(probabilidad_mutacion,nuevo_gen2)
            poblacion.append(nuevo_gen1)
            poblacion.append(nuevo_gen2)
            elimina_peores_genes(poblacion,solucion)

        if max_iter<iteraciones:
            fin = True

    print("Solucion: "+ str(solucion))
    mejor= mejor_gen(poblacion,solucion)
    return mejor, adaptacion_3sat(mejor,solucion)

if __name__=='__main__':
    random.seed() #Da una base para generar los mismo numeros aleatorios
    mejor_gen=algoritmo_genetico()
    print("Mejor gen encontrado: "+ str(mejor_gen[0]))
    print("Puntaje de adaptacion (funcion adaptacion): "+ str(mejor_gen[1]))


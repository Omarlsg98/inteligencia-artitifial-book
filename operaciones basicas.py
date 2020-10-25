#Esto es un comentario

# print ("introduce edad:")
# edad=input()
# dias= int(edad)**2 #** exponente
# print("Tienes "+ str(dias)+ " dias") ##toca colocar explicitamente la conversion a str
# Stringmultiliea ="""
# esto
# tiene varias lineas
# """

# help(str)
# edad=int(input())
# if not edad>= 18 and True or False:
#     print("Es mayor de edad")
# elif 2>3:
#     #Operacion
#     print(edad)
# else:
#     print("no es mayor de edad")
# while edad<=18:
#     print("entra")

# personas=['Juan','Ana','Antonio']
# for p in personas:
#     print (p)
#
# for p in range(1,12,2):
#     print (p)


# numeros=['1','2','3','4']
# numeros.append('5')
# print(numeros)
# numeros.pop()
# print(numeros)
# print(numeros.index('3'))
# numeros.reverse()
# print(numeros)
# del numeros[:3] ## borra los elementos hasta la posicion 3
# print(numeros)
# numeros=['1','2','3','4']
# print(numeros[1:3])
# a =1,2,3 # esta es una tupla, es inmutable

# numeros=['1','2','3','3','4','5','4']
# conjunto_numeros= set(numeros) # un conjunto se crea con set, es desorganizado,  no tiene elementos repetidos
# print(conjunto_numeros)# se puede hacer operacion comunes de conjuntos '-' diferencia, | or , & and, ^ xor

##diccionarios
# ventas={'ratones':10, 'teclados':13, 'Cds':200, 'Dvds':150}
# print(ventas)
# ventas['impresoras']=2
# print(ventas)
# del ventas['impresoras']
# print(ventas)
# print(ventas['Cds'])
# print('teclados' in ventas)
#
# #recorrer diccionarios
# for clave in ventas.keys():
#     print (clave + " = "+str(ventas[clave]))
# for clave,valor in ventas.items(): ## o ventas.iteritems()
#     print (clave + " = "+str(valor)) ## estos valores son solo de visualizacion no estan referenciados

## FUNCIONES

#
# def miprimerfuncion (parametro1=10):
#     resultado = parametro1**2
#     return resultado
#
# print(miprimerfuncion(5))

##CLASES

# class Coordenada:
#     def __init__(self,x,y):
#         self.posx=x
#         self.posy= y
#     def ver(self):
#         return self.posx, self.posy
#     def mover (self,x,y):
#         self.posx=x
#         self.posy= y
# class Circulo:
#     def __init__(self,x,y,r):
#         Coordenada.__init__(self,x,y)
#         self.radio= r
#     def ver(self):
#         coord= Coordenada.ver(self)
#         return coord[0], coord[1],self.radio
#
#
#
# circulo=Circulo(20,20,5)
# print((circulo.ver()))
# from arbol import Nodo
#
#
# informacion=[
#         [20,50,60,100],
#          [30,50,55,80],
#          [20,40,50,60],
#          [40,50,60,70]
#     ]
#
# h=0
# asd = Nodo([3,1,0])
# yaescogidos= asd.getDatos()
# yaescogidos.sort()
# yaescogidos.reverse()
# for i in range(0,4):
#     temp = CopiarInfo(informacion)
#     for j in yaescogidos:
#         temp[i].pop(j)
#     print(min(temp[i]))
#     h+=min(temp[i])
import random

random.seed()
print(str(random.random()))

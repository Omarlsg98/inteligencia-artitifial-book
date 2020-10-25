from math import sin,cos , acos


class Nodo:

     def __init__(self,datos,hijos=None):
         self.datos = datos
         self.hijos = None
         self.padre = None
         self.coste = None
         self.setHijos(hijos)

     def setHijos(self,hijos):
         self.hijos=hijos
         if self.hijos!=None:
             for h in self.hijos:
                 h.padre= self

     def getHijos(self):
         return self.hijos

     def getPadre(self):
         return self.padre

     def setPadre(self, padre):
         self.padre = padre

     def setDatos(self,datos):
         self.datos= datos

     def getDatos(self):
         return self.datos

     def setCoste(self,coste):
         self.coste= coste

     def getCoste(self):
         return self.coste

     def igual(self,nodo):
         if self.getDatos()==nodo.getDatos():
             return True
         else:
             return False

     def enLista(self,listaNodos):
         enLaLista=False
         for n in listaNodos:
             if self.igual(n):
                 enLaLista=True
         return enLaLista

     def __str__(self):
         return str(self.getDatos())

     def mostrarRecorrido(self,estado_inicial):
         resultado=[]
         nodo = self
         while nodo.getPadre()!=None:
            resultado.append(nodo.getDatos())
            nodo = nodo.getPadre()
         resultado.append(estado_inicial)
         resultado.reverse()
         return resultado
     def calcularTotalCost(self,coord,solucion):
        #g(n) + h(n) para esta ciudad
        lat1= coord[self.getDatos()][0]
        lon1= coord[self.getDatos()][1]
        lat2= coord[solucion][0]
        lon2= coord[solucion][1]
        d = int (geodist(lat1,lon1,lat2,lon2))
        c1=self.getCoste()+d
        return c1
     def calcularTotalCost(self,informacion):
        #g(n) + h(n) para esta opcion de empresa
         nodo = self
         profundidad= 0
         while nodo.getPadre()!=None:
            profundidad+=1
            nodo = nodo.getPadre()
         h=0
         yaescogidos= self.getDatos()
         yaescogidos.sort()
         yaescogidos.reverse()
         for i in range(profundidad,4):
            temp = CopiarInfo(informacion)
            for j in yaescogidos:
                temp[i].pop(j)
            h+=min(temp[i])

         c1 = self.getCoste()+h
         return c1

def geodist(lat1,lon1,lat2,lon2):
    grad_rad= 0.01745329
    rad_grad=57.2577951
    longitud = lon1-lon2
    val = (sin(lat1*grad_rad)*sin(lat2*grad_rad))+\
          (cos(lat1*grad_rad)*cos(lat2*grad_rad)*cos(longitud*grad_rad))
    return (acos(val)*rad_grad)*111.32

def CopiarInfo (info):
    tempInfo = []
    for i in range(0,len(info)):
        rows = []
        for j in range(0,len(info[i])):
           rows.append(info[i][j])
        tempInfo.append(rows)
    return tempInfo

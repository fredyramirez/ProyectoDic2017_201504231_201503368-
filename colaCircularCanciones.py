import sys
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin'

from graphviz import Digraph


from NodoCola import Nodo_Cola
class Cola_Circular:
    def __init__(self):
        self.Primero = None
        self.Ultimo = None

    def vacia(self):
        return self.Primero == None

    def encolar(self, Nombre):
        nuevo = Nodo_Cola(Nombre)
        if self.vacia():
            self.Primero = nuevo
            self.Ultimo = nuevo
        else:
            self.Ultimo.setSiguiente(nuevo)
            self.Ultimo = self.Ultimo.getSiguiente()
            self.Ultimo.setSiguiente(self.Primero) #esto se lo agregue para provar si asi se convierte en circular
            #self.Ultimo.getSiguiente = self.Primero

    def desencolar(self):
        if self.vacia():
            return None
        elif self.Primero == self.Ultimo:
             self.Primero= None
             self.Ultimo = None
             sys.stdout.write("la cola esta vacia")

        else:
            self.Primero = self.Primero.getSiguiente()
            self.Ultimo.setSiguiente(self.Primero)

           # return self.nuevo
    def graficar(self):
        dot = Digraph( comment='Lista Circular de Canciones')
        #dot.node('I', 'Inicio')
       # dot.node('Final', 'NULL')
        actual = self.Primero
        i = 0
       # dot.edges(["I"+str(i)])
        #dot.node('p', actual.getNombreCola())
        while actual:
            dot.node(str(i), actual.getNombreCola())
            actual = actual.getSiguiente()
            i +=1
            if actual == self.Primero:
                break

            dot.edge(str(i-1),str(i),constraint='false')
        dot.edge(str(i-1),str(0),constraint='false')
        #dot.edge('p', 'L', constraint='false')
        dot.render(filename="imagen", directory="C:\Users\hp main\Desktop\pru", view=True, cleanup=True)

        print dot

        #este metodo es para verificar si esta insertando y eliminando correctamente


    def mostrarCola(self):
        if self.vacia():
            return None
        else:
            aux = self.Primero
            sys.stdout.write("INICIO")
            while aux:
                sys.stdout.write("<==>" + aux.getNombreCola())
                aux = aux.getSiguiente()
                if aux == self.Primero:
                    break
           # sys.stdout.write("<==>" + aux.getNombreCola())
            sys.stdout.write("<==>NULL")

a = Cola_Circular()

a.encolar("cancion1")
a.encolar("cancion2")
a.encolar("cancion3")
a.encolar("cancion4")
a.encolar("cancion5")
a.encolar("cancion6")
a.encolar("cancion7")
a.encolar("cancion8")
a.encolar("cancion9")
a.encolar("cancion6")
a.encolar("cancion7")
a.encolar("cancion8")
a.encolar("cancion9")

a.encolar("cancion11")




#a.desencolar()

a.graficar()
a.mostrarCola()

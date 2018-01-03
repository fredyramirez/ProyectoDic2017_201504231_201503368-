from NodoUsuario import NodoUsuario
import sys
from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin'

class Lista_Usuarios:

    def __init__(self):
        self.Inicio = None

    def vacia(self):
        return self.Inicio == None

    def InsertarFinal(self,Nombre,Contra):
        nuevo = NodoUsuario(Nombre,Contra)
        if self.vacia():
            self.Inicio = nuevo
        else:
            aux = self.Inicio
            while aux.getSiguiente() != None:
               aux = aux.getSiguiente()
            aux.setSiguiente(nuevo)
            nuevo.setAnterior(aux)
           # nuevo.Siguiente = self.Inicio # para convertirla en lista doble tabien tenemos que quitar esto
           # self.Inicio.Anterior = nuevo # y esto

    def recorrer(self):
        aux = self.Inicio
        while aux.getSiguiente() != None:
            aux = aux.getSiguiente()

# tengo que validar cuando el .siguiente es nulo sino me saldra error
    def login(self,Nombre,Contra):
        aux = self.Inicio
        while aux.getSiguiente() != None:
            if aux.getNombreUsuario() == Nombre and aux.getContraUsuario() == Contra:
                return  True
            else:
                return False

    def graficar(self):
        dot = Digraph(comment='Lista de Usuarios')
        actual = self.Inicio
        i = 0
        while actual  != None:
            dot.node(str(i),actual.getNombreUsuario())
            actual = actual.getSiguiente()
            i += 1
            if actual!=None:
                dot.edge(str(i-1),str(i),constraint='false')
                dot.edge(str(i) , str(i-1), constraint='false')

        dot.render(filename="imagen", directory="C:\Users\hp main\Desktop\pru", view=True, cleanup=True)
        print dot

    def mostrarUsuario(self):
        if self.vacia():
            sys.stdout.write("<==>NULL")
        else:
            aux = self.Inicio
            sys.stdout.write ("INICIO")
            while aux != None:
                sys.stdout.write ("<==>" +  aux.getNombreUsuario())
                aux = aux.getSiguiente()
            sys.stdout.write ("<==>NULL")


A = Lista_Usuarios()
A.InsertarFinal("primero","primero")
A.InsertarFinal("segundo","segundo")
A.InsertarFinal("cuarto","cuarto")
A.InsertarFinal("quinto","quinto")
A.InsertarFinal("sexto","sexto")
A.InsertarFinal("septimo","septimo")
A.InsertarFinal("octavo","octavo")
A.InsertarFinal("noveno","noveno")
A.InsertarFinal("diez","diez")
A.InsertarFinal("once","once")
A.InsertarFinal("doce","doce")
A.InsertarFinal("trece","trece")



A.login("primero","primero")

A.graficar()
A.mostrarUsuario()




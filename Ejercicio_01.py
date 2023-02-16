#1. Crea un programa en Python que simule una lista de compras. El programa debe
# permitir al usuario agregar productos al final de la lista, eliminar productos
# del inicio de la lista y mostrar todos los productos en la lista en orden de compra.


class Nodo:
    def __init__(self,data):
        self.data = data
        self.siguiente = None

class ListaSimpleEnlazada:   
    def __init__(self):
        self.primero = None
        self.ultimo = None    
    #Crear una función: para saber si mi lista esta vacía.
    def vacia(self):
        return self.primero == None
    #Agregar al final 
    def agregar_final(self,data): #la funcion recibe dos parametros
        if self.vacia():
            self.primero =  self.ultimo = Nodo(data) 
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(data) 
    #Mostrar elementos
    def mostrar(self):
        aux = self.primero #Asignando a la variable aux el valor del primer nodo
        while aux != None:
            print(aux.data) #Imprime dato del nodo actual, almacenando en la variable aux
            aux = aux.siguiente #Asiganamos a la varibale aux el nodo siguiente     
    #Eliminar al inicio
    def eliminar_inicio(self):
        self.primero = self.primero.siguiente        
try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaSimpleEnlazada() 
        while opcion != 4:
            print("""\n\tLISTA DE COMPRAS
1. Agregar Compra al Final 
2. Eliminar Compra al Inicio
3. Mostrar Toda la Compra 
4. Salir""")
            opcion = int(input("Ingrese su opcion: "))
            if opcion == 1:
                data = input("¿Qué compra hizo? ")
                lista.agregar_final(data)
            elif opcion == 2:
                lista.eliminar_inicio()
            elif opcion == 3:
                lista.mostrar()
            elif opcion == 4:
                print("Fin")
            else:
                print("Ingrese una de las opciones de la lista: ") 
except Exception as e:
    print(e)       
            

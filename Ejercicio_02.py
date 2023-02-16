#2. Crea un programa en Python que mantenga un historial de tareas pendientes. 
# El programa debe permitir al usuario agregar una tarea al inicio de la lista,
# eliminar una tarea del final de la lista y mostrar todas las tareas en la lista
# en orden inverso al que se agregaron. Además, el programa debe contar la 
# cantidad total de tareas en la lista y mostrar ese número al usuario.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
class ListaDoble:   
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0 
    def vacio(self):
        return self.primero == None
    def agregar_principio(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = None
            self.primero = aux
        self.size += 1 
    def eliminar_final(self):
        if self.vacio():
            print("Lista vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1            
    def recorrer_inicio(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente        
    def contar(self):
        if self.primero == None:
            vacia1 = 0
        else:
            vacia1 = self.size
        return vacia1
try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaDoble()
        while opcion != 5:
            print("""\n\tLISTA DE TAREAS PENDIENTES: 
1. Agregar Tarea al Inicio de la Lista 
2. Eliminar Tarea al Final de la lista
3. Mostrar Tareas de la lista 
4. Cuantas Tareas Hay?
5. Salir""")
            opcion = int(input("\nIngrese su opcion: "))
            
            if opcion == 1:
                data = input("\nAgregue Su Tarea: ")
                lista.agregar_principio(data)
            elif opcion == 2:
                lista.eliminar_final()
            elif opcion == 3:
                print("\nSus tareas pendientes son de final al principio...\n")
                lista.recorrer_inicio()
            elif opcion == 4:
                print(f"Tienes {lista.contar()} Tareas pendientes")
            elif opcion == 5:
                print("Fin del programa")
            else:
                print("Ingrese una de las opciones de la lista: ") 
except Exception as e:
    print(e)     

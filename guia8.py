import random
from queue import LifoQueue as Pila
from queue import Queue as Cola
#generar numeros alazar entre un intervalo de numeros
#p =Pila()
#def pilaDeNumeros()

#p = Pila() #Crea una pila
#p.put(1)  #Apila un 1
#elemento = p.get() #Desapila
#p.empty()#Devuelve true si la pila esta vacia.

#1
def apilar(cantidad:int, desde:int, hasta:int)->Pila:
    p = Pila()
    i = 0
    while i < cantidad:
        p.put(random.randint(desde, hasta))
        i = i + 1
    return p
#Guardamos la funcion en una variable
pila_generada = apilar(4, 2, 8)

print(list(pila_generada.queue))

#2
def cantidad_elementos(p: Pila) -> int:
    aux = Pila()
    contador = 0

    # Paso 1: Pasar todos los elementos de p a aux
    while not p.empty():#Con el bucle While not estoy diciendo basicamente, mientras no pase esto, quiero que hagas tal cosa.
        elemento = p.get()#estoy guardando cada elemento  que estoy desapilando, en la variable "Elemento"
        aux.put(elemento)#y aca basicamente le estoy agregando los elementos que estoy desapilando
        contador += 1#por cada vez que elemino y vuelvo a agregar un elemento cuento 1

    # Paso 2: Restaurar la pila original
    while not aux.empty():
        p.put(aux.get())#Quiero que a la pila original le agregues los elementos que le habias sacado, y guardado en la pila aux
    #es como el juego de las torres de Hanoish, necesitas apilar las cosas en otra pila para guardar los elementos, y luego lo volves a 
    return contador

pila_nueva = cantidad_elementos([1,2,3,4,5,5])
print(list(pila_nueva.queue))


#3 
def buscar_elmaximo(p:Pila[int])->int:
    aux = Pila()
    elementoMayor = 0

    while not p.empty():
        paraComparar = p.get()
        aux.put(paraComparar)
        if elementoMayor < paraComparar:
            elementoMayor = paraComparar

    #y Ahora lo mismo vuelvo a reapilar la pila original, "SACANDOLE LOS ELEMENTOS A LA PILA AUXILIAR":
    while not aux.empty():
        p.put(aux.get())

    return elementoMayor

#print
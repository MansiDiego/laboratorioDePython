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
    while not p.empty():
        elemento = p.get()
        aux.put(elemento)
        contador += 1

    # Paso 2: Restaurar la pila original
    while not aux.empty():
        p.put(aux.get())

    return contador
#REPASAR Y SEGUIR HASTA EL EJERCICIO  2 "COLAS", Y LUEFO FINALIZAR EL EJERCICIO 2 DE P7
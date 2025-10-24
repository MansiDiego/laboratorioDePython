#Para laburar con arrays importamos el modulo:
from array import *

#a: array = array(typecode, [inicializers])
a: array = array("i",[10,20,30])
print(a)    
"""
---Arreglos Python--
Operaciones basicas sobre arrays.
Sea a un array:

a[i] −→ obtiene el valor del elemento i de a
a[i] = x −→ asigna x en el elemento i de a
a.append(x) −→ anade x como nuevo elemento de a
a.remove(x) −→ elimina el primer elemento en a que coincida con x
a.index(x) −→ obtiene la posicion donde aparece por primera vez el elemento x
a.count(x) −→ devuelve la cantidad de apariciones del elemento x
a.insert(p,x) −→ inserta el elemento x delante de la posicion p

"""

"""
--Listas en python--
¿Como se declaran?

▶ variableLista = [] #lista vacia
▶ otraVariableLista = list() #lista vacia
▶ otraVariable = [1, 2, True, "Hola", 5.8]
▶ unaMas = list([4, 9, False, "texto"])

#Comparte las mismas operaciones que los arrays:
Sea a una lista:
a[i] −→ obtiene el valor del elemento en posicion i de a
a[i] = x −→ asigna x en el elemento i de a
a.append(x) −→ anade x como nuevo elemento de a
a.remove(x) −→ elimina el primer elemento en a que coincida con x
a.index(x) −→ obtiene la posicion donde aparece por primera vez el elemento x
a.count(x) −→ devuelve la cantidad de apariciones del elemento x
a.insert(p, x) −→ inserta el elemento x delante de la posicion p


"""

#DIFERENTES FORMAS DE RECORRER LISTAS:

#with for i in range(funcion range para el rango en el que queremos que recorra)
def recorriendo(a:list[int])->list[int]:
    for i in range(len(a)):
        print(a[i])
print(recorriendo([20,19,21,22,60]))

#with for i in
def recorriendobis(a:list[int])->list[int]:
    for edad in a:
        print (edad)
print(recorriendobis([19,20,21]))
#with while
def recorriendowithWhile(s:list[int])->list[int]:
    i=0
    while i < len(s):
        res = print(s[i])
        i+=1
    return res
print(recorriendowithWhile([18,19,20,21,22,23]))

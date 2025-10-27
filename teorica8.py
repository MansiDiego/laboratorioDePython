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


##EJEMPLO DE DOCSTRING
def printar(s: str) -> str:
    """
    Esta función recibe un parámetro s de tipo str.
    Se espera que printee 'Hola Mundo' (o lo que se le pase como texto).

    Parámetros:
        s (str): texto que se desea mostrar por pantalla.

    Retorna:
        str: el mismo texto recibido.
    """
    print(s)
    return s

print(printar("hola mundo"))
print(printar.__doc__)

##Debugging:
def suma(a, b):
    total = a + b
    return total

x = 5
y = 3
resultado = suma(x, y)
print(resultado)


"""
Manejo de Archivos
archivo = open(”PATH AL ARCHIVO”, MODO, ENCODING)
▶ Algunos de los modos posibles son: escritura (w), lectura (r), texto
(t - es el default)
▶ El encoding se refiere a como esta codificado el archivo: UTF-8 o
ASCII son los mas frecuentes.
Operaciones basicas
▶ Lectura de contenido:
▶ read(size): Lee y devuelve una cantidad especıfica de caracteres o
bytes del archivo. Si no se especifica el tamano, se lee el contenido
completo.
▶ readline(): Lee y devuelve la siguiente lınea del archivo.
▶ readlines(): Lee todas las lıneas del archivo y las devuelve como una
lista.
▶ Escritura de contenido:
▶ write(texto): Escribe un texto en el archivo en la posicion actual del
puntero. Si el archivo ya contiene contenido, se sobrescribe.
▶ writelines(lineas): Escribe una lista de lıneas en el archivo. Cada lınea
debe terminar con un salto de lınea explıcito.
"""
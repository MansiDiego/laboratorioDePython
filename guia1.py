import math #Importamos la libreria para usar algunas funciones


#1
def imprimir_hola_mundo():
    return("hola mundo")

#1.2. imprimir_un_verso(): que imprima un verso de una canción que vos elijas, respetando los saltos de línea mediante
#el caracter \n."""
def imprimir_un_verso():
    return("Nobody ever loved me like she does \nOh, she does, yeah, she does\nAnd if somebody loved me like she does\nOh, she does, yes, she does")
print(imprimir_un_verso)

#1.3. raizDe2(): que devuelva la raíz cuadrada de 2 con 4 decimales. Ver función round"""
raizDe2 = 1.41421356237
print(round(raizDe2, 4)) #El primer parametro de la funcion round es sobre el numero que queremos redondear, y el 2do argumento del parametro le indica la cantidad de decimales que queremos
"""round(x) → redondea al entero más cercano.
Pero si el número está justo en la mitad (termina en .5), Python aplica una regla especial llamada round half to even
 (redondeo al par más cercano)."""

#1.4 factorial_de_dos()
def factorial_2 ():
    return  (2 * 1)

print(factorial_2())

#1.5 perimetro: que devuelva el perímetro de la circunferencia de radio 1. Utilizar la biblioteca math mediante el comando
#Forma de importar funciones: cuando queremos usar alguna funcion de la libreria lo que hacemos es: libreria.funcion(), por ejemplo math.round()
def problema_perimetro()-> float:
    return(2 * math.pi)
print(problema_perimetro())

#Ejercicio 2. Definir las siguientes funciones y procedimientos con parámetros:
"""1. problema imprimir_saludo (in nombre: String) {
requiere: { T rue }
asegura: {imprime “Hola < nombre >"por pantalla}
}
"""
def imprimir_saludo(nombre: str) -> None:
    res = nombre
    return "hola" + res
imprimir_saludo("mateo")
#Las funciones estan separadas y aisladas del bloque principales, a menos que las llamemos

##ACA ARRANCA LO DE LA CLASE PARA COMPLETAR LA GUIA:
#Para ejecutar una funcion por repl le metemos import el nombre de la pagina en la que estemos parado(en este caso labo1) por ejemplo seria labo1.imprimir_hola_mundo"""
#observaciones: primero debo entrar al archivo con import "nombre del archivo", una vez que entro al archivo le paso "nombre del archivo"."nombre de la funcion"quit
#observación no se puede recargar con el interprete, por lo tanto hay que volver a importar el archivo

#para calcular el resto usamos "%", por ejemplo para calcular el resto de 10%2 me daria 0.

#2.2 ME FALTA ESTE EJERCICIO...


#2.3 que convierta la temperatura de grados Farenheit a grados Celcius.
def farenheit_a_celcius(temp: int) -> int:
    res = (temp - 32) * 5
    res2= res/9
    return res2
print(farenheit_a_celcius(100)) 

#2.4 Imprimir dos veces el estribillo de una canción
def estribillo ():
    resultado = 2 * "se eriza la bandera nacional\n"
    return resultado
print(estribillo())

#Ejercicio 2.5 definir las sig funcion:
def es_multiplo_de(n:int, m:int) ->bool:
    return n % m == 0
print(es_multiplo_de(10,2))

#Ejercicio 2.6 indicar si el numero es par, usando la funcion multiplode

def es_par(x: int) -> bool:
    res = es_multiplo_de(x, 2)
    return res
print(es_par(3))

#Ejercicio 2.7 cantidad de pizzas FALTA TERMINAR
def cantidad_pizzas():

#EJercicio 3 para pedir la longitud nombre de la variable len(nombre)

def es_nombre_largo (nombre: str)->bool:
    return len(nombre) >= 3 and len(nombre) <=8

print(es_nombre_largo("mansilla"))


#Ejercicio 5.1
def devolver_el_doble(numero: int) -> int:
    res : int

    if numero % 2 == 0:
        res = 2 * numero
    else:
        res= numero

    return res

print(devolver_el_doble(4))

#RECORDAR GUARDAR LA VARIABLE PARA LOS CONDICIONALES.



#Ejercicio 6.2 implementar usando while: escribir una funcion que imprima los numeros pares del 10 y el 40.
def paresdel10al40()->None:
    i: int = 10
    while i<=40:
        print(i)
        i= i + 2

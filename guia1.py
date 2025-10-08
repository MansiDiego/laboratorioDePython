"""Ejercicio 1. Definir las siguientes funciones y procedimientos:
1. problema imprimir_hola_mundo () {
requiere: { T rue }
asegura: { imprime “¡Hola mundo!"por consola}
}"""

#1
print("Hello world!")

"""2. imprimir_un_verso(): que imprima un verso de una canción que vos elijas, respetando los saltos de línea mediante
el caracter \n."""

print("Nobody ever loved me like she does \nOh, she does, yeah, she does\nAnd if somebody loved me like she does\nOh, she does, yes, she does")

"""3. raizDe2(): que devuelva la raíz cuadrada de 2 con 4 decimales. Ver función round"""

raizDe2 = 1.41421356237
print(round(raizDe2, 4)) #El primer parametro de la funcion round es sobre el numero que queremos redondear, y el 2do argumento del parametro le indica la cantidad de decimales que queremos
"""round(x) → redondea al entero más cercano.
Pero si el número está justo en la mitad (termina en .5), Python aplica una regla especial llamada round half to even
 (redondeo al par más cercano)."""

"""4. factorial_de_dos()
problema factorial_2 () : Z {
requiere: { T rue }
asegura: {res = 2!}
}"""

factorial_2 = (2 * 1)
print(factorial_2)

"""5. perimetro: que devuelva el perímetro de la circunferencia de radio 1. Utilizar la biblioteca math mediante el comando
import math y la constante math.pi
problema perimetro () : R {
requiere: { T rue }
asegura: {res = 2 x π }
}
"""
import math
perimetro =  2 * math.pi
print(perimetro)

#Ejercicio 2. Definir las siguientes funciones y procedimientos con parámetros:
"""1. problema imprimir_saludo (in nombre: String) {
requiere: { T rue }
asegura: {imprime “Hola < nombre >"por pantalla}
}
"""

def imprimir_saludo(nombre: str) -> None:
    print(f"hola {nombre}")

imprimir_saludo("mateo")
#Las funciones estan separadas y aisladas del bloque principales, a menos que las llamemos



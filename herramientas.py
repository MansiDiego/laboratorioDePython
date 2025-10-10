#Division de enteros(redondea hacia abajo): 
divEntera= 7//2
print(divEntera)

#division que devuelve siempre un tipo de dato float(valor exacto):
divFloat = 7/2
print(divFloat)

#para redondear para arriba esta la funcion de la libreria importadad de math: "math.ceil(variable que queremos redondear)"
import math
def redondea_para_arriba(res:float)->int: 
    return (math.ceil(res))
print(redondea_para_arriba(3.14))

#Operadores:
# "AND", para establecer que queremos que se cumplan las 2 condiciones
print(True and True)   # True
print(True and False)  # False
print(5 > 2 and 10 > 3)  # True

#"OR", si se cumple una de las 2 condiciones ya estaria para que sea true
print(True or False)   # True
print(False or False)  # False
print(5 > 10 or 3 < 8) # True

#Niega el valor lógico (si es True pasa a False, y al revés).
print(not True)   # False
print(not False)  # True
print(not (5 > 2))  # False, porque 5 > 2 es True

#Para pedir la longitud de un string podemos usar la funcion "len"(y el string por parametro en cuestion) EJ:
def longitudName(name: str)->int:
    res = len(name)
    return res
print(longitudName("mateo"))

#Funciones min() y max():

#🔹 min() Devuelve el valor más pequeño. Ejemplos:
print(min(3, 7, 2, 9))        # 2
print(min([10, 4, 8, 6]))     # 4
print(min("python"))          # 'h' (usa el orden alfabético)

#🔹 max() Devuelve el valor más grande.
print(max(3, 7, 2, 9))        # 9
print(max([10, 4, 8, 6]))     # 10
print(max("python"))          # 'y' (Tambien usa el orden alfabético)

#✅ Resumen:
#min() → devuelve el valor mínimo.
#max() → devuelve el valor máximo.
#Se pueden usar con números, listas, tuplas, strings, etc.
#Con key podés personalizar el criterio de comparación. EJ con una key:

palabras = ["hola", "adiós", "Python", "computadora"]
print(min(palabras, key=len))  # 'hola'   (más corta)
print(max(palabras, key=len))  # 'computadora' (más larga)
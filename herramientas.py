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

#| Sintaxis                   | Significado                                         | Ejemplo           | Resultado     |
#| -------------------------- | --------------------------------------------------- | ----------------- | ------------- |
#| `range(n)`                 | Números de `0` a `n-1`                              | `range(5)`        | 0, 1, 2, 3, 4 |
#| `range(inicio, fin)`       | Números de `inicio` a `fin-1`                       | `range(2, 6)`     | 2, 3, 4, 5    |
#| `range(inicio, fin, paso)` | De `inicio` a `fin-1` avanzando de `paso` en `paso` | `range(1, 10, 2)` | 1, 3, 5, 7, 9 |



                        ###Mas Herramientas:
#sqrt (raiz cuadrada),(viene del modulo de "math") devuelve un float con la raiz cuadrada del numero que le hayamos pasado EJEMPLO:
import math
def raizCuadrada(x:int)->float:
    if x < 10:
       resultado = math.sqrt(x)
    else:
        resultado = x
    return resultado
print(raizCuadrada(6)) #LE PASAMOS MATH.SQRT(PARAMETRO) seria modulo.funcion(parametro)

#Funcion Round:
#🔢 2. round(x, n)
#👉 Redondea el número x al número de decimales n.
print(round(3.14159))      # 3  → redondea al entero más cercano
print(round(3.14159, 2))   # 3.14  → 2 decimales
#Si el decimal es .5, redondea al par más cercano (regla de redondeo bancario de Python).

#⬇️ 3. floor(x)
#👉 Redondea hacia abajo al entero más cercano.
#Está en el módulo math.
import math
print(math.floor(3.9))   # 3
print(math.floor(-2.3))  # -3  (baja al entero menor)


#⬆️ 4. ceil(x)
#👉 Redondea hacia arriba al entero más cercano.
#También está en math.
import math
print(math.ceil(3.1))   # 4
print(math.ceil(-2.3))  # -2  (sube al entero mayor)



###Operaciones sobre secuencias:###
#💡 Función	📘 Descripción	🧮 Ejemplo	💬 Resultado
#len(seq)	#Devuelve la longitud (cantidad de elementos).	len([10, 20, 30])	3
#min(seq)	#Devuelve el valor mínimo.	min([4, 2, 9])	2
#max(seq)	#Devuelve el valor máximo.	max("hola")	'o'
#sum(seq)	#Suma todos los elementos (solo numéricos).	sum((1, 2, 3))	6
#sorted(seq)	#Devuelve una lista ordenada.	sorted([3, 1, 2])	[1, 2, 3]



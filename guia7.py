#1.1
##3 FORMARS DISTINTAS DE ENCARAR EL MISMO PROBLEMA
def problemaPertenece(s: list[int], e: int) -> bool:
    res = False
    largo = len(s)
    i = 0
    while i < largo:
        if s[i] == e:
            return True
        i += 1
    return res
#s[i] se toma como indice, entonces lo que estoy iterando son las pociciones... 
# de la lista, no el valor del indice, clave e importante
#El metodo mas choto para recorrer una lista es con un while
print(problemaPertenece([1,2,3,4,5,6], 7))

def problemaPerteneceBiss(s:list[int], e:int)->bool:
    for i in s:
        if i==e:
            return True
        i=+1
    return False
print(problemaPerteneceBiss([1,2,3,4,5,6,7], 1))
    

def problemaPerteneceBis(s: list[int], e: int) -> bool:
    return e in s #Metodo pitagonico
print(problemaPerteneceBis([1,2,3,3,5], 5))

#1.2 problema divide a todos
def problema_divide_a_todos (s:list[int], e:int)->bool:
    i = 0
    largo = len(s)
    while i < largo:
        if s[i] % e != 0:
            return False
        i +=1
    return True
print(problema_divide_a_todos([2,4,6], 2))

#1.3 Suma total:
def sumatotal(s:list[int])-> int:
    i = 0
    largo = len(s)
    suma = 0
    while i < largo:
        suma = suma + s[i]
        i = i + 1 
    return suma
print(sumatotal([1,2,3]))

#1.3 BISSGPT
def sumatotal(s: list[int]) -> int:
    suma = 0
    for x in s:
        suma += x
    return suma


#1.4 Problema maximo, devuelve el valor del elemento mas grande dentro de la secuencia:
def mayor(s: list[int])->int:
    i=0
    largo=len(s)
    mayor = s[0]
    while i < largo:
        if s[i] > mayor:
            mayor = s[i]
        i = i + 1
    return mayor 
print(mayor([1,2,3,4,7,3]))

#1.5
def minimo(s:list[int] )-> int:
    i = 0
    menor = s[0]
    longitud = len(s)
    while i < longitud:
        if s[i] < menor:
            menor = s[i]#Basicamente estoy reasignando cual es el menor de todos
        i = i + 1
    return menor

print(minimo([4,3,4,1]))
#MINIMO BISS CON FOR: "Es mas declarativo y legible usar for para este caso"
def minimoBiss(s: list[int])->int:
    menor = s[0]
    for elemento in s:
        if elemento < menor:
            menor = elemento
    return menor
print(minimoBiss([1,2,3,2,5,0]))

#1.6 Problemas Ordenados de forma creciente:
def ordenados(s: list[int])->bool:
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True
print(ordenados([3,2,3,5]))

#1.6 Biss con while:
def ordenadosBiss(s: list[int])->bool:
    i=0
    longitud= len(s) - 1
    while i < longitud:
        if s[i] > s[i+1]:
            return False
        i = i + 1
    return True 
print(ordenadosBiss([4,2,3,4]))
#PERFECTO :), Lo que se le suma al while es declarar que vas a recorrer la lista excepto el ultimo elemento y hacer que el bucle itere la funcion a mano

#1.7 Problema pos maximo:
def pos_maximo(s: list[int])-> int:
    if len(s)==0:
        return -1
    else:
        i = 0
        indiceMaximo = 0
        while i < len(s) - 1:
            if s[i] > s[indiceMaximo]:
                indiceMaximo = i
            i = i + 1
        return indiceMaximo
print(pos_maximo([]))

#1.8 Problema posicion del minimo:
def pos_minimo(s: list[int])->int:
    if len(s)==0:
        return -1
    else:
        i=0
        indiceMenor = 0
        while i < len(s) - 1 :
            if s[i] < s[indiceMenor]:
                indiceMenor = i 
            i = i + 1
        return indiceMenor
print(pos_minimo([]))
#EN ALGUNOS CASOS CONVIENE UN WHILE Y FUE. es mas te diria que con un while podes correr cualquier cosa.

#1.9 Dada una lista de palabra, devolver true, si alguna palabra tiene longitud mayor a 7
def palabras(s:list[str])->bool:
    for i in range(len(s) - 1):#La condicion me pide que tiene que fijarse en todos menos en el ultimo
        if len(s[i]) > 7:
            return True
    return False
print(palabras(["mate","mateos","mansilla"]))    



#1.10 le mete una palabra y me determina si es palindromo o no
def palindromo(s: list[str]) -> bool:
    i = 0
    ultimo = len(s) - 1  # índice del último elemento
    while i < ultimo:
        if s[i] != s[ultimo]:  # si no coinciden, no es palíndromo
            return False
        i = i + 1
        ultimo = ultimo - 1
    return True  # si salió del bucle, todos coincidieron

print(palindromo(['o', 's','o']))  # True

#1.10Correción BISS:
def palindromoCorregido(s: str)->bool:
    i = 0 
    ultimo = len(s) - 1
    while i < ultimo:
        if s[i] !=s[ultimo]:
            return False
        i = i + 1
        ultimo = ultimo - 1
    return True
print(palindromoCorregido("osoz"))

#1.11 devolver true, si hay 3 elementos iguales dentro de una secuencia;)
def tresIgualesConsecutivos(s: list[int])->bool:
    i=0
    while i < len(s) - 2:
        if s[i]==s[i+1] and s[i]== s[i+2]:
            return True
        i = i + 1
    return False
print(tresIgualesConsecutivos([1,2,0,3,3]))#OJO CON LA IDENTACIÓN, es importante

#1.12Recorrer una palabra en formato string, y devolver true si tiene 3 vocales distintas:
def vocal(palabra: str)->bool:##ARME PRIMERO UNA FUNCION QUE DETECTA VOCALES
    vocales = "AEIOUaeiou"
    for letra in palabra:
        if letra in vocales:
            return True
    return False
print(vocal("mt"))
#ya tengo una funcion que me devuelve true si hay una letra que es vocal, ahora voy a crear otra que las vaya guardando:

def sumaVocal(palabra:str)->int:
    sumaVocales = set()
    i = 0
    while i < len(palabra):
        if vocal(palabra[i]):
            sumaVocales.add(palabra[i].lower())
        i = i + 1 #si justo en la posición i no habia una vocal va a pasar a la siguiente, y así sucesivamente, hasta el ultimo elemento
    return len(sumaVocales) >= 3
print(sumaVocal("mateo"))    

#1.13
def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:
    inicio_actual = 0
    long_actual = 1
    inicio_max = 0
    long_max = 1

    i = 0
    while i < len(s) - 1:
        if s[i] <= s[i + 1]:
            # sigue ordenada
            long_actual += 1
        else:
            # se rompió la secuencia
            if long_actual > long_max:
                long_max = long_actual
                inicio_max = inicio_actual
            # reinicio para la nueva secuencia
            inicio_actual = i + 1
            long_actual = 1
        i += 1

    # al final del bucle hay que comparar por si la secuencia más larga termina al final
    if long_actual > long_max:
        long_max = long_actual
        inicio_max = inicio_actual

    return inicio_max
print(pos_secuencia_ordenada_mas_larga([1,2,3,4,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))

#1.14 Cantidad de digitos Impares:
#primero creo una funcion que detecte si un digito es impar:
def impares(n:int)->bool:
    if n % 2!=0 :
        return True
    else:
        return False
print(impares(7))#Genial, funca
#Ahora voy a construir una funcion que cuente la cantidad de numeros impares:

def cantidasdImpares(s:list[int])->int:
    totalimpares = 0
    for numero in s:
        for digito in str(abs(numero)):#convierto cada numero en un string y recorro cada letra que seria un numero
            if impares(int(digito)):
                totalimpares = totalimpares + 1 

    return totalimpares
print(cantidasdImpares([133,3,2,3,4,5,6,7,7,7,7,7]))
##Y es asi lamentablemente, nada que valga la pena se consigue facilmente.




####2 modificando acorde si es par o impar:
def CerosEnPosicionesParesDos(s: list[int]) -> list[int]:
    res = list(s)         # copia de la lista original
    i = 0
    while i < len(res):
        if i % 2 == 0:    # posición par → reemplazo por 0
            res[i] = 0
        else:              # posición impar → mantengo el valor
            res[i] = res[i]
        i += 1
    return res

print(CerosEnPosicionesParesDos([7, 7, 7, 7, 7, 7]))


#2.2
def CerosEnPosicionesIMPares(s:list[int])->list[int]:
    i = 0
    while i < len(s):
        if i % 2 == 0:
            s[i] = s[i]
        else:
            s[i] = 0
        i += 1
    return s

print(CerosEnPosicionesIMPares([7,7,7,7]))


#2.2Biss con for:
def CerosEnPosicionesIMParesBiss(s: list[int]) -> list[int]:
    for i in range(len(s)):           # recorre los índices 0, 1, 2, ...
        if i % 2 != 0:                # si la posición es impar
            s[i] = 0
    return s

print(CerosEnPosicionesIMParesBiss([7, 7, 7, 7, 7, 7, 7, 7]))#No importa el elemente en la posicion, sino solamente el indice de la posicion.


#2.3 Problema sin vocales:

def sin_vocales(s: str) -> str:
    """
    Devuelve la subsecuencia de s que se obtiene al quitarle las vocales.
    requiere: True
    asegura: res es la subsecuencia de s sin las vocales
    """
    res = ""                      # resultado vacío
    vocales = "AEIOUaeiou"        # conjunto de vocales
    for c in s:                   # recorro cada caracter de s
        if c not in vocales:      # si no es vocal
            res += c              # lo agrego a la subsecuencia
    return res

# Ejemplo:
print(sin_vocales("Hola Mundo"))

#2.4
def reemplaza_vocales(s: str)->str:
    res = ""
    vocales = "AEIOUaeiou"
    for letras in s:
        if letras not in vocales:
            res += letras
        else:
            res += "-"
    return res

print(reemplaza_vocales("hola mundo"))

#2.5
def da_vuelta_str(s: str) -> str:
    """
    Devuelve una cadena igual a s pero invertida.
    requiere: True
    asegura: len(res) == len(s) y para todo i, res[i] = s[len(s) - i - 1]
    """
    res = ""
    i = len(s) - 1
    while i >= 0:
        res += s[i]
        i -= 1
    return res

print(da_vuelta_str("hola"))  # me va a devolver "aloh"

#2.5BISS usando Slicing:
def daVuelta(s: str)->str:
    res = s[::-1]
    return res
print(daVuelta("Mateo"))

#2.6
def eliminar_repetidos(s: str) -> str:
    """
    Devuelve una cadena sin caracteres repetidos, conservando el orden original.
    requiere: True
    asegura: len(res) <= len(s) y no hay caracteres repetidos en res
    """
    res = ""
    for c in s:
        if c not in res:   # si el caracter no está todavía en res
            res += c       # lo agrego
    return res

"""
# Ejemplo:
print(eliminar_repetidos("banana"))  # → "ban"#Repasar 2.6 y como carajos usar slicing
# Tomar una sublista específica, por ejemplo del índice 2 al 7, de 2 en 2
lista = [1,2,3,4,5,6,7,8,9,10]#INICIO:PASO:FIN (DEL LADO IZQ DE LOS ":" VAN LOS INDICES)
print(lista[2:8:2])  # [2, 4, 6]
"""
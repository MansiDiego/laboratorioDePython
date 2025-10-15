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
    mayor= s[0]
    while i < largo:
        if s[i] > mayor:
            mayor = s[i]
        i = i + 1
    return mayor 
print(mayor([1,2,3,4,5,3]))

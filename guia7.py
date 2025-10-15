#Ejercicio 1.1
def pertenece(s:list[int], e: int)-> bool:
    res = False #Valor por defecto es falso.
    i:int = 0
    long:int = len(s)
    while i < long:   #MIENTRAS QUE EL INDICE ESTE EN LA SECUENCIA
        if  i == e:     
            res = True
        i =+ 1
    return res

print(pertenece([1, 2, 3, 4, 5] ,6))
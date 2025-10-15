#La instruccion return, basicamente le dice cuando terminar y le indicamos que queremos que nos devuelva.
def suma2 (x: int, y: int) -> int:
    res: int = x + y
    return res

#Ejemplo de transformacion de estados--
def ejemplo() -> int: #Aca el nombre de la funcion es Ejemplo, y le definimos que devuelve un tipo Int.
    x: int = 0
    x = x + 3
    x = 2 * x
    return x

#Ejemplo de un condicional 
def elegirelMayor(x: int, y: int) -> int:
    z: int
    print("x = " + str(x) + " | y = " + str(y))
    if x > y :
        print("x es mayor a y")
        z = x
        print("(se cumple B) -> z toma el valor de x")
    else:
        print("y es mayor o giaul que x")
        z = y 
        print("(No se cumple B)-> Entonces z toma el valor de y") 
    return z
    


#Ejemplo de un programa con varios estados
"""def suc(x: int) -> int:
//estado a;
x = x + 2
//estado b
//vale x == x@a+2;
✭✭En el estado b, x vale lo que valıa en el estado a mas 2✮✮
x = x - 1
//estado c
//vale x == x@b-1;
✭✭En el estado c, x vale lo que valıa en el estado b menos 1✮✮
return x
I De esta manera, mediante la transformacion de estados, podremos realizar
una ejecucion simbolica del programa, declarando cuanto vale cada
variable, en cada estado del programa, en funcion de los valores anteriores."""

"""Conceptualmente, parece que:
Los tipos primitivos (int, float, str, tuple, bool, etc.) se pasan “por valor” (porque son inmutables, no podés modificar el objeto en sí).

Los tipos compuestos/mutables (list, dict, etc.) se pasan “por referencia” (porque sí podés modificar su contenido)."""
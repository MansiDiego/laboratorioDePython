import math #Importamos la libreria para usar algunas funciones
#1
def imprimir_hola_mundo():
    return("hola mundo")
print(imprimir_hola_mundo())
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

#Ejercicio 2.7 cantidad de pizzas, dada una cantidad de comensales y una minima cantidad de porciones que se come cada comensal
#determinar la cantidad de pizzas que necesitamos, me piden que es preferible que sobren porciones y que no falten.
#por lo tanto uso la funcion math.ceil, que es para que redondee para arriba, por ejemplo 7/2 = 3.5 => devuelve 4 con la funcion
def cantidad_pizzas(comensales: int, min_cant_porciones:int) -> int:
    porciones = comensales * min_cant_porciones
    numeroDePizzas = porciones / 8
    return (math.ceil(numeroDePizzas)) 
print(cantidad_pizzas(6,3))



#3.1
def alguno_es_0(num1: int, num2:int)->bool:
    res = num1 == 0 or num2 == 0 
    return res
print(alguno_es_0(0,3))

#3.2
def ambos_son_0(num1: int, num2:int)-> bool:
    res = num1 == 0 and num2 == 0
    return res
print(ambos_son_0(0,0))

#3.3 para pedir la longitud nombre de la variable len(nombre)####
def es_nombre_largo(nombre: str)->bool:
    return len(nombre) >= 3 and len(nombre) <=8
print(es_nombre_largo("mansilla"))

#3.4 ¿es Bisiesto? (que indica si un año tiene 366 dias)(Un año es bisiesto si es multiplo de 400, o bien de 4 pero no de 100)
def esBisiesto(año:int)->bool:
    res = año % 400 == 0 or (año % 4 == 0 and año % 100 != 0) 
    return res
print(esBisiesto(2012))


#4.1--Definir la función peso de pino(esta laburada sobre centimetros)--
def peso_de_pino(altura: int)->int:
    res : int
    if altura <= 300:
        res = altura * 3
    else:
       res = 300 * 3 + ((altura - 300) * 2)
    return res
print(peso_de_pino(500))

#4.1bis--Usando la funcion min y max solamente
def pesoDelPinoBis(alt: int) -> int:
    res : int
    res = min(alt, 300) * 3 + max(alt - 300, 0) * 2 
    return res
print(pesoDelPinoBis(300))

#4.2-- definir la funcion "es peso util", es util si pesa mas de 400 y menos de 1000, la funcion recibe un "peso"
def peso_util(util: int)->bool:
    return (min(1000, max(400, util))) == util #Observacion, toma los vordes, es decir puede ser 1000 o 400 y funca, sino deberia modificar los bordes, para abajo y para arriba para que sea estricto
print(peso_util(900))

#estoy haciendo composición de funciones, con max(400, util), si 400> util entonces me va a devolver 400, sino al reves.
#si util < 1000 entonces me va a devolver "min" o sea util, y lo mismo al reves si util>1000 me devuelve 1000 la funcion min.
#finalmente lo comparo con util, si es el mismo valor entonces true, si es 400 o 1000 quiere decir que se cayo por los bordes, y por ende no cumple lo pedido

#4.3 sin composición de funciones
def sirve_pinoSincompo(altura: int) -> bool:
    peso = peso_de_pino(altura) < 1000 and peso_de_pino(altura)> 400
    return peso
print(sirve_pinoSincompo(500))

#4.4 es una compo de las 2, recibe la altura del pino y determina si le sirve a la fabrica
def sirve_pino(altura: int) -> bool:
    peso = peso_de_pino(altura)
    return peso_util(peso)
print(sirve_pino(200))



#Ejercicio 5.1
def devolver_el_doble(numero: int) -> int:
    res : int
    if numero % 2 == 0:
        res = 2 * numero
    else:
        res = numero
    return res
print(devolver_el_doble(8))
#RECORDAR GUARDAR LA VARIABLE PARA LOS CONDICIONALES.

#5.2 
def devolver_valor_si_es_par_si_no_el_que_sigue(numero:int) -> int:
    res : int
    if numero % 2 == 0 :
        res = numero
    else:
        res = numero + 1
    return res
print(devolver_valor_si_es_par_si_no_el_que_sigue(18))    

#5.2 BIS "CON DOBLE IF"
def devolverpar_o_Sig(numero:int) ->int:
    res : int
    if numero % 2 == 0:
        res = numero
    if numero % 2 != 0:
        res = numero + 1
    return  res      
print(devolverpar_o_Sig(2))

#5.2 BIS III CON if elif else, la diferencia es que le puedo asignar como si tuviera un caso base(quiero creer xd)
def devolverLoMismo(numero: int)-> int:
    res : int
    if numero % 2 == 0:
        res = numero
    elif numero % 2 !=0:
        res = numero + 1
    else:
        res = 0        
    return res    
print(devolverLoMismo(3))  
#Las 3 formas funcionan, pero con elif puedo meterle mas condiciones

#5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) ->int:
    res : int
    if numero % 3 == 0 :
        res = 2 * numero
    elif numero % 9 == 0 :
        res = 3 * numero
    else:
        res = numero
    return res
print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))    

def bis2(numero: int) -> int:
    res: int
    if numero % 3 == 0 :
        res = 2 * numero
    if numero % 9 == 0 :
        res = 3 * numero
    else:
        res = numero

    return res 
print(bis2(3))  

def bis3(numero : int) ->int:
    res : int
    if numero % 3 == 0 :
        res = 2 * numero
    elif numero % 9 == 0 :
        res = 3 * numero  
    elif numero % 3 != 0 and numero % 9 !=0:
        res = numero
    return res
print(bis3(18))        
#Cuestionable porque las 3 funciones andan, pero de formas diferentes, la primera si capta la primer guarda con if, la toma como prioridad

#5.4
def lindo_nombre(nombre:str)->str:
    res : str
    if len(nombre) >= 5:
        res = "Tu nombre tiene muchas letras"
    else:
        res = "tu nombre tiene menos de 5 caracteres"
    return res
print(lindo_nombre("mate"))

#5.5
def elRango(numero: int)->str:
    res : int
    if numero < 5:
        res = "Menor a 5"
    elif numero >= 10 and numero <=20:
        res = "entre 10 y 20"
    else:
        res = "Mayor a 20"
    return res    
print(elRango(18))   

#5.6
def laburar_o_vacaciones(sexo: str, edad: int)-> str:
    res : str
    if sexo == "Masculino" and edad > 18 and edad < 65:
        res = "toca chambear, lo siento maquina!!"
    elif edad < 18:
        res= "Andá de vacaciones"
    elif sexo == "Masculino" and edad > 65:
        res = "Andá de vacaciones."
    elif sexo == "Femenino" and edad > 60:
        res = "Andá de vacaciones"    
    else:
        res = "toca chambear, lo siento maquina!!"    
    return res
print(laburar_o_vacaciones("Masculino", 66))    
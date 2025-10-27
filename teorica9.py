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
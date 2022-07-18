#Tipos de dato
""" Tipo numérico
Python3 trabaja con tres tipos numéricos:

Enteros (int) : Representan todos los números enteros (positivos, negativos y 0),
sin parte decimal. En python3 este tipo no tiene limitación de espacio.

Reales (float) : Sirve para representar los números reales, 
tienen una parte decimal y otra decimal. Normalmente se utiliza 
para su implementación un tipo double de C.

Complejos (complex) : Nos sirven para representar números complejos, 
con una parte real y otra imaginaria. Como hemos visto en la unidad anterior 
son tipos de datos inmutables.

"""
print("########Enteros (int)################")
entero = 7
type1 = type(entero)
print(type1)
print("_____________________________________")

print("########Reales (float)################")
real = 7.2
type2 = type(real)
print(type2)
print("_____________________________________")


print("########Complejos (complex)################")
complejo = 1+2j
type3 = type(complejo)
print(type3)
print("_____________________________________")

#Tipo cadena
"""  
Tipo cadena
Las cadenas de caracteres ( str ): Me permiten guardar secuencias de caracteres. 
Es un tipo inmutable. Como hemos comentado las cadenas de caracteres en python3 están codificada con Unicode.

"""

#Definición de cadenas. Constructor str
#Podemos definir una cadena de caracteres de distintas formas:
print("##########Tipo cadena##############")
cad1 = "Hola"
cad2 = '¿Que tal?'
cad3 = '''Hola que tal?'''
print(cad1)
print(cad2)
print(cad3)

# También podemos crear cadenas con el constructor str a partir de otros tipos de datos.
cad4 = str(1)
cad5 = str(2.45)
cad6 = str([1,2,3])
print(cad4)
print(cad5)
print(cad6)


print("_____________________________________")

""" 
Operaciones básicas con cadenas de caracteres
Las cadenas se pueden recorrer.
Operadores de pertenencia: in y not in .
Concatenación: +
Repetición: *
Indexación
Slice
Entre las funciones definidas podemos usar: len , max , min , sorted .
"""

# Tipo lista
"""
Tipo lista
Las listas nos permiten guardar un conjunto de datos que se pueden repetir 
y que pueden ser de distintos tipos. Es un tipo mutable. Son muy usadas para tratar un conjunto de datos.

"""
# Construcción de una lista
#Para crear una lista puedo usar varias formas:

#Con los caracteres [ y ] :
lista1 = []
lista2 = ["a", 1, True]

#  Utilizando el constructor list , que toma como parámetro un dato de algún tipo secuencia.

lista3 = list()
lista4 = list("hola")
print(lista4) 

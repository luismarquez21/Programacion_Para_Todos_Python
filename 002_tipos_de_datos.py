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

# Vamos a ver distintos ejemplos partiendo de una lista, que es una secuencia mutable.

listamc = [1,2,3,4,5,6]

#Las secuencias se pueden recorrer

for num in listamc:
    print(num, end="")

"""
Métodos principales de listas
Cuando creamos una lista estamos creando un objeto de la clase list , que tiene definido un conjunto de métodos:

lista.append   lista.copy     lista.extend   lista.insert   lista.remove   lista.sort
lista.clear    lista.count    lista.index    lista.pop      lista.reverse
Métodos de inserción: append, extend, insert

lista = [1,2,3]
lista.append(4)
lista
[1, 2, 3, 4]

 lista2 = [5,6]
 lista.extend(lista2)
lista
[1, 2, 3, 4, 5, 6]    

lista.insert(1,100)
lista
[1, 100, 2, 3, 4, 5, 6]
Métodos de eliminación: pop, remove

lista.pop()
6
lista
[1, 100, 2, 3, 4, 5]

lista.pop(1)
100
lista
[1, 2, 3, 4, 5]

lista.remove(3)
lista
[1, 2, 4, 5]

"""

# Tipo diccionario
"""
Los diccionarios son tipos de datos que nos permiten guardar valores, 
a los que se puede acceder por medio de una clave . 
Son tipos de datos mutables y los campos no tienen asignado orden.
"""
# Definición de diccionarios. Constructor dict

"""
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True
Si tenemos un diccionario vacío, al ser un objeto mutable, también podemos construir el diccionario de la siguiente manera.


>>> dict1 = {}
>>> dict1["one"]=1
>>> dict1["two"]=2
>>> dict1["three"]=3
Operaciones básicas con diccionarios
>>> a = dict(one=1, two=2, three=3)
 len() : Devuelve número de elementos del diccionario.
  >>> len(a)
  3
 Indexación: Podemos obtener el valor de un campo o cambiarlo (si no existe el campo nos da una excepción KeyError ):

  >>> a["one"]
  1
  >>> a["one"]+=1
  >>> a
  {'three': 3, 'one': 2, 'two': 2}
 del() :Podemos eliminar un elemento, si no existe el campo nos da una excepción KeyError :

  >>> del(a["one"])
  >>> a
  {'three': 3, 'two': 2}
 Operadores de pertenencia: key in d y key not in d .
  
  >>> "two" in a
  True
 iter() : Nos devuelve un iterador de las claves.
  
  >>> next(iter(a))
  'three'
Los diccionarios son tipos mutables
Los diccionarios, al igual que las listas, son tipos de datos mutable. Por lo tanto podemos encontrar situaciones similares a las que explicamos en su momentos con las listas.


>>> a = dict(one=1, two=2, three=3)
>>> a["one"]=2
>>> del(a["three"])
>>> a
{'one': 2, 'two': 2}    


>>> a = dict(one=1, two=2, three=3)
>>> b = a
>>> del(a["one"])
>>> b
{'three': 3, 'two': 2}    
En este caso para copiar diccionarios vamos a usar el método copy() :


>>> a = dict(one=1, two=2, three=3)
>>> b = a.copy()
>>> a["one"]=1000
>>> b
{'three': 3, 'one': 1, 'two': 2}


"""

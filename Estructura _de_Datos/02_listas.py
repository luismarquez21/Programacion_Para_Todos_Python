# Listas en Python

"""  
"Python es un lenguaje de programación interpretado de alto nivel y orientado a objetos, con el cual podemos crear todo tipo de aplicaciones."
En algunos lenguajes de programación se las conocen como arreglos o matrices; y se caracterizan porque los elementos están entre corchetes y separados por una coma.

"""

"""  
Una lista es una estructura de datos y un tipo de dato en python con características 
especiales. Lo especial de las listas en Python es que nos permiten almacenar cualquier
tipo de valor como enteros, cadenas y hasta otras funciones; por ejemplo:
"""

lista = [1, 2.5, 'DevCode', [5,6], 4]

print (lista[0]) # 1
print (lista[1]) # 2.5
print (lista[2]) # DevCode
print (lista[3]) # [5,6]
print (lista[3][0]) # 5
print (lista[3][1]) # 6
print (lista[1:3]) # [2.5, 'DevCode']
print (lista[1:6]) # [2.5, 'DevCode', [5, 6], 4]
print (lista[1:6:2]) # [2.5, [5, 6]]

for element in lista:
    print(element) 
    
# Métodos de las Listas
""" 
Las listas en Python  tienen muchos métodos que podemos utilizar, 
entre todos ellos vamos a nombrar los más importantes.
Para esto utilizaremos esta lista de ejemplo.
"""
my_list = [2, 5, 'DevCode', 1.2, 5]

# Append()
# Este método nos permite agregar nuevos elementos a una lista.
my_list.append(10) # [2, 5, 'DevCode', 1.2, 5, 10]
my_list.append([2,5])  # [2, 5, 'DevCode', 1.2, 5, [2, 5]]

print(my_list)

# Extend()
# Extend también nos permite agregar elementos dentro de una lista, 
# pero a diferencia de append al momento de agregar una lista, cada 
# elemento de esta lista se agrega como un elemento más dentro de la otra lista

my_list.extend([2,5]) # [2, 5, 'DevCode', 1.2, 5, 2, 5]

print(my_list)

# Remove()
# El método remove va a remover un elemento que se le pase como parámentro 
# de la lista a donde se le esté aplicando.

my_list.remove(2) # [5, 'DevCode', 1.2, 5]
print(my_list)

# Index()
# Index devuelve el número de indice del elemento que le pasemos por parámetro.
my_list.index('DevCode') # 2





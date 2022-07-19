#Operadores aritméticos
"""
Los operadores lógicos o logical operators nos permiten trabajar con valores de tipo 
booleano. Un valor booleano o bool es un tipo que solo puede tomar valores 
True o False. Por lo tanto, estos operadores nos permiten realizar diferentes operaciones 
con estos tipos, y su resultado será otro booleano. Por ejemplo, True and True usa el operador and, y 
su resultado será True. A continuación lo explicaremos mas en detalle.

"""

#Operador:	             Nombre:	                                     Ejemplo:
#and	       Devuelve True si ambos elementos son True	          True and True = True
#or	           Devuelve True si al menos un elemento es True	      True or False = True
#not	       Devuelve el contrario, True si es Falso y viceversa	  not True = False

#Operador and
""" 
El operador and evalúa si el valor a la izquierda y el de la derecha son True, 
y en el caso de ser cierto, devuelve True. Si uno de los dos valores es False, 
el resultado será False. Es realmente un operador muy lógico e intuitivo que 
incluso usamos en la vida real. Si hace sol y es fin de semana, iré a la playa.
Si ambas condiciones se cumplen, es decir que la variable haceSol=True y
la variable finDeSemana=True, iré a la playa, o visto de otra forma 
irALaPlaya=(haceSol and finDeSemana).

"""

print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# Operador or
""" 
El operador or devuelve True cuando al menos uno de los elementos es igual a True. 
Es decir, evalúa si el valor a la izquierda o el de la derecha son True.

"""

print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False

# Operador not
""" 
Y por último tenemos el operador not, que simplemente invierte True por False y False 
por True. También puedes usar varios not juntos y simplemente se irán aplicando uno 
tras otro. La verdad que es algo difícil de ver en la realidad, pero simplemente puedes 
contar el número de not y si es par el valor se quedará igual. Si por lo contrario 
es impar, el valor se invertirá.

"""
print(not True)  # False
print(not False) # True
print(not not not not True) # True
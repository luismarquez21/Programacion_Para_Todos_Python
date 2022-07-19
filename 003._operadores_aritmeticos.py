# Operadores aritméticos
"""
Los operadores aritméticos o arithmetic operators son los más comunes que nos 
podemos encontrar, y nos permiten realizar operaciones aritméticas sencillas,
como pueden ser la suma, resta o exponente. A continuación, 
condensamos en la siguiente tabla todos ellos con un ejemplo, donde x=10 y y=3.

"""
x = 10; y = 3
print("Operadores aritméticos")
print("x+y =", x+y) #Suma   #13
print("x-y =", x-y) #Resta  #7
print("x*y =", x*y) #Multiplicación  #30
print("x/y =", x/y) #División  #3.3333333333333335
print("x%y =", x%y) #Módulo  #1 # Se trata de calcular el resto de la división entera entre ambos números. Es decir, si dividimos 10 entre 3, el cociente sería 3 y el resto 1. Ese resto es lo que calcula el módulo.
print("x**y =", x**y) #Exponente #1000 # El operador ** realiza el exponente del número a la izquierda elevado al número de la derecha.
print("x//y =", x//y) #Cociente #3 Por último, el operador // calcula el cociente de la división entre los números que están a su izquierda y derecha.

""" 
El orden de prioridad sería el siguiente para los operadores aritméticos, 
siendo el primero el de mayor prioridad:

() Paréntesis
** Exponente
-x Negación
* / // Multiplicación, División, Cociente, Módulo
+ - Suma, Resta
"""
print(10*(5+3)) # Con paréntesis se realiza primero la suma
# 80
print(10*5+3)   # Sin paréntesis se realiza primero la multiplicación
# 53
print(3*3+2/5+5%4) # Primero se multiplica y divide, después se suma
#10.4
print(-2**4)       # Primero se hace la potencia, después se aplica el signo
#-16
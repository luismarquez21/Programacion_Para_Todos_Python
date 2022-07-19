#Operadores relacionales
#Los operadores relacionales, o también llamados comparison operators nos permiten 
# saber la relación existente entre dos variables. Se usan para saber si por ejemplo 
# un número es mayor o menor que otro. Dado que estos operadores indican si se cumple 
# o no una operación, el valor que devuelven es True o False. Veamos un ejemplo: 
# con x=2 e y=3

"""
Operador	    Nombre	                Ejemplo
==	            Igual	                x == y = False
!=	            Distinto	            x != y = True
>	            Mayor	                x > y = False
<	            Menor	                x < y = True
>=	            Mayor o igual	        x >= y = False
<=	            Menor o igual	        x < y = True

"""

x=2; y=3
print("Operadores Relacionales")
print("x==y =", x==y) # False
print("x!=y =", x!=y) # True
print("x>y  =", x>y)  # False
print("x<y  =", x<y)  # True
print("x>=y =", x>=y) # False
print("x<=y =", x<=y) # True
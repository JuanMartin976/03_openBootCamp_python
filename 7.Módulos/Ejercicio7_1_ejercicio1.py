# Se importa el módulo creado
from Ejercicio7_1_moduloCalculadora import * 

a, b, c, d = (10, 5, 8, 2)

print( "{} + {} = {}".format(a, b, suma(a, b) ) )
print( "{} - {} = {}".format(b, d, resta(b, d) ) )
print( "{} * {} = {}".format(b, b, multiplicar(b, b) ) ) 
print( "{} / {} = {}".format(a, c, division(a, c) ) )

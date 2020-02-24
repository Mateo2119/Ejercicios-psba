# -*- coding: utf-8 -*-
"""
58. Escribir un programa que cambie las mayúsculas de una cadena de caracteres a minúsculas y
viceversa. 

"""

cadena = input("Ingrese la cadena: ")
new_cadena = ""


for i in cadena:
    
    if i.isupper():
        new_cadena = new_cadena + i.lower()
    else:
        new_cadena = new_cadena + i.upper()

print(new_cadena)    

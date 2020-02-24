# -*- coding: utf-8 -*-
"""
Escribir un programa que dada una tupla de las vocales y otra con las consonantes, capture
una cadena de caracteres y cuente cuantos caracteres pertenecen a la tupla de vocales,
cuantos a la tupla de consonantes y cuantos no pertenecen a ninguna de las dos tuplas
"""

vocales = ("a","e","i","o","u")
consonantes = ("b","c","d","f","g","h","j","k","l","m","ñ","n","p","q","r","s","t","v","w","x","y","z")

cadena = input("Escriba su cadena : ")

vocales_num = 0
consonantes_num = 0
ninguno_num = 0

for i in cadena:
    if i.lower() in vocales:
        vocales_num = vocales_num +1
    elif i.lower() in consonantes:
        consonantes_num = consonantes_num +1
    else: 
        ninguno_num = ninguno_num +1
    
print(f"{cadena} tiene {vocales_num} vocales, {consonantes_num} consonantes y {ninguno_num} caracteres")
        
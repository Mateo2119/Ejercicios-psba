# -*- coding: utf-8 -*-
"""
Escribir un programa que lea una frase introducida desde el teclado y la escriba al revés

@author: lenovo
"""
palabra = input("Ingrese su palabra: ")
revez = ""

for i in reversed(palabra):
    revez = revez + i
    
print(revez)

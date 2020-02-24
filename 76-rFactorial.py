# -*- coding: utf-8 -*-
"""
76. Escriba un programa que calcule el factorial de un numero usando recursividad.
"""
numero = int(input("Digite el número: "))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

print(f"El factorial es: {factorial(numero)}")
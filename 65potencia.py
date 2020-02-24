# -*- coding: utf-8 -*-
"""
Escribir un programa que calcule la potencia usando una función propia (no debe usar la
funciones nativas del lenguaje u operadores que realicen esta operación).

"""
a = int(input("Digite el numero: "))
b = int(input("Digite la potencia: "))

def potencia(num, pot):
    res = 1
    
    for i in range(pot):
        res = res*num
        i = i + 1
    return res
    
print(potencia(a,b))
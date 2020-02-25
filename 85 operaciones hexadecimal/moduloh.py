# -*- coding: utf-8 -*-
"""
85. Crear un módulo que maneje funciones para operar en sistema hexadecimal, las operaciones
que se deben implementar son suma, resta, multiplicación y división.

@author: lenovo
"""

def a_entero(num):
     l = len(num) - 1
     entero = 0
     for i in num:
          potencia = 2 ** l
          entero = entero + ( int(i) * potencia)
          l = l - 1
     return entero

def a_hexa(num):
     hexadecimal = ""
     while (True):
          aux = str( num % 2 )
          num = int( num / 2 )
          hexadecimal = aux + hexadecimal
          if (num <= 1):
               hexadecimal = ( str( num ) if num > 0 else "" ) + hexadecimal
               break
     return hexadecimal
    
def sum_bin(a,b):
    b1 = a_entero(a)
    b2 = a_entero(b)    
    return a_hexa(b1+b2)

def res_bin(a,b):
    b1 = a_entero(a)
    b2 = a_entero(b)    
    return a_hexa(b1-b2)

def div_bin(a,b):
    b1 = a_entero(a)
    b2 = a_entero(b)    
    return a_hexa(b1/b2)

def mul_bin(a,b):
    b1 = a_entero(a)
    b2 = a_entero(b)    
    return a_hexa(b1*b2)
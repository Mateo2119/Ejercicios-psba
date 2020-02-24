# -*- coding: utf-8 -*-
"""
Escribir un programa que lea un tiempo en horas, minutos y segundos y empiece a
cronometrar el tiempo mostrándolo en pantalla hasta llegar al limite leído al inicio.

@author: lenovo
"""

import time

hora = int(input("Digite la hora limite: "))
minuto = int(input("Digite el minuto limite: "))
segundo = int(input("Digite el segundo limite: "))
reloj_limite = (hora*3600)+(minuto*60)+segundo
reloj = 0

for h in range(0,24):
    if reloj_limite == reloj:
        break
    for m in range(0,60):
        if reloj_limite == reloj:
            break
        for s in range(0,60):
            reloj = (h*3600)+(m*60)+s
            print(f"{h}:{m}:{s}")
            if reloj_limite == reloj:
                break
            time.sleep(1)
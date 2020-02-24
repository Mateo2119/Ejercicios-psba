numero = int(input("Ingrese el número del dia de la semana: "))

while numero <=0 or numero >7:
    numero = int(input("Ingrese el número del dia de la semana: "))

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miercoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sabado")
else:
    print("Domingo")
        
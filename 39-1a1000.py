seguir = True
numero = 0

while seguir:
    
    if seguir == True:        
        for i in range(1,21):
            print(numero + i)
        numero = numero + 20
    
    desicion = int(input("seguir mostrando: si (1) ó no (2) :"))
    while desicion!=1 and desicion!=2:
        desicion = int(input("seguir mostrando: si (1) ó no (2) :"))

    if desicion ==2 or numero == 1000:
        seguir = False
        print("Finalizado")
        
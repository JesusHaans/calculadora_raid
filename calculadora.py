import numpy as np

#Funcion para pedir un numero entero y que no se pueda introducir otro tipo de dato
def pedirNumeroEntero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            print (" ")
            num = int(input("Introduce un numero entero: "))
            correcto=True
            print (" ")
        except ValueError:
            print (" ")
            print('Error, introduce un numero entero')
            print (" ")
    return num
 
 #Funcion para llenar el array con la cantidad de discos que se quiera
def llenarArray(discos):
    array = []
    tamano = 0
    for i in range (0,discos):
        print (" ")
        print("Introduce el tamaño del disco en GB",i+1)
        print (" ")
        tamano = pedirNumeroEntero()
        array.append(tamano)
    return array

#Funcion para calcular el RAID 0 
def raid0():
    array = []
    print (" ")
    print("RAID 0")
    print (" ")
    print("Introduce el numero de discos que quieres usar")
    print (" ")
    correcto = False
    discos = 0
    while (not correcto):
        discos = pedirNumeroEntero()
        if(discos > 2):
            correcto = True
        else:
            print (" ")
            print("El numero de discos debe ser mayor o igual a 2")
            print (" ")
    array = llenarArray(discos)
    minimo = np.min(array)
    print (" ")
    print("El tamaño del RAID es",(minimo*discos),"GB")
    print (" ")
    arrayexceso = []
    exceso = 0
    for i in range (0,discos):
        if(array[i] > minimo):
            arrayexceso.append(array[i])
    for i in range (0,len(arrayexceso)):
        arrayexceso[i] = arrayexceso[i] - minimo
    for i in range (0,len(arrayexceso)):
        exceso = exceso + arrayexceso[i]
    print (" ")
    print("El tamaño sin uso del RAID es",exceso,"GB")
    print (" ")
    print("El tamaño de recuperacion del RAID es 0 GB")
    print (" ")


#Menu Principal donde usaremos para la eleccion de los RAID
def menu():
    salir = False
    opcion = 0

    while not salir:
 
        print ("1. RAID 0")
        print ("2. RAID 1")
        print ("3. RAID 5")
        print ("4. RAID 6")
        print ("5. RAID 1+0")
        print ("6. RAID 0+1")
        print ("7. RAID 5+0")
        print ("8. RAID 6+0")
        print ("9. SALIR")
        print (" ")
        print ("Elige una opcion")
        print (" ")

        opcion = pedirNumeroEntero()
 
        if opcion == 1:
            print ("Opcion RAID 0")
            raid0()
        elif opcion == 2:
            print ("Opcion RAID 1")
        elif opcion == 3:
            print("Opcion  RAID 5")
        elif opcion == 4:
            print("Opcion RAID 6")
        elif opcion == 5:
            print ("Opcion RAID 1+0")
        elif opcion == 6:
            print("Opcion RAID 0+1")
        elif opcion == 7:
            print("Opcion RAID 5+0")
        elif opcion == 8:
            print ("Opcion RAID 6+0")
        elif opcion == 9:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 9")

#Inicio del programa
menu()

#Despedida del programa
print ("Fin")
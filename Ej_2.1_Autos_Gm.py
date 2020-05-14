
#autos = ('Ford', 'Chevrolet', 'Fiat')
i=0
for i in range(5):
    precio=0
    Nombre = input("Ingrese Nombre y apellido  ")
    Marca = input ("Ingrese marca deseada  ")
    Puerta = input ("Ingrese cantidad de puertas  ")
    Color = input ("Ingrese color  ")
    if Marca == 'Ford':
       precio = precio + 100000
    elif Marca == 'Chevrolet':
        precio = precio + 120000
    elif Marca == 'Fiat':
        precio = precio + 80000
    if Puerta == '2':
        precio = precio + 50000
    elif Puerta == '4':
        precio = precio + 65000
    elif Puerta == '5':
        precio = precio + 78000
    if Color == 'Blanco':
        precio = precio + 10000
    elif Color == 'Azul':
        precio = precio + 20000
    elif Color == 'Negro':
        precio = precio + 30000

    print ("Sr/a " + Nombre + " usted selecciono el auto marca  " + Marca + " con " + Puerta + " puertas, color " + Color)
    print (" El precio es " + str (precio) + " pesos")

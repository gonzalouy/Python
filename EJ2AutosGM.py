condicion = False
i = 0
while condicion == False:
    if i == 4:
        condicion = True
    Nombre = input("Ingrese Nombre y apellido  ")
    Marca = input("Ingrese marca deseada  ")
    Puerta = input("Ingrese cantidad de puertas  ")
    Color = input("Ingrese color  ")

    if Marca == 'Ford':
        valor = 100000
    elif Marca == 'Chevrolet':
        valor = 120000
    elif Marca == 'Fiat':
        valor = 80000
    if Puerta == '2':
        valor1 = 50000
    elif Puerta == '4':
        valor1 = 65000
    elif Puerta == '5':
        valor1 = 78000
    if Color == 'Blanco':
        valor2 = 10000
    elif Color == 'Azul':
        valor2 = 20000
    elif Color == 'Negro':
        valor2 = 30000

    precio = (valor + valor1 + valor2)

    print("Sr/a " + Nombre + " usted selecciono el auto marca  " + Marca + " con " + Puerta + " puertas, color " + Color)
    print(" El precio es " + str(precio) + " pesos")
    i = i + 1
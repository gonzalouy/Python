#Calculo del Promedio

def Calculo_Promedio(Nota_matematicas, Nota_literatura, Nota_fisica):
    Valor = ((Nota_matematicas + Nota_literatura + Nota_fisica) / 3)
    return Valor

#Imprimir datos
def datos_del_alumno (Nombre,Apellido,Promedio):
    print('La nota promedio de ' + (str(Nombre)) + ' ' + (str(Apellido)) + ' es ' + (str(Promedio)))

def aprobacion(Promedio):
    if Promedio < 4:
        print('Insuficiente')
    if 4 <= Promedio <= 5.99999:
        print('A recuperatorio')
    if Promedio >= 6:
        print('Aprobado')
        if Promedio >= 9:
            print('Alumno destacado')
    else:
        Promedio = 0



#Ingreso de datos

Nombre = input('Ingrese su nombre ')
Apellido = input('Ingrese su apellido ')
Nota_matematicas = int(input('Ingrese la nota de matematicas '))
Nota_literatura = int(input('Ingrese la nota de literatura  '))
Nota_fisica = int(input('Ingrese la nota de fisica '))


Promedio=Calculo_Promedio(Nota_fisica,Nota_matematicas, Nota_literatura)
datos_del_alumno(Nombre,Apellido,Promedio)
aprobacion(Promedio)



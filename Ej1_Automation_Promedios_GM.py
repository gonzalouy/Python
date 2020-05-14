"""Programa de calculo de promedios
Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
Se pide imprimir el nombre, el apellido y el promedio.
Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". Caso contrario, si tiene menos de 4 puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado"""


#Defino variables y pido datos de entrada

Nombre = input('Ingrese su nombre ')
Apellido = input('Ingrese su apellido ')
Nota_matematicas = int(input('Ingrese la nota de matematicas '))
Nota_literatura = int(input('Ingrese la nota de literatura  '))
Nota_fisica = int(input('Ingrese la nota de fisica '))

#Calculo de promedio de notas

#Funcion de calculo del Promedio

def Calculo_Promedio():
    Valor = ((Nota_matematicas + Nota_literatura + Nota_fisica) / 3)
    return Valor

#Asigno el resultado del calculo de la funcion a la variable Promedio

Promedio=Calculo_Promedio()

print('La nota promedio de ' + (str(Nombre)) + ' ' + (str(Apellido)) + ' es ' + (str(Promedio)))

#Dependiendo del valor de Promedio imprimo el resultado final

if Promedio < 4:
    print('Insuficiente')
if 4 <= Promedio <= 5.99999:
     print ('A recuperatorio')
if  Promedio >= 6:
    print ('Aprobado')
    if Promedio >= 9:
        print('Alumno destacado')
else:
     Promedio=0
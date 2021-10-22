#Python essentials CEC 2021
#Roberto Rojas 
#Parte 1
#Crear un código capaz de mostrar en partalla lo siguiente:
print("Empezando a trabajar con Python")
print("Realizado por Roberto Rojas")
print("Consultando los tipos de valores")

#Declaración de todas las variables
var1=875
var2=4.89
var3="Now is better than ever"
var4=1.32
var5=5+8j
var6=8.2
var7="Readability counts"

#Despliegue de avisos según los datos
print("El tipo de dato de ",var1," es: \n",type(var1))
print("El tipo de dato de ",var2," es: \n",type(var2))
print("El tipo del texto: ",var3,", es: \n",type(var3))
print("El tipo de dato de ",var4," es: \n",type(var4))
print("¿El valor ",var5," corresponde a un valor entero? \n",isinstance(var5,int))
print("¿El valor ",var6," corresponde a un valor entero? \n",isinstance(var6,int))
print("¿El texto: ",var7,", corresponde a un string? \n",isinstance(var5,str))

'''
#Parte 2
#Desarrollar un código que permita mostrar en pantalla lo siguiente:
print("Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones:")

for i in range (5):
    var1=input("Interacción " + str(i+1) + ". Ingrese un valor cualquiera: ")
    print("Este tipo de dato en Python es: \n", type(var1))
    '''
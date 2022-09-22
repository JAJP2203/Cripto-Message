#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:51:15 2021

@author: José A Juárez_A00572186

Este programa va a desencriptar un mesaje por medio del algoritmo de RSA

Variables de entrada:
    bloques = numero de bloques ingresado por el usuario y los cuáles van a ser desencriptados
    lista = Lista en donde se van a ir guardando los numeros 
    num = Lista en donde se van a encontrar todos los bloques encriptados juntos y que vamos a usar en operaciones
    clave_n = Primer número de la clave privada
    clave_d = Segundo número de la clave privada

Variables de salida:
    desencriptacion = Los bloques de numeros ya desencriptados por el algoritmo RSA.
    coc = El primer número, ya decifrado (letra), del bloque. Este esta dentro de un ciclo for y por ende va a aplicar para todos los bloques.
    res = El segundo número, ya decifrado (letra), del bloque. Este esta dentro de un ciclo for y por ende va a aplicar para todos los bloques.

A continuación explicare como funciona el sig. programa:
    
    Primero se crea un diccionario, en donde, se ponen los valores númericos 
    de todas las letras del abecedario. Así mismo, se incluye el espacio.

Después, le pide al usuario que ingrese su mensaje encriptado, este obligatoriamente
debe de estar en bloques o números enteros. Así mimso, se le va a preguntar la cantidad 
de bloques/numeros que tiene.

Luego, se crea unas lista, en donde se juntan todos los bloques, se va a utilizar después.

Finalmente, se le pide al usuario que ingrese su clave privada, siempre dos numeros (n,d),
y con esto el algoritmo desencripta su mensaje. Así mismo, la salida se imprime el 
la oración completa con espacios y en mayúsculas.

El código contiene pequeños mensajes, en cada área, para explicar mejor los conceptos.

"""
#Inicializamos el diccionario, pero a diferencia al programa de encriptación, primero ponemos el valor número y después la letra porque ahora queremos saber el valor de la letra en base al número.
dic = {0:" ", 1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"i", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z"}
print("""
      Bienvenido, este programa tiene como función desencriptar mensajes 
      por medio del algoritmo RSA. Nota Importante, el mensaje debió haber
      sido encriptado por este mismo algoritmo. Así mismo, debe de contar con su
      clave privada (n,d), la cual ya se la debió de haber proporcionado por el 
      remitente o persona que le dio el mensaje encriptado, para poder desencriptar el mensaje.
      
      IMPORTANTE: Si se escribe incorrectamente un valor, el programa va a dar error y va 
      a tener que volver a correr el programa.
      """)
#Preguntamos por los bloques de número (variable de entrada)
bloques = int(input("De cuantos bloques (numeros) se compone su mensaje encriptado?  "))
num = []

for i in range(bloques):
    lista = int(input(f"Ingrese el bloque (número) {i+1} de su mensaje: "))
    num.append(lista)

#Inicio proceso de desencriptación por medio de algoritmo RSA
print("\nA continuación ingrese los dos numeros que componen su clave privada (n,d)")
clave_n = int(input("Inserte el primer numero de su clave privada (número entero) n: "))
clave_d = int(input("Inserte el segundo numero de su clave privada (número entero) d: "))

desencriptacion = []

for j in num:
    descrip = pow(j,clave_d,clave_n)#Pow sirve para elevar a una potencia.
    desencriptacion.append(descrip)
#print(f"\nSu mensaje desencriptado en bloques (numeros) es el siguiente: {desencriptacion}")

#Decifrar los valores, es decir, convertirlos de regreso a una cadena de caracteres

print("Su mensaje desencriptado es el siguiente: ")
for j in desencriptacion:
    coc = j // 27
    res = j % 27
    print(dic[coc], end="" + dic[res]) 

#Aquí se le pone el parámetro " end="" " para que no haga salto de línea y el mensaje se junte. Como esta esta dentro del ciclo for, todas las letras de todos los bloques se van a juntar hasta terminar de formar la oración.
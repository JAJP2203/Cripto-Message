#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:47:18 2021

@author: José A Juárez_A00572186

Este programa va a encriptar un mensaje por medio del algoritmo RSA.

Variables de entrada:
    m = mensaje ingresado por el usuario y el cuál va a ser encriptado
    num1 = Una lista en donde se van a guardar los valores impar o las letras que estan en lugar impar para poder separar bloques de dos letras
    num2 = Una lista en donde se van a guardar los valores par o las letras que estan en lugar par para poder separar bloques de dos letras
    num = Lista en donde se van a encontrar todos los valores juntos 
    final = Lista en donde se van a encontrar los bloques de numero
    clave_n = Primer número de la clave pública
    clave_e = Segundo número de la clave pública

Variables de salida:
    encriptacion = Los bloques de numeros ya encriptados por el algoritmo RSA.

A continuación explicare como funciona el sig. programa:
    
    Primero se crea un diccionario, en donde, se ponen los valores númericos 
    de todas las letras del abecedario. Así mismo, se incluye el espacio.

Después, le pide al usuario que ingrese un mensaje, este puede ser escrito en 
minúsuclas o mayúsculas. Sin embargo, es importante que se respeten los espacios, en
el caso de que sea una oración.

Luego, se crean unas listas, en donde se clasifican algunos valores (numeros par e impar), y con estos
se hace un algoritmo para cifrar las letras a numeros.

Finalmente, se le pide al usuario que ingrese su clave pública, siempre dos numeros (n,e),
y con esto el algoritmo encripta su mensaje. Así mismo, la salida se da en forma de 
lista con bloques de números.

El código contiene pequeños mensajes, en cada área, para explicar mejor los conceptos.

"""
#Inicializamos el diccionario, nos va a servir para asignarle numeros a las letras
dic = {" ":0, "A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}

print("""
      Bienvenido, este programa tiene como función encriptar mensajes 
      por medio del algoritmo RSA. Nota importante: va a necesitar su clave 
      pública (n,e) para que así el programa pueda encriptar el mensaje. 
      
      IMPORTANTE: Si se escribe incorrectamente un valor, el programa va a dar error y va 
      a tener que volver a correr el programa.
      """)
#Preguntamos por el mensaje (Variable de entrada)
m = input("Introduzca el mensaje que quiera cifrar: ")
l = len(m)
if l % 2 != 0:
    m = m + " "
#Crear listas para guardar valores
m = m.upper()
num = []
num1 = []
num2 = []
final = []

#Dividir las letras en las pares e impares
for i in m:
    num.append(dic[i])   
num1 = (num[ :: 2])
num2 = (num[1 :: 2])
contador = 0

#Algoritmo para cifrar las letras a numeros
for cod in num1:
    x = cod * 27 #Primera letra se multiplica por el módulo del diccionario, en este caso son 27.
    y = x + num2[contador] #Segunda letra se suma al resultado de multiplicar primer número con módulo
    contador = contador + 1
    final.append(y)

#Inicio proceso de encriptación por medio de Algoritmo RSA
print("\nA continuación ingrese los dos numeros enteros que componen su clave pública (n,e)")
clave_n = int(input("Inserte el primer número de su clave pública (número entero-módulo) n: "))
clave_e = int(input("Inserte el segundo número de su clave pública (número entero-exponente) e: "))
encriptacion = []

for e in final:
    crip = pow(e,clave_e,clave_n)
    encriptacion.append(crip)
    
print(f"\nSu mensaje encriptado en bloques (numeros) es el siguiente: {encriptacion}")


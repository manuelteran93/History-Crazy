# import random
# moneda_al_aire = random.randint(0, 1)
# if moneda_al_aire == 1:
#     print("Cara")
# else:
#     print("Sello")

# frutas = ["Fresas", "Nectarinas", "Manzanas", "Uvas", "Melocotones", "Cerezas", "Peras"]
#
# for fruta in frutas:
#     print(fruta)
#     print(fruta + " Pie ")
# print(frutas)


#PROGRAMA DE CALCULADORA DE ALTURA DE ESTUDIANTES

# estudiantes_altura = input("[ingrese las alturas]").split()
#
#
# #suma las alturas de todos los estudiantes e imprime la altura total
#
# total_altura = 0
# for altura in estudiantes_altura:
#   total_altura += int(altura)
# print(f"Total altura = {total_altura}")
#
# #cuenta cuántos estudiantes hay e imprime el número.
# #156 178 165 171 187
# numero_de_estudiantes = 0
# for estudiante in estudiantes_altura :
#   numero_de_estudiantes += 1
# print(f"Numero de estudiantes = {numero_de_estudiantes}")
#
#
# porcentaje_de_altura = round(total_altura / numero_de_estudiantes)
# print(f"EL Promedio de total de altura es : {porcentaje_de_altura}")


#PROGRAMA DE CALCULADORA DE PUNTUACION
# 78 65 89 86 55 91 64 89
# estudiantes_promedios = input("[ingrese los promedios]").split()
#
# max = sorted(estudiantes_promedios)[-1]
#
# print(max)


# sum = 0
# for even_number in range(0,101,2):
#     sum += even_number
# print (sum)

#PROGRAMA DE ENTREVISTA
# Su programa debe imprimir cada número del 1 al 100 por turno.
# Cuando el número es divisible por 3, en lugar de imprimir el número,
# debe imprimir "Fizz". `Cuando el número es divisible por 5, entonces
# en lugar de imprimir el número debe imprimir "Buzz".` `Y si el número
# es divisible por 3 y 5, p. 15 entonces, en lugar del número, debería
# imprimir "FizzBuzz"`

# for numero in range (1, 100):
#     if numero % 3 == 0 and numero % 5 == 0:
#         print("FizzBuzz")
#     elif numero % 3 == 0:
#         print("Fizz")
#     elif numero % 5 == 0:
#         print(("Buzz"))
#     else:
#         print(numero)


# #PROGRAMA DE GENERAR CONTRASEÑA
#
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# password_list = []
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")

# def greet():
#   print("hello")
#   print("hi")
#   print("cualquiera")


# greet()
#
# def greet(name):
#   print("hello    ")
#   print("hi")
#   print("cualquiera")
#
#
# greet()

# numero = (((3 + 2) / (2 * 5)) ** 2)
# print(numero)
#
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
# coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

# horas_atrabajar = int(input(" Hola Cuantas Horas Trabajaste esta Semana : ?  \n "))
# costo_de_hora = int(input(" A cuanto te pagaron la hora esta Semana : ?  \n "))
#
# total_de_pago = horas_atrabajar * costo_de_hora
# print(f" El total a pagar son {total_de_pago} $ ")

# Escribir un programa que lea un entero positivo, n , introducido por el usuario y des
# pués muestre en pantalla la suma de todos los enteros desde 1 hasta n . La suma de lo
# n primeros enteros positivos puede ser calculada de la siguiente forma:

# n = int(input("Ingrese un numero entero \n  "))
#
# suma = round( n * (n + 1 ) / 2 )
#
# print(suma)

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule
# el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la
# frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa
# corporal calculado redondeado con dos decimales.
#
# peso = int(input("Cuanto pesas en kg ? \n "))
# altura = float(input("Cual es tu alruta ? \n"))
#
# icm = round((peso) / (altura)**2 , 2)
#
# print(f" Tu icm es {icm} " )


# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
# la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son lo
# números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la divi
# sión entera respectivamente.

# n = int(input("Escriba un primer numero  ? \n "))
# m = int(input("Escriba un segundo? \n "))
#
# print( n / m)



# def case(nombre, pais, ciudad):
#     print(f"Hola cual es {nombre} ?")
#     print(f"En que {ciudad} vives ?")
#     print(f"En que {pais} queda? ")
#
# case(nombre="Jesue" ,  pais="Venezuela" , ciudad="Guanare")


# import math  #para redondear
# def pinturas( height, width, cover):
#     calculo = test_h * test_w
#     numero_de_latas = math.ceil(calculo / covering)  #math.ceil numero entero redondearlo al maximo
#     print(f"Se necesitaran {numero_de_latas} para pintar ")
#
#
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# covering = 5
#
# pinturas(height=test_h, width=test_w, cover=covering)

#PROGRAMA PARA SABER QUE AUTO TE GUSTA

# print (("Mi perro Renzo")[::-1])

# uno = 10
# dos = 10
# if dos > uno :
#     print("Es mayor")
# elif uno == dos:
#     print("Es Igual")
# elif uno > dos:
#     print("Es Mayor")
# else:
#     print("Es diferente")

# uno = ["Lunes", "Martes", "Miercoles", "Jueves" , "Viernes"]
# if "Martex" in uno:
#     print("Se encontro")
# else:
#     print("no se encontro")

# uno = 10
# if uno < 10:
#     if uno > 20:
#         if uno == 11:
#             print("ok")
#         else:
#             print()
#
# else:
#     print("ninguno se cumple")


# uno = 10
# dos = 20
#
# if uno == dos and uno > 2:
#     print("ok")
# else:
#     print("son diferentes")


#bucles

# primera = 1
#
# while primera < 11:   #no se ejecutara hasta que primera valga menor que 11
#     print("EL valor es : " , primera)
#     primera = primera + 1  # se le va sumando una unidad en el final


#recorridos dentro de la variable usamos for
#for devuelve la cantidad de elementos que tenemos
# primera = "Hola Mundo"
# for uno in primera:
#     print(uno)


#def se usan para llamar varias veces la funcion
#se debe cerrar con la funcion definida.
# def saludo(#parametro):
#     print("Hola a todos")
# saludo()
# saludo()
# saludo()

# def suma(uno, dos):
#     print(uno + dos )
# suma(10 ,20)

#TUPLAS NO SE PUEDEN CAMBIAR UNA VEZ CREADAS
# uno = (10 , 20, 30, 40, "Yoney")
# print(uno[:5])

# uno = (10 , 20, 50, 80, "Yoney")
# indice = 0
# while indice < len(uno):
#     print(uno[indice])
#     indice = indice + 1

# #CADENAS
# uno = "Hola"
# dos = "mundo"
# tres = uno + " " + dos
# print(tres)

#CADENA COCATENACION
# uno = "hola"
# dos = "mundo"
# tres = "saludo : {0} {1}" . format(uno,dos)
# print(tres)

# #COCATENACION
# uno = "hola mundo \n "
# print(uno * 10)

# uno = "hola mundo"
# uno += "es un saludo"
# print(uno)

uno = {"a" : 10, "b": 20}
help(uno)
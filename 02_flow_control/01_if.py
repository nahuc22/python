###
# 01 - Sentencias condicionales (if, elif, else)
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()


print("\n Sentencia simple condicional")

edad = 28

if edad >= 28:
    print("Eres mayor de edad")
    print("Felicidades hahahaha")

edad = 16
if edad <= 15:
    print("Acá se la pela si no cumple directamente")

print("\n Sección de elseif")

nota = 15 

if nota >= 8:
    print("Eri buenazo")
elif nota >=6:
    print("Eri bueno cacho")
elif nota >= 5:
    print("Aprobadiño")
else:
    print("No wnnnn!")    


# Javascript
# && --> and
# || --> or
print("\n Condiciones multiples")
edad = 25
tiene_carnet = False

#&&
if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("POLICIAA!!!!")

# ||
if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
else:
    print("Coimita y podes zafar")

# !
es_fin_de_semana = False
# Javascript => !
if not es_fin_de_semana:
    print("Venga cachi que hay que laburar jaja")

tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

if edad < 18:
    print("No puedes entrar a la disco")
elif tiene_dinero:
    print("Puedes ir a la discoteca")
else:
    print("Quedate en casa")

numero = 5
if numero:
    print(f"El número {numero} no es cero")

numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
    print(f"El numero es {numero}")

# ternario    

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)


# print("\nEjercicio 1:")

# num1 = input("Escribe el primero número:")
# num2 = input("Escribe el segundo número:")

# if num1 > num2:
#     print(f"{num1} es mayor")
# elif num1 < num2:
#     print(f"{num2} es mayor")
# else:
#     print("Los números son iguales")

# print("\nEjercicio 2:")
# print("\n")

# num1 = input("Escribe el primero número:")
# num2 = input("Escribe el segundo número:")
# operacion = input("Elija si quiere elija su operación:")


# suma = True
# resta = True
# divi = True
# multi = True

# if suma:
#     total = int(num1) + int(num2)
#     print(f"{total}")


###
# 03 - Listas
# Secuencias mutables de elementos
# Puede contener elementos de diferentes tipos.
###

print("\nCrear listas")
lista1 = [1, 2 ,3 , 4 ,5] # lista de enteros
lista2 = ["manzanas", "peras", "bananas"] # lista de cadenas
lista3 = [1, "hola", 3.14 , True] #lista de tipos

lista_vacia = []
lista_de_listas =[[1,2], [3, 4]]
matrix = [[1, 2], [2,3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

#Acceso a elemtos por índice
print("\nAcceso a elementos")
print(f"lista 2 indice 0: {lista2[0]}")

#Listas de listas
print(lista_de_listas[1][0])

# Slicing (cortesuki)
print(f"lista1[1:4]: {lista1[1:4]}") # [2,3,4]
print(f"lista1[:3]: {lista1[:3]}") # [1,2,3]
print(f"lista1[3:]: {lista1[3:]}") # [4,5]
print(f"copia de lista1[:]: {lista1[:]}") # [1,2,3,4,5]

# Hay más mágia
lista1 = [0, 1 ,2 ,3 ,4 ,5, 6, 7, 8, 9, 10]
print(f"Salteo de a 2: {lista1[::2]}")
print(f"Invertida: {lista1[::-1]}")

#Modificar listas
lista1[0] = 20
print(f"Modificando indice 0:{lista1}")

# Añadir elementos a una lista
lista1 = [1,2,3]
lista1 = [1,2,3] + [4,5,6]
print(lista1)

# Forma picante
lista1 += [7,8,9]
print(lista1)

#Recuperar longitud
print("Longitud de la lista es:", len(lista1))

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
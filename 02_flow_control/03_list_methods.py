###
# 03 - Listas con métodos"
# Metodos más importantes
###

from os import system
if system("clear") != 0: system("cls")

lista1 = ["a", "b", "c" , "d" , "e"]

###Agregar

#Agrega al último indice
lista1.append("f")
print(lista1)

#Inserta en el indice el valor
lista1.insert(1, "@")
print(lista1)

#Varios valores al final de la lista
lista1.extend(["correr", "caminar", "dormir"])
print(lista1)

###Borrar

# Por coincidencia
lista1.remove('@')
print(lista1)

# Remueve y devuelve el último
ultimo = lista1.pop()
print(ultimo)

# Elimina el indice
indice1 = lista1.pop(1)
print(lista1)
print(indice1)

# Delete
del lista1[-1]
print(lista1)

lista1.clear() # Borra todo
print(lista1)

lista1 = ["panda", "gato", "perro", "kanguro", "tortuga"]
del lista1[1:3]
print(lista1)

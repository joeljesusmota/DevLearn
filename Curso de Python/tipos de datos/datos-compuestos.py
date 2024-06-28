#creando una lista (se pueden modificar)
lista = ["Hola soy Mota", "Como estas", True, 5.9]

#creando una tupla ( no se pueden modificar)
tupla = ("Hola soy Mota", "Como estas", True, 5.9)

#esto es valido
lista[3] = "Maquinola"

#esto no es valido
#tupla[3] = "Maquinola"

#creando un conjunto (set) 
    # podemos redefinir pero no modificar sus elementos
    # no podemos acceder a sus elementos a travez de un indice, sino mas bien a travez de un bucle
    # no almacena datos duplicados
    # almacena los datos de manera desordenada
conjunto = {"Hola soy Mota", "Como estas", True, 5.9, "Hola soy Mota"}

# crando un diccionario (dict)
# la estructura es Key : Value y separamos con comas
diccionario = {
    'nombre' : "Joel Mota",
    'profesion' : "Policia",
    'esta_emocionado' : True
}
print(diccionario['profesion'])

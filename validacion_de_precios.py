"""
Escribí un programa que permita al usuario ingresar el precio de un producto, 
pero que sólo acepte valores mayores a 0. Si el usuario ingresa un valor inválido (negativo o cero),
el programa debe mostrar un mensaje de error, y volver a pedir el valor hasta que se ingrese uno válido. 
Al final, el programa debe mostrar el precio aceptado.

Tips: 
Antes de empezar, pensá si es necesario usar contadores o acumuladores.
Recordá que input() siempre devuelve cadenas de caracteres.
"""

lista_nombre_art_con_precio = []
nombre_artiulo = None

# Menu de Opciones
print()
print("Menu de Gestion de Productos\n")
print("1. Alta de productos nuevos")
print("3 Salir\n")

# Solicitar al usuario que selecione una opcion
while True:
    opcion = int(input("ingrese 1 para dar de alta o 3 para salir (1 - 3)  "))

    # Mostramos la opcion seleccionada
    print(f"Has seleccionado la opcion: {opcion}\n")

    if opcion == 1:
        nombre_artiulo = str(input("Ingrese el nombre del producto: "))
        lista_nombre_art_con_precio.append(nombre_artiulo)
        precio_art = float(input("ingrese precio unitario: "))
        if precio_art > 0:
            lista_nombre_art_con_precio.append(precio_art)
        else:
            while precio_art <= 0:
                print(
                    "Error, el precio debe ser mayor a 0. Por favor, ingrese un nuevo valor:  "
                )
                precio_art = float(input("ingrese precio unitario: "))
                if precio_art > 0:
                    lista_nombre_art_con_precio.append(precio_art)

    elif opcion == 3:
        print("Salir")
        break
    else:
        print("La opción es incorrecta\n")

print(lista_nombre_art_con_precio)

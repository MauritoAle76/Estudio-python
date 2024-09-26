"""" encunciado del primer problema

Crea un programa que solicite al usuario dos números enteros. 
Realiza las siguientes operaciones: suma, resta, multiplicación, y módulo. 
Muestra el resultado de cada operación en un formato claro y amigable. 
Asegúrate de incluir mensajes personalizados que expliquen cada resultado, por ejemplo: "La suma de tus números es: X".
"""

# # variables
numero_1 = 0
numero_2 = 0

# imput

numero_1 = int(input("Ingrese el primer numero  "))
numero_2 = int(input("Ingrese el segundo numero "))


# operaciones matematicas

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multipicacion = numero_1 * numero_1 * numero_2
modulo = numero_1 % numero_2  # modula me da el resto de la division

# print de las operaciones realizadas
# print()

print(f"Usted ingreso los siguientes numeros, {numero_1} y {numero_2} ")
print()
print(f"La suma de los numeros ingresados es {suma} ")
print()
print(f"La resta de los numeros ingresados es {resta} ")
print()
print(f"La multiplicacion de los numeros ingresados es {multipicacion} ")
print()
print(f"El modulo resultante de la division de los numeros ingresados es {modulo} ")
print()


""" Ejercicio 2

Escribe un programa en Python que calcule la propina que se debe dejar en un restaurante. 

El script debe solicitar al usuario el monto total de la cuenta y el porcentaje de propina que desea dejar.
 
Utilizando operadores aritméticos, calcula la cantidad de propina y el total a pagar (incluyendo la propina). 
Finalmente, muestra los resultados en la pantalla

"""
print()
print("VAMOS A CALCULAR LA PROPINA")
print()

monto_total_de_la_cuenta = 0
porcentaje_de_la_propina = 0


# preguntar al usuario

monto_total_de_la_cuenta = float(
    input("Estimados, por favor ingrese el monto total de la cuenta en pesos  ")
)

print()
porcentaje_de_la_propina = float(
    input("Por favor indique el porcentaje que esta dispuesto a pagar de propina   ")
)

print()

print(
    "Muchas Gracias por la informacion, estamos calculando el monto de propina y el total a pagar"
)
print()

# calculos de total de propina y el monto total a pagar

calculo_de_propina = monto_total_de_la_cuenta * porcentaje_de_la_propina / 100

monto_total_mas_propinas = monto_total_de_la_cuenta + calculo_de_propina

# print

print(
    f"El monto total informado es pesos: {monto_total_de_la_cuenta} mas la propina del : {porcentaje_de_la_propina} %, esto nos da un importe final a pagar de $ {monto_total_mas_propinas}.-"
)
print()

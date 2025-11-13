# PROYECTO LÓGICA: Katas de Python

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
# de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(cadena):
    frecuencia = {}
    for letra in cadena:
        if letra != ' ':
            if letra not in frecuencia:
                frecuencia[letra] = 0
            frecuencia[letra] += 1
    return frecuencia

# print(frecuencia_letras("katas de python"))

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

def duplicar_numeros(lista):
    return list(map(lambda x: x * 2, lista))

# print(duplicar_numeros([43, 2, 29, 4, 1]))

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe 
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista_palabras, palabra_objetivo):
    lista_palabras_filtradas = []
    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            lista_palabras_filtradas.append(palabra)
    return lista_palabras_filtradas

# print(filtrar_palabras(["python", "java", "kotlin", "javascript"], "java"))

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

# print(diferencia_listas([10, 20, 30], [1, 2, 3]))

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

def evaluar_nota(lista_numeros, nota_aprobado=5):
    media = sum(lista_numeros) / len(lista_numeros)
    
    if media >= nota_aprobado:
        estado = "aprobado"
        return (media, estado)
    else:
        estado = "suspenso"
        return (media, estado)
    
# print(evaluar_nota([6, 7, 8, 5, 4]))

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# print(factorial(3))

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda x: x[0] + " " + x[1], lista_tuplas))

# print(tuplas_a_strings([("Claudia", "R"), ("Martí", "M"), ("Bruna", "G")]))

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no 
# numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

def dividir_numeros():
    num1 = input("Ingresa el primer número: ")
    num2 = input("Ingresa el segundo número: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Error: Debes ingresar valores numéricos."
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    return "La división fue exitosa. El resultado es: " + str(num1 / num2)

# print(dividir_numeros())

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
# "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

def mascotas_legales(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda x: x not in mascotas_prohibidas, lista_mascotas))

# print(mascotas_legales(["Perro", "Gato", "Tigre", "Loro", "Oso"]))

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza 
# una excepción personalizada y maneja el error adecuadamente.

def promedio(lista_numeros):
    if len(lista_numeros) == 0:
        return "Error: La lista está vacía."
    return sum(lista_numeros) / len(lista_numeros)

# print(promedio([1, 5, 2, 10]))
# print(promedio([]))

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o 
# un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def edad_usuario():
    edad = input("Introduce tu edad: ")

    try:
        edad = int(edad)
    except ValueError:
        return "Error: Debes ingresar un valor numérico."
    if float(edad) < 0 or float(edad) > 120:
        return "Error: Edad fuera de rango."
    
    return "Edad: " + str(edad)

# print(edad_usuario())

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map().

def longitud_palabras(frase):
    lista_palabras = frase.split()
    return list(map(lambda x: len(x), lista_palabras))

# print(longitud_palabras("Katas de Python"))

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

def letras_mayus_minus(conjunto):
    # Set convierte el string en un conjunto sin elementos repetidos (y desordenados)
    conjunto = set(conjunto)
    #Eliminar espacios
    conjunto.discard(' ')
    return map(lambda x: (x.upper(), x.lower()), conjunto)

# print(list(letras_mayus_minus("Katas de Python")))

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. 
# Usa la función filter().

def empieza_con(lista_palabras, letra):
    # filter pide una función y una lista
    lista = list(filter(lambda x: x[0] == letra, lista_palabras))

    return lista

# print(empieza_con(["Katas", "de", "Python", "Kotlin", "Java"], "K"))

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

def sumar_tres(lista_numeros):
    return list(map(lambda x: x + 3, lista_numeros))

# print(sumar_tres([1, 2, 3, 4, 5]))

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas 
# las palabras que sean más largas que n. Usa la función filter().

def palabras_mas_largas(texto, n):
    lista_palabras = texto.split()
    return list(filter(lambda x: len(x) > n, lista_palabras))

# print(palabras_mas_largas("Estoy practicando con Katas de Python para recordar lo que aprendí hace un tiempo", 4))

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde 
# al número quinientos setenta y dos (572). Usa la función reduce().

from functools import reduce

def agregar_digito(x, y):
    return x * 10 + y

def lista_a_numero(lista_digitos):
    # reduce aplica la función 'agregar_digito' de forma acumulativa a los elementos de la lista
    return reduce(agregar_digito, lista_digitos)

# print(lista_a_numero([5, 7, 2, 4, 1, 9]))

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, 
# edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa 
# la función filter().

def estudiantes_aprobados(lista_estudiantes):
    # lambda que filtra los estudiantes que en su diccionario con clave 'calificación' tienen un valor mayor o igual a 90
    return list(filter(lambda x: x['calificación'] >= 90, lista_estudiantes))

# print(estudiantes_aprobados([{'nombre': 'Ana', 'edad': 20, 'calificación': 95}, 
# {'nombre': 'Luis', 'edad': 22, 'calificación': 85},
# {'nombre': 'Marta', 'edad': 21, 'calificación': 90}]))

# 19. Crea una función lambda que filtre los números impares de una lista dada.

def filtrar_impares(lista_numeros):
    # % devuelve el residuo de la división, es impar si no es divisible entre 2
    return list(filter(lambda x: x % 2 != 0, lista_numeros))

# print(filtrar_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función 
# filter().

def es_entero(x):
    try :
        int(x)
        return 1
    except ValueError:
        return 0

def filtrar_int(lista_elementos):
    return list(filter(es_entero, lista_elementos))

# print(filtrar_int([1, 'dos', 3, 'cuatro', 5, 'seis']))

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
# No veo la necesidad de utilizar lambda.
def cubo(numero):
    return (lambda x: x ** 3)(numero)

# print(cubo(3))

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce(). 

def producto (x, y):
    return x * y

def producto_total(lista_numeros):
    return reduce(producto, lista_numeros)

# print(producto_total([1, 2, 3, 4, 5]))

# 23. Concatena una lista de palabras. Usa la función reduce().

def concatena_dos (palabra1, palabra2):
    return palabra1 + " " + palabra2

def concatena_todo(lista):
    return reduce(concatena_dos, lista)

# print(concatena_todo(["Este", "proyecto", "me", "parece", "interesante"]))

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

# Con funcón lambda
def resta_total (lista_numeros):
    return reduce(lambda x, y: x - y, lista_numeros)

# print(resta_total([100, 13, 50, 2]))

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    return len(cadena)

# print(contar_caracteres("Katas de Python"))

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
# No veo la necesidad de utilizar lambda.

def residuo_division(num1, num2):
    return (lambda x, y: x % y)(num1, num2)

# print(residuo_division(5,2))

# 27. Crea una función que calcule el promedio de una lista de números.

def promedio(lista_numeros):
    if len(lista_numeros) == 0:
        return "Error: La lista está vacía."
    return sum(lista_numeros) / len(lista_numeros)

# print(promedio([0, 20, 30, 40, 60]))

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return "Error: No se encontraron elementos duplicados."

# print(primer_duplicado([1, 2, 3, 4, 5, 6, 7, 2, 8, 9, 3]))

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el 
# carácter '#', excepto los últimos cuatro.

def enmascarar_variable(variable):
    texto = str(variable)
    # Tantos '#' como caracteres menos 4, texto[inicio:fín:paso] marco el inicio como -4 para contar desde el final
    return (len(texto)-4) * '#' + texto[-4:]

#print(enmascarar_variable(1234567890))

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
# pero en diferente orden.

def anagramas(palabra1, palabra2):
    vistos = set()
    for letra in palabra1:
        vistos.add(letra)
    for letra in palabra2:
        if letra not in vistos:
            return False
        
    if len(palabra1) != len(palabra2):
        return False
    else:
        return True
    
# print(anagramas("lacteo", "coleta"))

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar 
# en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, 
# se lanza una excepción.

def buscar_nombre():
    lista_nombres = input("Ingresa una lista de nombres: ").split(' ')
    nombre_a_buscar = input("Ingresa el nombre que deseas buscar: ")

    try:
        if nombre_a_buscar in lista_nombres:
            return "Nombre encontrado."
        else:
            raise ValueError("Error: Nombre no encontrado en la lista.")
    except ValueError as e:
        return str(e)
    
# print(buscar_nombre())

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
# no trabaja aquí.

def buscar_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado['nombre'] == nombre_completo:
            return empleado['puesto']
    return "La persona no trabaja aquí."

# print(buscar_empleado("Martina Real", [{'nombre': 'Marta Pla', 'puesto': 'Ingeniera'}, {'nombre': 'Óscar Pérez', 'puesto': 'Diseñador'}, 
#                                     {'nombre': 'Martina Real', 'puesto': 'Directora'}]))

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

def sumar_listas(lista1, lista2):
    # Primer elemento de lista1 con primer elemento de lista2, segundo con segundo, etc.
    return list(map(lambda x, y: x + y, lista1, lista2))

# print(sumar_listas([1, 2, 3], [4, 5, 6]))


# 34. Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco,
# nueva_rama, crecer_ramas, quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.

class Arbol:
    # Inicializa el árbol con un tronco = 1 y una lista de ramas vacía
    def __init__(self, tronco = 1):
        self.tronco = tronco
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1) # Nueva rama de longitud 1

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            raise IndexError("Posición de rama inválida.")
    
    def info_arbol(self):
        print ("Tronco:", self.tronco)
        print ("Número de ramas:", len(self.ramas))
        print ("Longitud de las ramas:", self.ramas)

# Caso de uso
"""
arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
arbol.info_arbol()
"""

# 35. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona 
# métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Error: Fondos insuficientes para retirar.")
        self.saldo -= cantidad

    # Transfiere dinero desde otro usuario a este usuario
    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError("Error: Fondos insuficientes para transferir.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

# Caso de uso
"""
u1 = UsuarioBanco("Alicia", 100, True)
u2 = UsuarioBanco("Bob", 50, True)
u2.agregar_dinero(20)
u1.transferir_dinero(u2, 80)
u1.retirar_dinero(50)
print("Saldo de Alicia:", u1.saldo)
print("Saldo de Bob:", u2.saldo)
"""

# No hay enunciado 36.

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, 
# eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto . 
# Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):
    diccionario = {}
    palabras = texto.split(" ")
    # Añado palabra por palabra al diccionario, si ya existe incremento su contador
    for palabra in palabras:
        if palabra not in diccionario:
            diccionario[palabra] = 0
        diccionario[palabra] += 1
    return diccionario

def reemplazar_palabras(texto, palabra_nueva, palabra_vieja):
    palabras = texto.split(" ")
    # Utilizo enumerate para obtener el índice y la palabra
    for i, palabra in enumerate(palabras):
        if palabra == palabra_vieja:
            if palabra_nueva == "":
                # Elimino la palabra vieja si la nueva es cadena vacía (para evitar espacios dobles)
                palabras.pop(i)
            else:
                # Reemplazo la palabra vieja por la nueva
                palabras[i] = palabra_nueva

    # Transformo la lista de palabras de nuevo en texto 
    return (" ".join(palabras))

# He modificado la funcion de reemplazar_palabras para que sirva para eliminar palabras
def eliminar_palabra(texto, palabra):
    return reemplazar_palabras(texto, "", palabra)

def procesar_texto():
    selector = input("Selecciona una opción (1. contar, 2. reemplazar, 3. eliminar): ")
    match selector:
        case "1":
            texto = input("Ingresa el texto: ")
            return contar_palabras(texto)
        case "2":
            texto = input("Ingresa el texto: ")
            palabra_vieja = input("Ingresa la palabra a reemplazar: ")
            palabra_nueva = input("Ingresa la nueva palabra: ")
            return reemplazar_palabras(texto, palabra_nueva, palabra_vieja)
        case "3":
            texto = input("Ingresa el texto: ")
            palabra = input("Ingresa la palabra a eliminar: ")
            return eliminar_palabra(texto, palabra)
        case _:
            return "Error: Opción no válida."
        
# print(procesar_texto())

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def determinar_momento_dia():
    hora_minuto = input("Introduce la hora en formato (hh:mm): ")
    hora, minuto = map(int, hora_minuto.split(":"))

    if hora not in range(0, 24) or minuto not in range(0, 60):
        return "Error: Fuera de rango."

    if 6 <= hora <= 13:
        if hora == 6 and minuto >= 30 or hora > 6:
            return "Es de día, concretamente la mañana."
        else:
            return "Es de noche."
    elif 13 < hora < 20:
        return "Es de día, concretamente la tarde."
    else: 
        return "Es de noche."
    
# print(determinar_momento_dia())

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
# Las reglas de calificación son: 0 - 69 insuficiente, 70 - 79 bien, 80 - 89 muy bien, 90 - 100 excelente

def calificacion_texto():
    nota = input("Introduce la calificación numérica (0-100): ")

    try:
        nota = int(nota)
    except ValueError:
        return "Error: Debes ingresar un valor numérico."
    if nota < 0 or nota > 100:
        return "Error: Fuera de rango."
    
    if nota <= 69:
        return "Insuficiente"
    elif nota <= 79:
        return "Bien"
    elif nota <= 89:
        return "Muy bien"
    else:
        return "Excelente"
    
# print(calificacion_texto())

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y 
# datos (una tupla con los datos necesarios para calcular el área de la figura).

import math
def calcular_area(figura, datos):
    try:
        datos = tuple(map(float, datos))
    except ValueError:
        return "Error: Los datos deben ser numéricos."  
    
    match figura:
        case "rectangulo":
            largo, ancho = datos
            return largo * ancho
        case "circulo":
            radio = datos[0]
            return math.pi * radio ** 2
        case "triangulo":
            base, altura = datos
            return (base * altura) / 2
        case _:
            return "Error: Figura no reconocida."
        
# print(calcular_area("rectangulo", (5, 10)))
# print(calcular_area("circulo", (7, )))
# print(calcular_area("triangulo", (4, 8)))
        
# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final 
# de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:

#1. Solicita al usuario que ingrese el precio original de un artículo.
#2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

import unicodedata

def calcular_precio_final():
    precio_inicial = input("Ingresa el precio inicial del artículo: ")
    descuento = input("¿Tienes un cupón de descuento? (Sí/No): ")

    # Para evitar problemas con acentos y mayúsculas
    descuento_normalizado = unicodedata.normalize('NFKD', descuento).encode('ASCII', 'ignore').decode('ASCII')

    if descuento_normalizado.lower() == "si":
        valor_descuento = input("Ingresa el valor del cupón de descuento: ")
        try:
            precio_inicial = float(precio_inicial)
            valor_descuento = float(valor_descuento)
        except ValueError:
            return "Error: Debes ingresar valores numéricos."
        
        if valor_descuento > 0:
            # Aplico el descuento
            precio_final = precio_inicial - valor_descuento
        else:
            return "Error: El valor del cupón debe ser mayor a cero."
    else:
        try:
            precio_inicial = float(precio_inicial)
        except ValueError:
            return "Error: Debes ingresar un valor numérico."
        # No hay descuento
        precio_final = precio_inicial

    return "El precio final es: " + str(precio_final)

# print(calcular_precio_final())

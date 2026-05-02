"""
Calculadora v4 - Código modular con funciones
==============================================

En esta cuarta versión refactorizarás todo el código en funciones reutilizables.
Verás cómo el código se vuelve más limpio, mantenible y profesional.

Conceptos aplicados:
- Definición de funciones con def
- Parámetros y return
- Docstrings para documentación
- Separación de responsabilidades
- Patrón if __name__ == "__main__"

Instrucciones:
1. Crea funciones para cada operación matemática
2. Crea función para mostrar el menú
3. Crea función para obtener números del usuario
4. Organiza todo en una función main()
"""

# TODO 1: Define las funciones para cada operación matemática
# Cada función debe recibir dos parámetros (a, b) y devolver el resultado

def sumar(a, b):
    """Suma dos números.

    Args:
        a: Primer número
        b: Segundo número

    Returns:
        La suma de a y b
    """
    return a + b
    


def restar(a, b):
    """Resta dos números."""
    # TODO: Implementa la resta
    return a - b


def multiplicar(a, b):
    """Multiplica dos números."""
    # TODO: Implementa la multiplicación
    return a * b


def dividir(a, b):
    """Divide dos números.

    Args:
        a: Dividendo
        b: Divisor

    Returns:
        El resultado de a / b
    """
    # TODO: Implementa la división
    return a / b


# TODO 2: Crea una función para mostrar el menú
def mostrar_menu():
    """Muestra el menú de opciones de la calculadora."""
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    


# TODO 3: Crea una función para obtener dos números del usuario
def obtener_numeros():
    """Pide dos números al usuario y los devuelve.

    Returns:
        Una tupla con los dos números (num1, num2)
    """
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    return num1, num2
    


# TODO 4: Crea la función principal que contiene el bucle del programa
def main():
    """Función principal de la calculadora."""

    while True:
        # TODO 4.1: Muestra el menú llamando a la función mostrar_menu()
        mostrar_menu()

        # TODO 4.2: Pide la opción al usuario
        opcion = input("\nElige una opción: ")

        # TODO 4.3: Si elige salir, termina
        if opcion == "5":
             print("¡Hasta pronto! 👋")
             break

        # TODO 4.4: Valida que la opción sea válida
        if opcion not in ["1", "2", "3", "4"]:
            print("❌ Opción no válida")
            continue

        # TODO 4.5: Obtén los números llamando a la función obtener_numeros()
        num1, num2 = obtener_numeros()

        # TODO 4.6: Controla división por cero
        if opcion == "4" and num2 == 0:
            print("❌ No se puede dividir por cero")
            continue

        # TODO 4.7: Llama a la función correspondiente según la opción
        # Nota cómo ahora el código es mucho más limpio
        # if opcion == "1":
        #     resultado = sumar(num1, num2)
        #     simbolo = "+"
        # elif opcion == "2":
        #     resultado = restar(num1, num2)
        #     simbolo = "-"
        # elif opcion == "3":
        #     resultado = multiplicar(num1, num2)
        #     simbolo = "*"
        # elif opcion == "4":
        #     resultado = dividir(num1, num2)
        #     simbolo = "/"

        # TODO 4.8: Muestra el resultado
        # print(f"✅ {num1} {simbolo} {num2} = {resultado:.2f}")

    


# TODO 5: Punto de entrada del programa
# Este patrón permite que el archivo sea importable sin ejecutarse automáticamente
# if __name__ == "__main__":
#     main()


# ¡Excelente! Has refactorizado tu calculadora con funciones.
#
# Ventajas de esta versión:
# ✅ Cada función tiene una responsabilidad clara
# ✅ El código es reutilizable (puedes importar estas funciones en otros archivos)
# ✅ Es más fácil de leer y entender
# ✅ Es más fácil de probar (puedes testear cada función individualmente)
# ✅ Es más fácil de mantener y extender
#
# Prueba que funcione igual que la v3, pero nota cómo el código es más claro.
#
# 💡 En la v5 añadirás un historial de operaciones usando listas y diccionarios

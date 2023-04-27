def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        resultado = a / b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")


def main():
    a, b, c, d = (10, 5, 0, "Hola")

    print("{} + {} = {}".format(a, b, suma(a, b)))
    print("{} - {} = {}".format(b, d, resta(b, d)))
    print("{} * {} = {}".format(b, b, producto(b, b)))
    print("{} / {} = {}".format(a, c, division(a, c)))
    

if __name__ == "__main__":

    main()
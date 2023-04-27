import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= ini and numero <= fin:
                return numero
            else:
                print(f"Por favor ingrese un número entre {ini} y {fin}.")
        except ValueError:
            print("Por favor ingrese un número válido.")

def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    lista_numeros = []
    for i in range(numeros):
        numero = random.uniform(0, 100)
        if modo == 1:
            redondeo = math.ceil(numero)
        elif modo == 2:
            redondeo = math.floor(numero)
        else:
            redondeo = round(numero)
        print(f"Número: {numero}, redondeado: {redondeo}")
        lista_numeros.append(redondeo)

    return lista_numeros

def main():
    print("Bienvenido al generador de números aleatorios.")
    lista = generador()
    print(lista)

if __name__ == "__main__":


    main()
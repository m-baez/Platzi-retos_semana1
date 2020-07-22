# Reto #4 “Suma de enteros”

"""Instrucciones: otro clásico conocido, donde pedirás al usuario que ingrese 2 números y muestre en pantalla el resultado. Si quieres añadir más dificultad puedes utilizar números con punto decimal y especificar el número de decimales después del punto.
Ejemplo: 2.5633 + 5.6883 = 8.25"""


def main():
    print('Ingresarás dos números para realizar una suma :D \n')
    n1 = float(input('Ingresa el primer número: '))
    n2 = float(input('Ingresa el segundo número: '))
    res = (n1 + n2).__round__(2)

    print('\n El resultado de tu suma es: {}'.format(res))


if __name__ == '__main__':
    main()

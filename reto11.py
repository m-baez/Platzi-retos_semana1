# Reto #11 “Cuantas veces un número en otro”

"""Instrucciones: pide al usuario ingresar un número mayor a 1000 y otro menor a 100. Indica de una forma sencilla de entender al usuario cuantas veces cabe el número menor a 100 en el número mayor a 1000"""


def main():
    print('-'*50)
    biggerN = int(
        input('Ingresa un número mayor a 1,000 y presiona ENTER: '))
    minorN = int(input('Ingresa un número menor a 100 y presiona ENTER: '))
    res = biggerN / minorN
    print('\nEl número {} cabe {:,.2f} veces en {:,}'.format(
        minorN, res, biggerN))
    print('-'*50)


if __name__ == '__main__':
    main()

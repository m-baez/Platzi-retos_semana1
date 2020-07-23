# Reto #10 “Conversor de millas”

"""Instrucciones: hay 1.609344 km en una milla (mi). Escribe un programa en el que el usuario indique una cantidad de millas y muestre en pantalla el resultado convertido a kilómetros."""


def main():
    print('-'*60)
    miles = float(input('¿Cuántas millas quieres conventir a kilometros? '))
    kilometres = miles * 1.609344

    print('El resultado es: {:,.2f} kilometros'.format(kilometres))
    print('-'*60)


if __name__ == '__main__':
    main()

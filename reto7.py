# Reto #7 “Edad futura y pasada”

"""Instrucciones: pide al usuario que indique su nombre y su edad. Como mensaje de salida le indicarás que edad tuvo el año pasado y cuantos años tendrá el siguiente año.
Ejemplo: [nombre] el año pasado tenías X años y el próximo año cumplirás Y años."""


def main():
    name = str(input('Ingresa tu nombre: '))
    age = int(input('Ingresa tu edad: '))
    past = age - 1
    future = age + 1

    print('%s el año pasado tenías %d años y el próximo año cumplirás %d años' % (
        name, past, future))


if __name__ == '__main__':
    main()

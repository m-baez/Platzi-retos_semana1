# Reto #2 “Hola… nombre y apellido:”

"""Instrucciones: Ahora que sabemos incluir nombres, podemos agregar más datos. Intentemos con un apellido para tener algo así: ``Hola, [nombre] [apellido]"""


def main():
    name = str(input('Ingresa tu nombre y presiona ENTER: '))
    lastName = str(input('Ahora ingresa tu apellido y presiona ENTER: '))

    print('Hola {} {}'.format(name, lastName))


if __name__ == '__main__':
    main()

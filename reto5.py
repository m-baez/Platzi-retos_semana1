# Reto #5 “Suma y multiplicación”

"""Instrucciones: añadiendo un extra al reto anterior ahora el usuario ingresará 3 números, sumarás los 2 primeros y el resultado será multiplicado por el tercero. Añade las consideraciones del punto decimal del reto anterior.
Ejemplo:
Datos de entrada:2, 3, 4
Resultado:20"""


def main():
    print('Ingresarás 2 números para sumarlos y despúes ingresarás otro número para multiplicarlos \n')
    n1 = float(input('Escribe el primer número: '))
    n2 = float(input('Ahora un segundo para sumar: '))
    resSuma = n1 + n2
    n3 = int(input(
        'Ahora un tercer número, este servirá para multiplicar el resultado de la suma: '))
    resMult = (resSuma * n3).__round__(2)
    print('\nEl resultado es: {}'.format(resMult))


if __name__ == '__main__':
    main()

# Reto #6 “Resta de pizzas”

"""Instrucciones: llegaste a una fiesta con X cantidad de rebanadas de pizza (indicadas por el usuario), después de un rato se consumió Y cantidad de rebanadas y quedan Z. Fácil ¿cierto?
El reto está en que expreses lo que sucede es una forma comprensible para cualquier persona, imprescindible pensar en tus usuarios 😉"""


def main():
    pizzas = int(input('¿Cuántas pizzas llevaste a la fiesta? '))
    slicesOfPizza = pizzas * 8
    print('Ok, tienes {} rebanadas \n'.format(slicesOfPizza))

    consumedSlices = int(input('¿Cuántas rebanadas se han consumido? '))
    res = slicesOfPizza - consumedSlices

    if slicesOfPizza < consumedSlices:
        print('No te pases, no pueden consumir mas de lo que hay')
    elif res == 0:
        print('Ya no queda ninguna rebanada :c')
    elif res == 1:
        print('Solo queda {} rebanada de pizza'.format(res))
    elif slicesOfPizza > consumedSlices:
        print('Solo quedan {} rebanadas de pizza'.format(res))


if __name__ == '__main__':
    main()

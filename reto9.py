# Reto #9 “Calculando días”

"""Instrucciones: escribe un programa al que le indiques una cantidad de días y como resultado deberá mostrar cuantas horas, minutos y segundos hay en dicha cantidad de días."""


def main():
    print('-'*70)
    days = int(input('Escribe un número, que serán los días: '))
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    if days == 1:
        print(
            'En {} día hay {:,} horas, {:,} minutos y {:,} segundos'.format(days, hours, minutes, seconds))
    elif days > 0:
        print(
            'En {:,} días hay {:,} horas, {:,} minutos y {:,} segundos'.format(days, hours, minutes, seconds))
    print('-'*70)


if __name__ == '__main__':
    main()

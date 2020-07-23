# Reto #8 “Divide la cuenta”

"""Instrucciones: vas con tus amigos a tu restaurante favorito y acuerdan dividir la cuenta. Para facilitar las cosa pedirás al usuario que indique el total a pagar, entre cuantas personas se dvidirá la cuenta, porcentaje de propina a incluir, un porcentaje de impuestos, total a pagar incluyendo propina más impuestos y el total a pagar por cada persona."""


def main():

    print('-'*80)
    totalToPay = float(input('¿Cuánto es el total a pagar? '))
    persons = int(input('¿Entre cuántas personas se dividirá la cuenta? '))
    tip = str(input('¿Cuánta propina quieren dejar? (10%, 15%, 20%) '))

    tip10total = int(tip) * totalToPay / 100
    tip15total = int(tip) * totalToPay / 100
    tip20total = int(tip) * totalToPay / 100

    totalPerPerson = totalToPay / persons
    total = totalPerPerson + int(tip)
    pTotal = '\nTotal que pagará cada persona, con la propina incluida: $%.2f pesos' % total

    if tip == '0':
        print('\nOk, no dejarás nada de propina')
        print('Total que pagará cada persona, sin propina incluida: $%.2f pesos' %
              totalPerPerson)
    elif tip == '10':
        tip10PerPerson = int(tip) * totalPerPerson / 100
        print(pTotal)
        print('Ok, esto dejarán en total de propina entre %d personas: $%.2f pesos' %
              (persons, tip10total))
        print('Y esto, es lo que pagará cada persona individualmente de propina: $%.2f pesos' % tip10PerPerson)
    elif tip == '15':
        tip15PerPerson = int(tip) * totalPerPerson / 100
        print(pTotal)
        print('Ok, esto dejarán en total de propina entre %d personas: $%.2f pesos' %
              (persons, tip15total))
        print('Y esto, es lo que pagará cada persona individualmente de propina: $%.2f pesos' % tip15PerPerson)
    elif tip == '20':
        tip20PerPerson = int(tip) * totalPerPerson / 100
        print(pTotal)
        print('Ok, esto dejarán en total de propina entre %d personas: $%.2f pesos' %
              (persons, tip20total))
        print('Y esto, es lo que pagará cada persona individualmente de propina: $%.2f pesos' % tip20PerPerson)

    print('-'*80)


if __name__ == '__main__':
    main()

# Reto #3 “Mensaje multilínea”

"""Instrucciones: seguro has visto que en Platzi hay más de 600 cursos ¿puedes mostrar a que categorías corresponden en una sola línea de código?
Debe mostrarse así:
Platzi cuenta con cursos de:
[categoría1]
[categoría2]
[categoría3]
[categoría4]
[categoría5]
[categoría6]"""


def main():
    cursos = ['Curso de Pensamiento Lógico', 'Fundamentos de Ingeniería de Software', 'Fundamentos de Base de Datos',
              'Curso de API REST', 'Curso de Programación Orientada a Objetos: POO', 'Introducción a C++']

    print('Platzi cuenta con cursos de:')
    for curso in cursos:
        print('- {}'.format(curso))


if __name__ == '__main__':
    main()

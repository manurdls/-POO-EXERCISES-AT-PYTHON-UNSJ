def bloqueTryExcept():
    try:
        num1, num2 = eval(input('Ingrese dos numeros separados por coma:'))
        resultado = num1 / num2
        print('El resultado es {0:10.8f}'.format(resultado))

    except ZeroDivisionError as error:
        print('Error: {}\nLa division por cero es un error.'.format(error))
    except SyntaxError as error:
        print('Error: {}\nIngrese dos numeros separados por coma, ejemplo: 1,2'.format(error))
    except Exception as error:
        print('Error: {}\nEntrada erronea.'.format(error))

    else:
        print('No hubo excepciones')

    finally:
        print('Siempre se ejecuta esta accion')

if __name__ == '__main__':
    bloqueTryExcept()
from sympy import *


def f(x):
    return x**2 - 3


def derivada(x):
    xChar = Symbol('x')
    exp = str((diff(f(xChar))))
    return eval(exp, {"x": x})


def newton(chute, precisao):

    if abs(f(chute)) < precisao:
        print(f'Raiz = {chute:.2f}')
    else:
        if derivada(chute) == 0:
            print("Derivada nula, escolha outro chute")
        else:
            xiMais1 = chute - f(chute)/derivada(chute)
            while True:

                if abs(f(xiMais1)) < precisao:
                    print(f'Raiz = {xiMais1:.2f}')
                    break
                else:
                    xiMais1 = chute - f(chute)/derivada(chute)
                    chute = xiMais1


newton(3, 0.01)

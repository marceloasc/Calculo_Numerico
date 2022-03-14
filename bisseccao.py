
def f(x):
    return (x**2) - 7


def bisseccao(xa, xb, precisao):
    xm = 99999
    if f(xa)*f(xb) < 0:
        while (abs(f(xm)) > precisao):
            xm = (xa + xb) / 2
            if abs(f(xm)) < precisao:
                continue
            else:
                if f(xa)*f(xm) < 0:
                    xb = xm
                else:
                    xa = xm
        print(f'Raiz = {xm:.2f}')
    else:
        return print("Insira novos valores para Xa e Xb")


bisseccao(-3, 2, 0.01)

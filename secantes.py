
def f(x):
    return x**2 - 3


def secantes(chutes, precisao):

    x3 = 9898989898989898

    if abs(f(chutes[0])) < precisao:
        print(f"Raiz = {chutes[0]}")

    elif abs(f(chutes[1])) < precisao:
        print(f"Raiz = {chutes[1]}")

    else:
        while True:

            x3 = chutes[1] - (f(chutes[1])*(chutes[0] - chutes[1])) / (f(chutes[0]) - f(chutes[1]))

            if abs(f(x3)) < precisao:
                print(f"Raiz = {x3}")
                break
            else:
                chutes[0] = chutes[1]
                chutes[1] = x3


secantes([1, 3], 0.01)

import math #para fazer calculos matematicos

#funçoes
def mostra_menu():
        print('1 - Calcular equaçãi do 1º grau.')
        print('2 - Calcular equaçãi do 2º grau.')
        print('3 - Sair do progama.')

#equação de 2 grau
def cal_grau_2(a,b,c):
    delta = (b**2)-(4*a*c)
    if delta < 0:
        return 'A equação não possui reízes reais!'
    elif delta == 0:
        return f'O valor de x é: {(-b)/(2*a)}.'
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta)/(2*a)
        x2 = (-b - raiz_delta)/(2*a)
        yield f'Valor de x1: {x1}'
        yield f'Valor de x2: {x2}'
#equação do 1º grau
cal_grau_1 = lambda a,b: -b/a


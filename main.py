import equacoes as eq

if __name__ == '__main__':
    while True:
        eq.mostra_menu()
        op = input('Opção desejada: ')
        match op:
            case '1':
                a = float(input('Valor de a: ').replace(',','.'))
                b = float(input('Valor de b: ').replace(',','.'))
                print(f'Valor de x: {eq.cal_grau_1(a,b)}')
                continue
            case '2':
                a = float(input('Valor de a: ').replace(',','.'))
                b = float(input('Valor de b: ').replace(',','.'))
                c = float(input('Valor de a: ').replace(',','.'))
                result = eq.cal_grau_2(a,b,c)
                for x in result:
                    print(x)
                continue
            case '3':
                break
            case _:
                print('Opção inválida!')
                continue
    print('Progama encerrado!')
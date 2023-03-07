def soma():

    print('=-=-=-=-=-=-=-=-=-=')
    while True:
            valor = int(input('Digite o valor inicial: '))
            if valor == 0:
                break

            soma = 0
            if valor % 2 == 1:
                valor += 1

            for n in range(valor, valor+10, 2):
                soma += n

            print('A soma dos 5 pares é..: {}'.format(soma))
    print('=-=-=-=-=-=-=-=-=-=')

if __name__ == '__soma__':
    soma()
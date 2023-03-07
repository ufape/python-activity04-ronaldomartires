def valores():

    print('=-=-=-=-=-=-=-=-=-=')
    valor1 = int(input('Digite o valor 1: '))
    valor2 = int(input('Digite o valor 2: '))
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
    soma = []
    for s in range(valor1+1, valor2,):
           if s % 5 == 2 or s % 5 == 3:
                soma.append(s)
    print('Os números são..: {}'.format(' '.join(str(n)for n in soma)))
    print('=-=-=-=-=-=-=-=-=-=')

if __name__ == '__valores__':
    valores()
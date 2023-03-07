def primo(numero):

    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True 


def teste_numero_primo():
    n = int(input('Digite quantos testes realizará: '))
    for s in range(1, n+1):
        x = int(input('Teste {}: '.format(s)))
        if primo(x):
            print('{} é primo.'.format(x))
        else:
            print('{} não é primo.'.format(x))

    

if __name__ == '__teste_numero_primo__':
    teste_numero_primo()
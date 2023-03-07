def teste():

    def e_perfeito(n):
        quant = 0
        for s in range(1, n):
            if n % s == 0:
                quant += s
        return quant == n
      
    def teste_numero_perfeito():
        n = int(input('Digite quantos testes realizará: '))
        for s in range(1, n+1):
            x = int(input('Teste {}: '.format(s)))
            if e_perfeito(x):
                print('{} é perfeito.'.format(x))
            else:
                print('{} não é perfeito.'.format(x))

    teste_numero_perfeito()

if __name__ == '__teste__':
    teste()
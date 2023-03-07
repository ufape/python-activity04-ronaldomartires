def media():
    
    print('=-=-=-=-=-=-=-=-=-=')
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    n3 = float(input('Digite a nota 3: '))
    n4 = float(input('Digite a nota 4: '))
    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)
    print('Media: {:.1f}'.format(media))
    if media < 5.0:
        print('Aluno reprovado.')
    elif media >= 7.0:
        print('Aluno aprovado.')
    else:
        print('Aluno em exame.')
        exame = float(input('Digite a nota do exame: '))
        media_exame = (media + exame) / 2
        if media_exame >= 5.0:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
            print('A nova média')
        print('Media final: {:.1f}'.format(media_exame))
    print('=-=-=-=-=-=-=-=-=-=')

if __name__ == '__media__':
    media()
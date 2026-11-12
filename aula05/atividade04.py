print('''
[1] - Sul
[2] - Norte
[3] - Leste
[4] - Oeste
[5 ou 6] - Nordeste
[7,8 ou 9] - Sudeste
[10] - Centro-Oeste
[11] - Noroeste
''')

regiao = int(input('Escolha uma Região: '))

match regiao:
    case 1:
        print('Região Sul')
    case 2:
        print('Região Norte')
    case 3:
        print('Região Leste')
    case 4:
        print('Região Oeste')
    case 5 | 6:
        print('Região Nordeste')
    case 7|8|9:
        print('Região Sudeste')
    case 10:
        print('Região Centro-Oeste')
    case 11:
        print('Região Noroeste')
    case _:
        print('Produto Importado! ')
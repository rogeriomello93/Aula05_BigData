numero = float(input('Escolha um numero qualquer: '))

if numero >0:
    print(f'O número {numero} é positivo')

elif numero == 0:
    print(f'O número é zero!')

else:
    print(f'O número {numero} é negativo')


('''
[1] - Positivo
[2] - Negativo
[3] - Zero
''')

match numero:
    case 1:
        print() 

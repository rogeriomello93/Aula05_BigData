num = float(input('Escolha um numero qualquer: '))

if num>0:
    print(f'O número {num} é positivo')

elif num == 0:
    print(f'O número é neutro!')

else:
    print(f'O número {num} é negativo')


match num:
    case num if num >0:
        print(f'O número {num} é positivo')
    case num if num <0:
        print(f'O número {num} é negativo')
    case _:
        print(f'O número {num} é neutro')

 

nota1 = float(input('Qual foi a primeira nota? '))
nota2 = float(input('Qual foi a segunda nota? '))
nota3 = float(input('Qual foi a terceira nota? '))
nota4 = float(input('Qual foi a quarta nota? '))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f'Sua nota média foi de {media:.1f}')

if media >= 7:
    print(f'Parabens, você foi aprovado!!')

elif media >=5:
    print (f'Você está em recuperação!')

else:
    print (f'Você está reprovado!')


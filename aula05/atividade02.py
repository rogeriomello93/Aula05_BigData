notafinal = float(input('Qual foi a nota final do aluno? '))
freqfinal = float(input(f'Qual a % de frequencia do aluno?'))
valormensalidade = 500


if notafinal >= 7 and freqfinal >=75:
    desconto = valormensalidade*0.2
    valorfinal = valormensalidade - desconto
    print('Parabens, você tem direito a bolsa! ')
    print(f'Bolsa concedida no valor de R$ {desconto}')
    print(f'Sua mensalidade agora é de R$ {valorfinal}')

else:
    print ('A nota final foi abaixo de 7 ou a frequência abaixo de 75%. Portanto, o aluno não tem direito a bolsa!')

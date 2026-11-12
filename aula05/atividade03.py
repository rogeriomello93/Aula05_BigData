compra = float(input('Qual valor da compra ? '))
fidelidade = (input('Cliente cadastrado no programa fidelidade? ')).lower()

if fidelidade == 's':
    input('Informe seu cpf: ')


if compra > 200 or fidelidade == 's':
    print(f'Valor final é de R$ {compra:.2f}')

else: 
    frete = 25
    valorfinal = compra + frete
    print(f'O valor final com frete é de R$ {valorfinal:.2f}')

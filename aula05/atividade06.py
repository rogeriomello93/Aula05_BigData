venda = float(input('Informe o Valor da venda: '))

match venda:
    case venda if venda < 100:
        print(f'O valor de R$ {venda:.2f} é classificado como venda pequena')
    case venda if venda <500:
        print(f'O valor de R$ {venda:.2f} é classificado como venda média')
    case _:
        print(f'O valor de R$ {venda:.2f} é classificado como venda grande')
        
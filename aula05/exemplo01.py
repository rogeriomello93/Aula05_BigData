#frete gratis com pedido > 50,00 e a distancia até 3km, se tiver direito, valor final sem frete, se não, 8 de frete.

pedido = float (input('Qual valor do pedido? '))
dist = float (input('Qual a distancia de entrega segundo o GPS? '))

valorfinal = pedido
valorentrega = (pedido + 8)

if pedido > 50 and dist <= 3:
    print(f'O valor final é de {valorfinal}')

else:
    print(f'O valor final é de {valorentrega}')

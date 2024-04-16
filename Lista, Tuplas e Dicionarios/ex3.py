# Crie um dicionário representando um carrinho de compras. 
# Adicione produtos(chaves)e quantidades(valores) ao carrinho.
# Calcule o total do carrinho de compra.

carrinho_compra = {}

carrinho_compra['Banana'] = 5
carrinho_compra['Maca'] = 6
carrinho_compra['Laranja'] = 7

total = 0

for produto, quantidade in carrinho_compra.items():
    preco = 1.0
    total += quantidade * preco

print(f'Total R${total:.2f}')
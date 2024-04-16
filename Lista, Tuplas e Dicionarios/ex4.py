# Crie um dicionário representando contatos(nome,telefone). Permita 
# ao usuário procurar por um contato pelo nome

contato = {
    'Alice': '(11) 98745-3210',
    'Ben': '(15) 98765-4321',
    'Carol': '(21) 98765-4321',
    'Davi':'(44) 99877-6547'
}

nome = input('Digite o nome de contato que voce gostaria de procurar ')

if nome in contato:
    print(f'O telefone para {nome} eh {contato[nome]}')
else: 
    print(f'Desculpa, {nome} nao esta na lista de contato.')
    
# Vamos construir um jogo de forca. O programa escolherá aleatoriamente 
# uma palavra secreta de uma lista pre definida. A palavra secreta será 
# representada por espaços em branco, um para cada letra da palavra.
# O jogador terá um número limitado de 6 tentativas. Em cada tentativa,
# o jogador pode fornecer uma letra. Se a letra estiver presente na 
# palavra secreta, ela será revelada nas posições correspondentes.
# Se a letra não estiver na palavra, uma mensagem de erro deverá ser 
# informada. Após um número máximo de erros,o jogador perde. O jogo 
# continua até que o jogador adivinhe a palavra ou exceda o número 
# máximo de tentativas. Dica:Você precisará importar uma biblioteca 
# para resolver esse exercicio

import random

palavras = ['WomakersCode', 'python', 'django', 'sucesso', 'alegria']
palavras_adv = random.choice(palavras)
letras_corretas = ['_'] * len(palavras_adv)
tentativas = 6


while '_' in letras_corretas and tentativas > 0:
    
    print(' '.join(letras_corretas))

    advinha = input('Advinhe uma letra: ').lower()

    if advinha in palavras_adv:
        for i, letras in enumerate(palavras_adv):
            if letras == advinha:
                letras_corretas[i] = advinha
    else:
        tentativas -= 1
        print('Tentativa Errada! Voce tem {} tentativas restantes.'.format(tentativas))

if '_' not in letras_corretas:
    print('Parabens! Voce advinhou a palavra {}.'.format(palavras_adv))
else:
    print('Desculpe, Voce ulrapassou as tentativas. A palavra era {}.'.format(palavras_adv))
"""
Estruturas logicas

Para o AND ambos valores precisam ser true
Para o OR um ou outro valor precisa ser true
Para o NOT o valor do booleano é invertido

# NOT é unário, depende de um unico valor

ativo = True
logado = True

if ativo and logado:
    print(' Bem vindo. Voce está logado')
else:
    print('Voce precisa logar no sistema')

ativo = False
logado = False

if ativo or logado:
    print(' Bem vindo. Voce está logado')
else:
    print('Voce precisa logar no sistema')

"""

ativo = True
logado = False

if not ativo:
    print(' Voce precisa logar no sistema')
else:
    print(' Voce está logado ')

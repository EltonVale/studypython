"""
LOOP é estrutura de repeticao
FOR é uma dessas estruturas

C ou Java:
  for(int i = 0; i< limitador; i++){
   \\ execucao do limitador
}

python
   for item in inteiravel:
   //execucao do loop

utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis
"""
"""
nome = 'Elton Miguel'
lista = [1,3,5,7,9]
numeros = range(1, 10) #temos que transformar em lista

# exemplos de FOR 1. Iteirando em uma string

for letra in nome:
    print(letra)

# exemplo de FOR 2. Iteirando sobre uma lista
for numero in lista:
    print(numero)

# exemplo de FOR 3. Iterando sobre um range

for numero in range(1, 10):
    print(numero)

for i, v in enumerate(nome):
    print(nome[i])
"""

qtd= int(input('Quantas vezes o loop deve rodar '))
soma=0

for n in range(1, qtd+1):
    print(f' Loop {n}')
    numero = int(input( 'Digite um numero para somar'))
    soma = soma+ numero
print(f' O somatorio total é {soma}')

nome = 'Elton Miguel'
for letra in nome:
    print(letra, end='') # end='' é para nao pular linhas e imprimir o nome em uma linha so

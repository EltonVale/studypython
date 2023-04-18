"""

Listas funcionam como vetores, matrizes. Arrays em outras linguagens, pode colocar qualquer tipo
de dado. DINAMICO

 em C ou JAVA: Array
  -Possuem tamanho e tipo de dado fixo;
  ou seja, nessas linguagens se voce criar um array do tipo int e tamanho de 5, este array
  sempre será do tipo inteiro e podera sempre ter sempre no maximo 5 valores

Já em Python:

-Dinamico: Nao possui tamanho fixo; podemos criar a lista e ir adicionando elementos
-Qualquer tipo de dado: NAo possui tipo de dado fixo, podemos colocar qualquer tipo

As listas em Python sao representadas por colchetes []
"""

"""
print(' Digite algo ')
num =  input()

lista1 = [1, 10, 20, 3, 11, 13, 16, 2, 9, 5, 41, 23, 40, 8]
lista2 = ['Elton','Miguel']
lista3 = ['F','A','B','I']
lista4 = list(range(100))

if num in lista1 or lista2 or lista3 or lista4:
    print(f' Encontrei o valor {num}')
else:
    print(f' Nao encontrei o {num}')

 #ordenar uma lista:
lista1.sort()
print(lista1)

# Contar o numero de ocorrencias:
print(lista1.count(10))
print(lista2.count('Elton'))

# Adicionar elementos em listas:
#OBS para adicionar elementos em listas, utilizamos a funcao append

print(lista1)
lista1.append(98)
print(lista1)

# extend adiciona varios elementos a lista. Para adicionar lista dentro de outra lista,
#utilizar o append com parenteses e colchetes

lista1.extend([123,41,54,66])
print(lista1)

# Podemos inserir elementos informando a posicao

lista1.insert(2,'novo valor')
print(lista1)

# é possivel inverter uma lista com o reverse

lista1.reverse()
print(lista1)

# Saber o tamanho de lista

print(len(lista3))

# transformar string em lista com split. Separa pelo espaco

curso= "Elton Miguel do Vale"
print(curso)
curso= curso.split()
print(curso)

# Transformar string em lista sinalizando dentro do split qual o separador

curso = "Milene,Miguel,do,Vale"
curso=curso.split(',')
print(curso)

# Iterando elementos em listas

lista10 = [1, 40, 50, 60, 70 ,80]
soma=0

for elemento in lista10:
    print(elemento)
    soma= soma + elemento

    print(f' O valor da soma é {soma} ')
"""
"""
carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione produtos no carrinho ou digite sair ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

print(f' O seu carrinho possui os seguintes produtos: {carrinho}')
"""
"""
cores = ['Branco', 'Verde', 'Amarelo', 'Vermelho', 'Roxo']
indice = 0

while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Outra forma de fazer quando se tiver maior quandidade de valores

cores = ['Branco', 'Verde', 'Amarelo', 'Vermelho', 'Roxo']

for indice, cor in enumerate(cores):
    print(indice, cor)   
    
# Achar o indice por exemplo de um produto em uma lista de 1 milhao de itens

produtos = ['Playstatio', 'Xbox', 'Celular', 'mouse', 'teclado']

print(produtos.index('mouse'))# em caso de duplicidade de elementos ele retorna o primeiro encontrado

# Soma, Valor máximo, Valor minimo, tamanho

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma os itens da lista
print(max(lista)) # Maximo valor
print(min(lista)) # Minimo valor
print(len(lista)) # Tamanho da lista

# Trasformar lista em tupla

lista = [1, 2, 3, 4, 5, 6]

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de lista

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)
     
"""

# Desempacotamento de lista

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

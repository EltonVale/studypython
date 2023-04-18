
"""

As tuplas sao representadas por parenteses
As tuplas sao imutaveis: Ao se criar uma tupla ela nao muda. Toda operacao em tupla gera uma nova tupla



# as tuplas sao representadas por () mas veja:
#

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

# é a virgula que define uma tupla, pois pode ser tupla tambem sem parenteses

tupla2 = 1, 2, 3, 4

print(tupla2)
print(type(tupla2))

# exemplos:

(4) nao é tupla
(4,) é tupla
4, é tupla


exemplo_tupla_range = tuple(range(20))
print(exemplo_tupla_range)

# desempacotamento de tupla

tupla = (' Elton ', 'Miguel')

nome, sobrenome = tupla
print(f' O nome é {nome}')
print(f' O sobrenome é {sobrenome}')

# metodos de adicao e remocao de elementos nao existem pois tuplas sao imutaveis

#verificar se determinado elemento esta contido na tupla

tup = (1, 2, 3)
var = int(input('Digite um numero '))
if var in tup:
    print(f'O {var} está na tupla')
else:
    print(f'O {var} nao está na tupla ')

print(type(tup))

# iterando em uma tupla

for n in tup:
    print(n)

# contando elementos dentro da tupla

exemplo_tupla = ('a', 'b', 'a', 'c', 'c', 'c')

print(len(exemplo_tupla)) # apenas pra ver o tamanho da tupla
print(exemplo_tupla.count('c')) # incidencia do C na tupla

# Interando com while

tupla = ( 'Janeiro ', 'Fevereiro ', 'Marco', 'Abril', 'Junho', 'Julho')

i = 0
while i < len(tupla):
    print(tupla[i])
    i = i + 1

# verificando em qual indice esta na tupla

tupla = ('Janeiro ', 'Fevereiro', 'Marco', 'Abril', 'Junho', 'Julho')

print(tupla.index('Fevereiro'))

# Slicing. tupla[inicio:fim:passo]

tupla = ('Janeiro ', 'Fevereiro', 'Marco', 'Abril', 'Junho', 'Julho')

print(tupla[0:5:3])

# Slicing. tupla[inicio:fim:passo]

tupla = ('Janeiro ', 'Fevereiro', 'Marco', 'Abril', 'Junho', 'Julho')

print(tupla[0:5:3])

"""

# Porque utilizar tuplas?

#- Tuplas sao mais rapidas do que listas
#- Tuplas deixam seu codigo mais seguro- tem a ver com imutabilidade




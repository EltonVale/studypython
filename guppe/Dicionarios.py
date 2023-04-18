"""

Em outras linguagens de programacao, dicionarios é chamado de mapas.

Dicionarios sao colecoes do tipo chave/valor

em listas e tuplas, a chave fica oculta, podemos acessar pelo indice e verificar qual chave, pois so
vemos os valores.
Exemplo:
[0, 1, 2, 3]
[1, 2, 3, 4]     podemos ver que temos o valor 1 na posicao 0, valor 2 na posicao 1 e assim por diante

podem ser de qualquer tipo
podemos misturar tipos de dados

tem de estar entre aspas simples, dois pontos e valor. fica assim :
    chave : valor >- {'ex' : 'Exemplo', 'ex2' : 'Exemplo2')

#forma 1 (mais comum) criacao de dicionarios
paises = {'Br': 'Brasil', 'EUA': 'Estados Unidos', 'Py': 'Paraguai'}
print(paises)
print(type(paises))

# forma 2

paises1 = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises1)
print(type(paises1))


# Acessando elementos

# Forma 1- Acessando via chave, da mesma forma que lista/tupla

paises2 = {'Br': 'Brasil', 'EUA': 'Estados Unidos', 'Py': 'Paraguai'}
print(paises2['Br'])

# Forma 1- Acessando elementos via get - recomendada

paises2 = {'Br': 'Brasil', 'EUA': 'Estados Unidos', 'Py': 'Paraguai'}
print(paises2.get('Br'))

print(' Digite algo ')      #bricando com acessar elementos pelo input do usuario
dados = input()
if dados in paises2:
    print(f' O valor da chave é {paises2.get(dados)}')

"""

# Adicionando elementos a um dicionario

receita = {
    'Janeiro': 100, 'Fevereiro': 200
}
print(receita)
print(type(receita))

# Adicionando elementos a dicionarios

receita['Abril'] = 350

print(receita)
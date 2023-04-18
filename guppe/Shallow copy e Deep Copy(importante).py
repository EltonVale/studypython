#Deep copy . nao afeta a outra lista

lista = [1, 2, 3, 4, 5]

nova = lista.copy()
print(lista, nova)

nova.append('Teste')

print(lista)
print(nova)

nova.insert(2, '99')
print(f' A nova lista modificada é {nova}')

nova.append(50)
print(nova)

# Forma 2 Shallow copy. Altera as duas listas

lista1 = [1, 2, 3, 4, 5]

nova1 = lista1

nova1.append(99)

print(lista1)
print(nova1)
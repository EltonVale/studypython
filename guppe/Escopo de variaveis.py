"""
Dois casos de escopo:
  Variaveis globais: sao reconhecidas e seu escopo compreende todo o programa.
  Variaveis locais: sao reconhecidas apenas no bloco onde foram declaradas, seu escopo está limitado ao bloco declarado.


Para declarar variáveis em python fazemos:

nome_da_variavel= valor_da_variavel

python é uma linguagem de tipagem dinamica. Isso significa que ao declararmos
uma variavel nos nao colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor a mesma

"""

numero= 9 #exemplo de variavel global. Pois nao esta dentro de bloco
print(numero)
print(type(numero))

if numero > 10:
    novo= numero + 10

    print(f'voce digitou um numero maior do que 10 \n{novo}')
else:
    print(f'Digite um numero maior do que 10')
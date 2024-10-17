from random import randint, random, choices, choice
import requests

# def sortear_musica(lista):
#     numeros_a_jogar     = []
#     # with open('combinacao.txt', 'w', encoding='utf-8') as file:
#     for x in range(lista):
#             numeros = []
#             while len(numeros_a_jogar) <= x:
#                 numero  = randint(1, 60)
#                 if numero not in numeros:
#                     numeros.append(numero)
#                 if len(numeros) == 6:
#                     numeros.sort()
#                     if numeros in numeros_a_jogar:
#                          numeros.clear()
#                          print('Números já estão na lista')
#                          return
#                     numeros_a_jogar.append(numeros)
#                     break
#             # file.write(f'Jogo número: {x+1} = {str(numeros)}\n')
#     numeros_a_jogar.sort()
#     return numeros_a_jogar 

lista = ['Album 1', 'Album 2', 'Album 3', 'Album 4', 'Album 5']
def sorte(lista):# Sortea uma lista de músicas ou albúns escolhidos
    escolhas = []# lista de escolhas
    while len(escolhas) < 5:
        for musica in lista:
            escolha = choice(lista)
            if escolha not in escolhas:
                escolhas.append(escolha)
    return escolhas# retorna as escolhas

print(sorte(lista))

"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados. 
"""
import random
import exercises as cabecalho

cabecalho.cabecalho("lançamento de dados")

lista_valores = []
contador1 = 0 
contador2 = 0 
contador3 = 0 
contador4 = 0 
contador5 = 0 
contador6 = 0 

for i in range(1, 101):
    lista_valores.append(random.randint(1,6)) # Gostei e vou refatorar o meu numa unica linha. Ficou bacana.
       
for valor in lista_valores:
    if valor == 1:
        contador1 += 1
    elif valor == 2:
        contador2 += 1
    elif valor == 3:
        contador3 += 1
    elif valor == 4:
        contador4 += 1
    elif valor == 5:
        contador5 += 1
    elif valor == 6:
        contador6 += 1

print(f"""
O dado caiu {contador1} vezes no número 1.
O dado caiu {contador2} vezes no número 2.
O dado caiu {contador3} vezes no número 3.
O dado caiu {contador4} vezes no número 4.
O dado caiu {contador5} vezes no número 5.
O dado caiu {contador6} vezes no número 6.
""")

"""
Codigo bonito de se ver. Mas vou deixar uma dica pra fazer em menos linha e 
eliminar a tripa de if  e deixar seu codigo ainda mais foda do que é sempre.
PS: EU AMO UMA VISCERA DE IF. Mas como a senhorita tem codigos muito bons 
estou fazendo essa observação. Desculpa por isso.

from collections import Counter

resultado = Counter(lancamentos) # Aqui o comando counter checa 
quantas ocorrencias tiveram na lista de cada face do dado.

for jogada, ocorrencia in resultado.items():
    print(f'o lado do dado {jogada} ocorreu {ocorrencia} vezes')

"""
"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte
    quantos espaços em branco existem na frase.
    quantas vezes aparecem as vogais a, e, i, o, u. 

"""
import exercises as cabecalho

cabecalho.cabecalho("conta espaços e vogais")


frase = input("Insira a frase: ")

tamanho_string = len(frase.lower())

contador_espaco = 0 
contador_vogais = 0
for caractere in frase:
    if caractere == " ":
        contador_espaco +=1
    
    if caractere == "a" or caractere == "e" or caractere == "i" or caractere == "o" or caractere == "u":
        contador_vogais += 1

print(f"O espaço aparece {contador_espaco} vezes e as vogais aparecem {contador_vogais} vezes")

""" Eu to encontrando o resultado incorreto para o texto que apliquei. rodei o seu e o meu pra checar. 

no seu aparece o resultado: O espaço aparece 18 vezes e as vogais aparecem 36 vezes
no meu aparece o resultado: 
O elemento "A" aparece no texto 153 vezes
O elemento " " aparece no texto 268 vezes
O elemento "U" aparece no texto 44 vezes
O elemento "I" aparece no texto 88 vezes
O elemento "E" aparece no texto 180 vezes
O elemento "O" aparece no texto 136 vezes

mas digitando um texto curto na linha de comando da certo.

o rato levado roeu a roupa do rei de roma 

no seu aparece o resultado: O espaço aparece 9 vezes e as vogais aparecem 19 vezes
no meu aparece o resultado:
O elemento "O" aparece no texto 7 vezes
O elemento " " aparece no texto 9 vezes
O elemento "A" aparece no texto 5 vezes
O elemento "E" aparece no texto 4 vezes
O elemento "U" aparece no texto 2 vezes
O elemento "I" aparece no texto 1 vezes
"""
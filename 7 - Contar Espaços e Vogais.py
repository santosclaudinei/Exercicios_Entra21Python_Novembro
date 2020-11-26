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
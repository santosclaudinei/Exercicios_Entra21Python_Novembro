"""  
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
"""
import exercises as cabecalho

cabecalho.cabecalho("triângulos")

a = int(input("Insira o lado A do triângulo: "))
b = int(input("Insira o lados B do triângulo: "))
c = int(input("Insira o lado C do triângulo: "))

def tipo_triangulo(a,b,c):
    if a != b and c != b and a != c:
        print("Triângulo Escaleno")
    elif a == b and c == b and a == c:
        print("Triângulo Equilátero")
    else:
        print("Triângulo Isósceles")
""" Deixar dois espaços entre uma função e outra ou entre uma função e bloco de codigo. """
if a < b + c and b < a + c and c < a + b:
    print("\nOs números infomados formam um triângulo\n")
    tipo_triangulo(a,b,c)
else:
    print("\nOs números infomados não formam um triângulo")

""" Que codigo enxuto e bem feito. PARABÉNS AMANDA. Vou rever o meu. rs """

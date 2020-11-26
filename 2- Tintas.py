"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

"""

import exercises as cabecalho

cabecalho.cabecalho("loja de tintas")

area_pintada = int(input("Insira o tamanho em metros quadrados a ser pintado: "))
#resto = area_pintada - cont

def lata(area_pintada):
    #litro_metro2 = area_pintada + 6
    #qtd_litros = 0

    # cobertura de 1l para 6 m²
    #for i in range(0, area_pintada, 6):
    #    litro_metro2 -= 6
    #   qtd_litros +=1

    #latas = area_pintada/ 18
    latas = area_pintada/(18 * 6)
    valor_lata = latas * 80
    
    print(f"O valor a ser pago para cobrir {area_pintada} m² utilizando {int(latas)} lata(s) de tinta é: {valor_lata:.2f}")

def galao(area_pintada):
    #litro_metro2 = area_pintada + 6
    #qtd_litros = 0

    # cobertura de 1l para 6 m²
    #for i in range(0, area_pintada, 6):
    #    litro_metro2 -= 6
    #   qtd_litros +=1

    #galao = area_pintada/ 18
    galao = int(area_pintada/(3.6 * 6))
    valor_galao = galao * 25
    
    print(f"O valor a ser pago para cobrir {area_pintada} m² utilizando {galao} galão(ões) de tinta é: {valor_galao:.2f}")

#def lata_galao(area_pintada):

while True:
    opcao = int(input(f"""
    MENU
    \t[1] Comprar apenas latas de 18 litros
    \t[2] Comprar apenas galões de 3,6 litros
    \t[3] Comprar latas e galões
    \t[4] Sair
    SeLecione a opção que preferir: """))

    if opcao == 1:
        lata(area_pintada)
    elif opcao == 2:
        galao(area_pintada)
    elif opcao == 3:
        pass
    elif opcao == 4:
        print("Obrigado pela preferência :)")
        break
    else:
        print("Opção inválida!")
        continue


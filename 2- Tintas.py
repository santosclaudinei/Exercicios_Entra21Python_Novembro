"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.    
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


150 metros quadrados
2 latas
7 galões
ou 1 lata e 3 galões

"""
import exercises as cabecalho

cabecalho.cabecalho("loja de tintas")

""" remover comentarios abaixo caso não sejam mais necessarios. """

area_pintada = int(input("Insira o tamanho em metros quadrados a ser pintado: "))
#resto = area_pintada - cont

def lata(area_pintada):
    latas = area_pintada/(18 * 6) * 1.1
    latas = round(latas)
    valor_lata = latas * 80

    print(f"O valor a ser pago para cobrir {area_pintada} m² utilizando {latas} lata(s) de tinta é: {valor_lata:.2f}")

def galao(area_pintada):
    galao = area_pintada/(3.6 * 6) * 1.1
    galao = round(galao)
    valor_galao = galao * 25
    
    print(f"O valor a ser pago para cobrir {area_pintada} m² utilizando {galao} galão(ões) de tinta é: {valor_galao:.2f}")

def lata_galao(area_pintada):
    latas = area_pintada/(18 * 6) * 1.1
    print(latas)  # Remover a checagem
    latas = round(latas)
    print(latas)  # Remover a checagem

    aux = area_pintada - (latas * (18 * 6))

    galao = aux/(3.6 * 6) * 1.1
    galao= round(galao)

    """ Valor de galões esta dando negativo para uma area de 5000m² (verificar codigo dessa area) """

    valor_total = latas * 80  + galao * 25
    print(f"""
    O valor a ser pago para cobrir {area_pintada} m² de tinta é: {valor_total:.2f}
    Você vai precisar de:
    \tLatas: {latas}
    \tGalões: {galao} """)

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
        lata_galao(area_pintada)
    elif opcao == 4:
        print("Obrigado pela preferência :)")
        break
    else:
        print("Opção inválida!")
        continue


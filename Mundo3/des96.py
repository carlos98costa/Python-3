#Desafio 96 - Função que calcula área

def calc_area(lar, com):
    area = lar * com
    print(f'Á aréa de um terreno {lar} x {com} é de : {area}m². ')


print('Controle de terrenos')
print('-=' * 20)
lar = float(input('Entre com a largura do terreno (m): '))
com = float(input('Entre com o comprimento do terreno (m): '))
calc_area(lar, com)
#Desafio 99 - Função que descobre o maior

from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo. ')
    print(f'O maior valor informado foi {maior}. ')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
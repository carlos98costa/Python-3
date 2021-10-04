#Desafio 101 – Funções para votação
from datetime import datetime

def voto(age):
    if idade >= 18 and idade < 70:
        print(f'Com {idade} anos: Voto OBRIGATORIO! ')
    elif idade < 18 and idade >= 16 or idade > 70:
        print(f'Com {idade} anos: Voto OPICIONAL!')
    else:
        print(f'Com {idade} anos: Não vota! ')


ano_nasc = int(input('Digite seu ano de nascimento: '))
idade = datetime.today().year - ano_nasc
voto(age=idade)
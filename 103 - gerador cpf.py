# VALIDAÇÃO DOS DOIS DÍGITOS DO CPF
# coletando os valores e retirando os pontos e caracteres a mais para calcular os dígitos
import re
import sys
from random import randint

cpf = ""
for c in range(0, 9):
    cpf += str(randint(0, 9))

cpf = re.sub(r'[^0-9]', '', cpf)
cpf = list(cpf)

# validando caracteres repetidos

cpf_user = ''.join(cpf)
print(cpf_user)
primeiro_caractere = cpf_user[0]
repetido = cpf_user == primeiro_caractere * len(cpf_user)
if repetido:
    print('Voce enviou dados sequenciais')
    sys.exit()
# multiplicando os valores pela contagem regressiva


def regressiva(cpf):
    i = 0
    soma = 0
    for c in range(len(cpf)+1, 1, -1):
        soma = soma + (int(cpf[i])*c)
        i += 1
    return soma


# contas e validações finais
soma = regressiva(cpf)
resultado = (soma * 10) % 11
digito = resultado if resultado <= 9 else 0
print(f'O primeiro digito é {digito}')
cpf.append(digito)

# segundo digito

soma2 = regressiva(cpf)
resultado = (soma2 * 10) % 11
digito2 = resultado if resultado <= 9 else 0
cpf.append(digito2)
print(f'O segundo digito é {digito2}')

def remover_pontuacao(cpf):
    return cpf.replace(".", "").replace("-", "")


def calcular_digito(digitos, peso_inicial):
    soma = 0
    peso = peso_inicial
    for digito in digitos:
        soma += int(digito) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        return 0
    return 11 - resto


def validar_cpf(cpf):
    numeros = remover_pontuacao(cpf.strip())
    if len(numeros) != 11 or not numeros.isdigit():
        return False
    if numeros == numeros[0] * 11:
        return False
    if calcular_digito(numeros[:9], 10) != int(numeros[9]):
        return False
    if calcular_digito(numeros[:10], 11) != int(numeros[10]):
        return False
    return True

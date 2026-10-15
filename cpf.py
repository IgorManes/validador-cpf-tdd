def validar_cpf(cpf):
    numeros = cpf.strip().replace(".", "").replace("-", "")
    if len(numeros) != 11 or not numeros.isdigit():
        return False
    if numeros == numeros[0] * 11:
        return False
    soma = 0
    peso = 10
    for digito in numeros[:9]:
        soma += int(digito) * peso
        peso -= 1
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    if digito1 != int(numeros[9]):
        return False
    soma = 0
    peso = 11
    for digito in numeros[:10]:
        soma += int(digito) * peso
        peso -= 1
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    if digito2 != int(numeros[10]):
        return False
    return True

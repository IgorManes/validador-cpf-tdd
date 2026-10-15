def validar_cpf(cpf):
    numeros = cpf.strip().replace(".", "").replace("-", "")
    if len(numeros) != 11 or not numeros.isdigit():
        return False
    if numeros == numeros[0] * 11:
        return False
    return True

def validar_cpf(cpf):
    numeros = cpf.replace(".", "").replace("-", "")
    return len(numeros) == 11

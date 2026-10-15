from cpf import validar_cpf


def test_ambiente_funciona():
    assert True


def test_rejeita_texto_vazio():
    assert validar_cpf("") is False


def test_rejeita_menos_de_11_digitos():
    assert validar_cpf("1234567890") is False


def test_rejeita_digitos_todos_iguais():
    assert validar_cpf("11111111111") is False


def test_aceita_pontuacao():
    assert validar_cpf("529.982.247-25") is True

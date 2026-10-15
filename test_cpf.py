from cpf import validar_cpf


def test_ambiente_funciona():
    assert True


def test_rejeita_texto_vazio():
    assert validar_cpf("") is False

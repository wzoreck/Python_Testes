def soma(x, y):
    # Utilizando Assertions (voltado para outros desenvolvedores)
    # Verificando se x é uma instância de int ou float (Assertions)
    assert isinstance(x, (int, float)), 'X precisa ser do tipo int ou float'
    assert isinstance(y, (int, float)), 'Y precisa ser do tipo int ou float'
    return x + y


def soma2(x, y):
    # Doctests (Escrever testes na documentação diretamente) - precisa executar este arquivo!
    # (chama a função e verifica se o retorno condiz com o resultado esperado)
    """Soma x e y

    >>> soma2(10, 20)
    30

    >>> soma2(5, 2)
    90

    >>> soma2('10', 30)
    Traceback (most recent call last):
    ...
    AssertionError: X não é int ou float
    """
    # Este último teste passará pois foi feito tratamento de excessão
    assert isinstance(x, (int, float)), 'X não é int ou float'
    return x + y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
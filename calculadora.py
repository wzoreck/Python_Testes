# Utilizando Assertions (voltado para outros desenvolvedores)

def soma(x, y):
    # Verificando se x é uma instância de int ou float
    assert isinstance(x, (int, float)), 'X precisa ser do tipo int ou float'
    return x + y
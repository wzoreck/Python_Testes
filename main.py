from calculadora import soma

# print(f'A soma entre 10 e 20 é: {soma(10, 20)}')
# print(f'A soma entre -10 e 20 é: {soma(-10, 20)}')

# Com o try except evitamos o encerramento do programa, a execução é mantida
try:
    print(soma('10', 20))
except AssertionError as e:
    print(f'A operação falhou: {e}')
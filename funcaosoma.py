
def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = float(input("Valor 1: "))
    valor2 = float(input("Valor 2: "))
    resposta = minha_funcao(valor1, valor2)
    print('--> ', valor1, ' + ', valor2, " = ",resposta)
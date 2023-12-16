fluxo_caixa = []

print("______________")
print("FLUXO DE CAIXA")
print("--------------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite qualquer outro número para encerrar #\n")

def adicionar_transacao():
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    fluxo_caixa.append({
        'nome': nome,
        'valor': valor
    })


while True:
    
    opcao = int( input("Escolha uma opção: "))
    
    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break
    

# nota fiscal 
total = 0

print("---------------------------")

for fc in fluxo_caixa:
    print('Nome:', fc['nome'], "\n Valor: R$", fc['valor'])
    total = total + fc['valor']
    
print("---------------------------")

print("Saldo atual: R$",total)

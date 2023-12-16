import os
import platform


mensagens = []

nome = input("Nome: ")

while True:
    
    # limpando terminal
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['texto'])
            
    print("__________________________________")
    
    #obtendo texto
    texto = input("mensagem: ")
    if texto =='fim':
        break
    
    # adicionando mensagem na lista
    mensagens.append({
        'nome': nome,
        'texto': texto
    })
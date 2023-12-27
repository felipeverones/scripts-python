import random as rd


escolha = int(input("Você escolhe cara ou coroa? 0 para cara, 1 para coroa\n"))

side = rd.randint(0,1)

if side == 0:
    print("Deu cara!")
else:
    print("Deu coroa!")
    
if escolha == side:
    print("Você Venceu!")
else:
    print("Você perdeu...")    
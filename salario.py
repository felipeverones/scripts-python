salario = float(input("Informe o salário: "))

if salario <= 4000:
    print('Programador Júnior')
elif salario > 4000 and salario <= 7000:
    print("Programador Pleno")
elif salario > 7000 and salario <= 15000:
    print("Programador Sênior")
else:
    print("Gerente de Projetos")

height = input("Insira sua altura, em metros:\n")


weight = input("Insira seu peso, em quilogramas:\n")


weight_as_float = float(weight)
height_as_float = float(height)

bmi = weight_as_float /(height_as_float ** 2)

if bmi < 18.5:
    print(f"Seu IMC é {round(bmi,2)}, você está abaixo do peso.")
elif bmi < 25:
    print(f"Seu IMC é {round(bmi,2)}, você tem um peso normal.")
elif bmi < 30: 
    print(f"Seu IMC é {round(bmi,2)}, você está ligeiramente acima do peso.")
elif bmi < 35:
    print(f"Seu IMC é {round(bmi,2)}, você está obeso.")
else:
    print(f"Seu IMC é {round(bmi,2)}, você está clinicamente obeso.")
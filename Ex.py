entrada = input("Que horas são?")

if entrada.isdigit():
    hora = int(entrada)
    
    if hora < 24 and hora > 0:
        if hora >= 0 and hora <= 11:
            print("Bom dia!") 

        elif hora >= 12 and hora <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")
    else:
        print("Digite um horário válido!")
else:
    print("Por favor, digite um número inteiro!")
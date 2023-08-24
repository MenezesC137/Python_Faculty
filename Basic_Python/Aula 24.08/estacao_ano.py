dia = int(input("Digite o dia: "))
mes = input("Digite o mês: ")
if mes == "janeiro" or mes == "Janeiro" or mes == "JANEIRO" or mes == "1":
    if dia >= 1 and dia <= 31:
        print("Verão")
    else:
        print("Dia inválido")
elif mes == "fevereiro" or mes == "Fevereiro" or mes == "FEVEREIRO" or mes == "2":
    if dia >= 1 and dia <= 29:
        print("Verão")
    else: 
        print("Dia inválido")
elif mes == "março" or mes == "Março" or mes == "MARÇO" or mes == "3":
    if dia >= 1 and dia <= 20:
        print("Verão")
    elif dia >= 21 and dia <= 31:
        print("Outono")
    else:
        print("Dia inválido")
elif mes == "abril" or mes == "Abril" or mes == "ABRIL" or mes == "4":
    if dia >= 1 and dia <= 30:
        print("Outono")
    else:
      
        print("Dia inválido")
elif mes == "maio" or mes == "Maio" or mes == "MAIO" or mes == "5":
    if dia >= 1 and dia <= 31:
        print("Outono")
    else:
        print("Dia inválido")
elif mes == "junho" or mes == "Junho" or mes == "JUNHO" or mes == "6":
    if dia >= 1 and dia <= 20:
        print("Outono")
    elif dia >= 21 and dia <= 30:
        print("Inverno")
    else:
        print("Dia inválido")
elif mes == "julho" or mes == "Julho" or mes == "JULHO" or mes == "7":  
    if dia >= 1 and dia <= 31:
        print("Inverno")
    else:
        print("Dia inválido")
elif mes == "agosto" or mes == "Agosto" or mes == "AGOSTO" or mes == "8":
    if dia >= 1 and dia <= 31:
        print("Inverno")
    else:
        print("Dia inválido")
elif mes == "setembro" or mes == "Setembro" or mes == "SETEMBRO" or mes == "9":
    if dia >= 1 and dia <= 22:
        print("Inverno")
    elif dia >= 23 and dia <= 30: 
        print("Primavera")
    else:
        print("Dia inválido")
elif mes == "outubro" or mes == "Outubro" or mes == "OUTUBRO" or mes == "10":

    if dia >= 1 and dia <= 31:
        print("Primavera")
    else:
        print("Dia inválido")
elif mes == "novembro" or mes == "Novembro" or mes == "NOVEMBRO" or mes == "11":
    if dia >= 1 and dia <= 30:
        print("Primavera")
    else:
        print("Dia inválido")
elif mes == "dezembro" or mes == "Dezembro" or mes == "DEZEMBRO" or mes == "12":
    if dia >= 1 and dia <= 21:
        print("Primavera")
    elif dia >= 22 and dia <= 31:
        print("Verão")
    else:
        print("Dia inválido")
else:
    print("Mês inválido")
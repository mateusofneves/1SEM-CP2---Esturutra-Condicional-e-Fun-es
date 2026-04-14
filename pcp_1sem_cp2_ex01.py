# criação das primeiras 3 variaveis. CE = Codigo do estado. Peso = Peso da carga. CC = Codigo da carga
CE = int(input("Informe o Codigo do estado de origem: "))

Peso = float(input("Digite o Peso da carga em toneladas: "))

CC = int(input("Digite o codigo da carga: "))

#Calculo para converter toneladas para quilogramas
Tone_Kq = Peso * 1000

#criacao dos "e se"
if(CC >= 10 and CC <= 20):
    # calculo para retirar o preço bruto da carga
    preco_Kq = Tone_Kq * 100
    if(CE == 1):
        #calculo do imposto
        imposto = preco_Kq * 0.35
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}. \n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f} \n ")

    elif(CE == 2):
        imposto = preco_Kq * 0.25
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}. \n Preço da carga do caminhao {preco_Kq:.2f}. \n "
              f"Valor do imposto: {imposto:.2f}. \n Valor total: {valor_total:.2f} \n")

    elif (CE == 3):
        imposto = preco_Kq * 0.15
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}. \n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f} \n")

    elif (CE == 4):
        imposto = preco_Kq * 0.05
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f} \n ")

    elif (CE == 5):
        imposto = preco_Kq
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f} \n")

    elif (CE >= 6):
        print(f"DIGITE UM CODIGO DE ESTADO VALIDO!!")


if(CC >= 21 and CC <= 30):
    preco_Kq = Tone_Kq * 250
    if (CE == 1):
        imposto = preco_Kq * 0.35
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f} \n")

    elif (CE == 2):
        imposto = preco_Kq * 0.25
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f} \n")

    elif (CE == 3):
        imposto = preco_Kq * 0.15
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f} \n")

    elif (CE == 4):
        imposto = preco_Kq * 0.05
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f}\n ")

    elif (CE == 5):
        imposto = preco_Kq
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f} \n")
    elif (CE >= 6):
        print(f"DIGITE UM CODIGO DE ESTADO VALIDO!!")

if(CC >= 31 and CC <= 40):
    preco_Kq = Tone_Kq * 340
    if (CE == 1):
        imposto = preco_Kq * 0.35
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f} \n")

    elif (CE == 2):
        imposto = preco_Kq * 0.25
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f}\n ")

    elif (CE == 3):
        imposto = preco_Kq * 0.15
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f}\n ")

    elif (CE == 4):
        imposto = preco_Kq * 0.05
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}. \n"
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f} \n")

    elif (CE == 5):
        imposto = preco_Kq
        valor_total = imposto + preco_Kq
        print(f"Peso da carga em Kq: {Tone_Kq:.2f}.\n Preço da carga do caminhao {preco_Kq:.2f}.\n "
              f"Valor do imposto: {imposto:.2f}.\n Valor total: {valor_total:.2f} \n")

    elif (CE >= 6):
        print(f"DIGITE UM CODIGO DE ESTADO VALIDO!!")








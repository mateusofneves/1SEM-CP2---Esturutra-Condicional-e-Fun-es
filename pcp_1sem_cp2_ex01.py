# Entrada de dados
CE = int(input("Informe o Código do estado de origem (1 a 5): "))
peso = float(input("Digite o peso da carga em toneladas: "))
CC = int(input("Digite o código da carga (10 a 40): "))

# Conversão toneladas -> kg
peso_kg = peso * 1000

# Definição do preço por kg
if 10 <= CC <= 20:
    preco_por_kg = 100
elif 21 <= CC <= 30:
    preco_por_kg = 250
elif 31 <= CC <= 40:
    preco_por_kg = 340
else:
    print("Código de carga inválido!")
    exit()

# Definição do imposto por estado
impostos = {
    1: 0.35,
    2: 0.25,
    3: 0.15,
    4: 0.05,
    5: 0.0
}

if CE not in impostos:
    print("Código de estado inválido!")
    exit()

# Cálculos
preco_total = peso_kg * preco_por_kg
imposto = preco_total * impostos[CE]
valor_total = preco_total + imposto

# Saída
print(f"""
Peso da carga em kg: {peso_kg:.2f}
Preço da carga: {preco_total:.2f}
Imposto: {imposto:.2f}
Valor total: {valor_total:.2f}
""")





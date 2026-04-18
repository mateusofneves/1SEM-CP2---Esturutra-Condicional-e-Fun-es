#PEGANDO VALORES! :O
nome = input("Digite o nome do colaborador: ")
cargo = input("Digite o cargo do funcionario: ").lower()
salario_base = float(input("Digite o valor do seu salario: "))
horas_ex = float(input("Digite o número de horas extras trabalhadas: "))
faltas = int(input("Digite o número de faltas do mês: "))
bonus = bool(input("recebeu bônus por desempenho (s/n): ").lower().startswith('s'))

#TOTAL DE BONUS COM HORAS EXTRAS E CARGO
def bonus_geral(bonus_h, bonus_c):
    acrescimos = bonus_h + bonus_c
    print(f"Seu total de acréscimos de bônus é de: R${acrescimos:.2f}")
    return acrescimos

# CONFIGURANDO BONUS SE TIVER
bonus_c = 0

if bonus:
    #TABELINHA COM OS VALORES E CARGOS PERMITIDOS
    bonus_cargos = {
        "gerente": 1000,
        "analista": 500,
        "assistente": 300,
        "estagiario": 100
    }

    #SE O CARGO EXISTIR NA TABELA BONUS RETORNA O VALOR BONUS ATRIBUIDO
    if cargo in bonus_cargos:
        bonus_c = bonus_cargos[cargo]
        print(f"Bônus de R$ {bonus_c} atribuído ao {cargo}.")
    else:
        print("sem bônus atribuído")

#CALCULO DO BONUS POR HORA EXTRA
def bonus_por_hora_extra(salario_base, horas_ex):
    valor_hora = salario_base / 160  # base padrão mensal
    bonus_h = valor_hora * 1.5 * horas_ex
    print(f"O bônus de hora extra trabalhada é de: R${bonus_h:.2f}")
    return bonus_h

#CALCULO DE DESCONTO POR FALTAS
def calcular_desconto_faltas(salario_base, faltas):
    desconto = salario_base * 0.02 * faltas
    print(f"Total de descontos por faltas: R${desconto:.2f}")
    return desconto

# EXECUÇÃO

bonus_h = bonus_por_hora_extra(salario_base, horas_ex)
acrescimos = bonus_geral(bonus_h, bonus_c)
descontos = calcular_desconto_faltas(salario_base, faltas)

salario_bruto = salario_base
salario_final = salario_bruto + acrescimos - descontos

print("\n===== RESUMO =====")
print(f"Salário bruto: R${salario_bruto:.2f}")
print(f"Total de acréscimos: R${acrescimos:.2f}")
print(f"Total de descontos: R${descontos:.2f}")
print(f"Salário final: R${salario_final:.2f}")


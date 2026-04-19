# ===== entrada de dados =====
nome = input("Digite o nome do colaborador: ")
cargo = input("Digite o cargo do funcionário: ").lower()
salario_base = float(input("Digite o valor do salário: "))
horas_ex = float(input("Digite o número de horas extras: "))
faltas = int(input("Digite o número de faltas no mês: "))
recebeu_bonus = input("Recebeu bônus por desempenho? (s/n): ").lower().startswith('s')


# ===== funções =====

# calcula o valor ganho com horas extras
def calcular_horas_extras(salario_base, horas):
    valor_hora = salario_base / 160  # padrão de 160h mensais
    extra = valor_hora * 1.5 * horas
    return extra


# calcula desconto por faltas
def calcular_descontos_faltas(salario_base, faltas):
    desconto = salario_base * 0.02 * faltas
    return desconto


# calcula bônus por cargo (se tiver direito)
def calcular_bonus(cargo, recebeu_bonus):
    bonus_cargos = {
        "gerente": 1000,
        "analista": 500,
        "assistente": 300,
        "estagiario": 100
    }

    if recebeu_bonus and cargo in bonus_cargos:
        return bonus_cargos[cargo]
    else:
        return 0


# ===== cálculo =====

# calcula cada parte separadamente
valor_horas_extras = calcular_horas_extras(salario_base, horas_ex)
valor_bonus = calcular_bonus(cargo, recebeu_bonus)
valor_descontos = calcular_descontos_faltas(salario_base, faltas)

# salário bruto é só o base
salario_bruto = salario_base

# soma de acréscimos
acrescimos = valor_horas_extras + valor_bonus

# cálculo final
salario_final = salario_bruto + acrescimos - valor_descontos


# ===== saída =====
print("\n===== RESUMO =====")
print(f"Funcionário: {nome}")
print(f"Salário bruto: R${salario_bruto:.2f}")
print(f"Acréscimos (extras + bônus): R${acrescimos:.2f}")
print(f"Descontos (faltas): R${valor_descontos:.2f}")
print(f"Salário final: R${salario_final:.2f}")

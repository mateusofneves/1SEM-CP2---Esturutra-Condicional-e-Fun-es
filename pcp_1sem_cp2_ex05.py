import math


def pode_aprovar(idade, renda, valor):
    # precisa ser maior que 18 (não inclui 18)
    if idade <= 18:
        return False, "O cliente precisa ter mais de 18 anos."

    # limite de 20x a renda
    limite = renda * 20
    if valor > limite:
        return False, f"Valor acima do permitido (máx: R$ {limite:,.2f})"

    return True, "Aprovado"


def definir_taxa(parcelas):
    # define a taxa de acordo com a quantidade de parcelas
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10


def calcular_parcela(valor, taxa, parcelas):
    # fórmula da tabela price
    i = taxa
    n = parcelas

    # evita repetir cálculo
    fator = math.pow(1 + i, n)

    return valor * i * fator / (fator - 1)


def calcular_total(parcela, parcelas):
    # total pago no final
    return parcela * parcelas


def calcular_juros(total, valor):
    # quanto foi pago só de juros
    return total - valor


def executar_sistema():
    print("=" * 40)
    print("SISTEMA DE FINANCIAMENTO")
    print("=" * 40)

    try:
        # entrada de dados
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        renda = float(input("Renda mensal: "))
        valor = float(input("Valor do empréstimo: "))
        parcelas = int(input("Parcelas (3 a 24): "))

        # valida parcelas
        if not (3 <= parcelas <= 24):
            print("Número de parcelas inválido.")
            return

        aprovado, motivo = pode_aprovar(idade, renda, valor)

        print("\n--- RESULTADO ---")

        if aprovado:
            taxa = definir_taxa(parcelas)

            parcela = calcular_parcela(valor, taxa, parcelas)
            total = calcular_total(parcela, parcelas)
            juros = calcular_juros(total, valor)

            print("Status: APROVADO")
            print(f"Cliente: {nome}")
            print(f"Valor: R$ {valor:,.2f}")
            print(f"Taxa: {taxa*100:.0f}% ao mês")
            print(f"Parcela: R$ {parcela:,.2f}")
            print(f"Total pago: R$ {total:,.2f}")
            print(f"Juros: R$ {juros:,.2f}")

        else:
            print("Status: NEGADO")
            print(f"Motivo: {motivo}")

    except ValueError:
        print("Erro: entrada inválida.")


if __name__ == "__main__":
    executar_sistema()

import math


def pode_aprovar(idade, renda, valor):
    """
    Verifica se o cliente atende aos requisitos básicos de aprovação:
    - Ter mais de 18 anos.
    - Valor do financiamento ser no máximo 20 vezes a renda mensal.
    """
    if idade < 18:
        return False, "O cliente deve ter mais de 18 anos."

    limite_renda = renda * 20
    if valor > limite_renda:
        return False, f"O valor solicitado excede o limite de 20x a renda mensal (R$ {limite_renda:,.2f})."

    return True, "Aprovado"


def definir_taxa(parcelas):
    """
    Define a taxa de juros mensal com base no número de parcelas.
    """
    if parcelas <= 6:
        return 0.05  # 5% ao mês
    elif 7 <= parcelas <= 12:
        return 0.08  # 8% ao mês
    else:
        return 0.10  # 10% ao mês (13 até 24 parcelas)


def calcular_parcela(valor, taxa, parcelas):
    """
    Calcula o valor da parcela (PMT) usando a fórmula da Tabela Price:
    PMT = PV * [i * (1 + i)^n] / [(1 + i)^n - 1]
    """
    # i = taxa, n = parcelas, PV = valor
    i = taxa
    n = parcelas
    pv = valor

    numerador = pv * i * math.pow((1 + i), n)
    denominador = math.pow((1 + i), n) - 1

    pmt = numerador / denominador
    return pmt


def calcular_total(parcela, parcelas):
    """
    Calcula o valor total pago ao final do financiamento.
    """
    return parcela * parcelas


def calcular_juros(total, valor):
    """
    Calcula o total de juros pagos (Total Pago - Valor Inicial).
    """
    return total - valor


def executar_sistema():
    """
    Função principal para interação com o usuário.
    """
    print("=" * 40)
    print("SISTEMA DE ANÁLISE DE FINANCIAMENTO")
    print("=" * 40)

    try:
        # 1. Coleta de dados
        nome = input("Nome do cliente: ")
        idade = int(input("Idade: "))
        renda = float(input("Renda mensal (R$): "))
        valor_solicitado = float(input("Valor desejado do empréstimo (R$): "))
        parcelas = int(input("Número de parcelas (3 até 24): "))

        # Validação do intervalo de parcelas
        if parcelas < 3 or parcelas > 24:
            print("\nErro: O número de parcelas deve estar entre 3 e 24.")
            return

        # 2. Verificação de Aprovação
        aprovado, motivo = pode_aprovar(idade, renda, valor_solicitado)

        print("\n" + "-" * 40)
        print("RESULTADO DA ANÁLISE")
        print("-" * 40)

        if aprovado:
            # 3. Definição da Taxa e Cálculos
            taxa_mensal = definir_taxa(parcelas)
            valor_parcela = calcular_parcela(valor_solicitado, taxa_mensal, parcelas)
            valor_total = calcular_total(valor_parcela, parcelas)
            total_juros = calcular_juros(valor_total, valor_solicitado)

            # 4. Exibição dos dados aprovados
            print(f"Status: APROVADO")
            print(f"Cliente: {nome}")
            print(f"Valor Financiado: R$ {valor_solicitado:,.2f}")
            print(f"Taxa de Juros: {taxa_mensal * 100:.0f}% ao mês")
            print(f"Número de Parcelas: {parcelas}")
            print(f"Valor da Parcela: R$ {valor_parcela:,.2f}")
            print(f"Valor Total Pago: R$ {valor_total:,.2f}")
            print(f"Total de Juros Pagos: R$ {total_juros:,.2f}")
        else:
            print(f"Status: NEGADO")
            print(f"Motivo: {motivo}")

        print("=" * 40)

    except ValueError:
        print("\nErro: Por favor, insira valores numéricos válidos para idade, renda e valores.")


if __name__ == "__main__":
    executar_sistema()
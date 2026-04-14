print("=====TIPO DO TRIÂNGULO=====")
a = int(input("Digite o valor do lado A: "))
b = int(input("Digite o valor do lado B: "))
c = int(input("Digite o valor do lado C: "))

lados = [a, b, c]
lados.sort(reverse=True)

A, B, C = lados

print(f"O lado A: {A}. O lado B: {B}. O lado {C}")

# verifica se forma triângulo
if A >= B + C:
    print("NÃO FORMA TRIÂNGULO")
# tipos
elif A == B == C:
    print("TRIÂNGULO EQUILATERO")
elif A == B or B == C or C == A:
    print("TRIÂNGULO ISOSCELES")
elif A**2 == B**2 + C**2:
    print("TRIÂNGULO RETANGULO")
elif A**2 > B**2 + C**2:
    print("TRIÂNGULO OBTUSANGULO")
else:
    print("TRIÂNGULO ACUTANGULO")
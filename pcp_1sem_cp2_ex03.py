#Questao 3, sistema de controle de notas dos alunos
print(f'==========SISTEMA DE NOTAS==========')
nome = input('Digite o nome do aluno: ')
rm = int(input('Digite o RM do aluno: '))
nota_cp1 = float(input('Digite a nota da CP-1: '))
nota_cp2 = float(input('Digite a nota da CP-2: '))
nota_cp3 = float(input('Digite a nota da CP-3: '))
nota_sp1 = float(input('Digite a nota da Sprint 1 (sp1): '))
nota_sp2 = float(input('Digite a nota da Sprint 2 (sp1): '))
nota_gs  = float(input('Digite a nota da Global Solution (gs): '))
print(f'\n')

#variavel que vai receber a menor nota para calcular as medias
menor = 0

#condicionais de verificacao para ver qual a menor nota entre os checkpoints
if nota_cp1 < nota_cp2 and nota_cp1 < nota_cp3 and nota_cp1 < nota_sp1 and nota_cp1 < nota_sp2 and nota_cp1 < nota_gs:
    menor = nota_cp1
elif nota_cp2 < nota_cp1 and nota_cp2 < nota_cp3 and nota_cp2 < nota_sp1 and nota_cp2 < nota_sp2 and nota_cp2 < nota_gs:
    menor = nota_cp2
elif nota_cp3 < nota_cp2 and nota_cp3 < nota_cp1 and nota_cp3 < nota_sp1 and nota_cp3 < nota_sp2 and nota_cp3 < nota_gs:
    menor = nota_cp3

#variaveis armazenando as notas medias com e sem peso
media = ((nota_cp1 + nota_cp2 + nota_cp3 + nota_sp1 + nota_sp2 - menor) * 0.4 + (nota_gs * 0.6)) / 4
media_com_peso = media * 0.4

#exibindo os resultados
print(f'==========RESULTADOS==========')
print(f'Nome do aluno: {nome}')
print(f'RM do aluno: {rm}')
print(f'Média do semestre (sem peso): {media:.2f}')
print(f'Média do semestre (com peso): {media_com_peso:.2f}')
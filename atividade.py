from trata_dicionario import conversor_percent_genero
from trata_dicionario import conversor_percent_ensino
from trata_dicionario import conversor_percent_idade


professor = input("Digite o nome do professor da turma:")
print(f"Bem vindo {professor}, esse programa é feito para que possamos interpretar os valores de nossos alunos da sala de aula:")

continuar = "Y"
lista_alunos = []


while continuar == "Y":
    dados_aluno = {}
    aluno = input("Preencha o nome do aluno: ")

    genero = input("Identifique o gênero, digite M para Masculino e F para feminino: ").upper()

    while genero not in ["M", "F"]:
        genero = input("Por favor digite M ou F! ").upper()

    idade = int(input("Qual é a sua idade? "))

    escolaridade = input("Qual a sua escolaridade?\nDigite:\nM para médio.\nS para Superior.\nPS para Pos.\n").upper()
    
    while escolaridade not in ["M", "S", "PS"]:
        escolaridade = input("Por favor digite M, S ou F").upper()
    
    dados_aluno['aluno'] = aluno
    dados_aluno['genero'] = genero
    dados_aluno['idade'] = idade
    dados_aluno['escolaridade'] = escolaridade

    lista_alunos.append(dados_aluno)
    
    continuar = input("Deseja continar?: (Y/N) ")


escolha = int(input("O que deseja saber?\nDigite:\n1 - para comparação de genero\n2 - para comparação de escolaridade\n3 - para comparação de idades"))

while escolha not in [1, 2, 3]:
    escolha = int(input("Por favor digite 1, 2, 3"))

if escolha == 1:

    total_dados = conversor_percent_genero(lista_alunos)
    print(total_dados['percet_homens'])
    print(total_dados['percet_mulheres'])

elif escolha == 2:

    total_dados = conversor_percent_ensino(lista_alunos)
    print(total_dados['percet_pos'])
    print(total_dados['percet_superior'])
    print(total_dados['percet_medio'])

elif escolha == 3:

    total_dados = conversor_percent_idade(lista_alunos)
    print(total_dados['menor_vinte'])
    print(total_dados['entre_vinte_trinta'])
    print(total_dados['maior_trinta'])

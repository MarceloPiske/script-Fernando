from utils import calc_percent


def conversor_percent_genero(lista_alunos):

    total_alunos = len(lista_alunos)

    total_dados = {}
    homens = 0
    mulheres = 0

    for aluno in lista_alunos:

        if aluno.get("genero") == "F":
            mulheres += 1
        else:
            homens += 1

    total_dados['percet_homens'] = calc_percent(homens, total_alunos)
    total_dados['percet_mulheres'] = calc_percent(mulheres, total_alunos)

    return total_dados

def conversor_percent_ensino(lista_alunos):

    total_alunos = len(lista_alunos)

    total_dados = {}
    medio = 0
    superior = 0
    superior_c = 0
    pos_graduacao = 0

    for aluno in lista_alunos:
        if aluno.get("escolaridade") == "M":
                medio += 1
        elif aluno.get("escolaridade") == "S":
            superior += 1
        elif aluno.get("escolaridade") == "PS":
            pos_graduacao += 1

    total_dados['percet_pos'] = calc_percent(pos_graduacao, total_alunos)
    total_dados['percet_superior'] = calc_percent(superior, total_alunos)
    total_dados['percet_medio'] = calc_percent(medio, total_alunos)

    return total_dados

def conversor_percent_idade(lista_alunos):

    total_alunos = len(lista_alunos)
    total_dados = {}
    menor_vinte = 0
    entre_vinte_trinta = 0
    maior_trinta = 0

    for aluno in lista_alunos:
        if aluno.get("idade") < 20:
            menor_vinte += 1
        elif aluno.get("idade") < 30:
            entre_vinte_trinta += 1
        else:
            maior_trinta += 1

    total_dados['menor_vinte'] = calc_percent(menor_vinte, total_alunos)
    total_dados['entre_vinte_trinta'] = calc_percent(entre_vinte_trinta, total_alunos)
    total_dados['maior_trinta'] = calc_percent(maior_trinta, total_alunos)

    return total_dados
    
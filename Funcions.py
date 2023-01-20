# Bibliotecas necessarias para a conexão e envio de dados para o banco
import json
import requests


# Função específica para o cadastro de novo aluno
def novoAluno(matricula, link, chaveMat):
    Alunos = requests.get(f"{link}/.json")

    # Dois parametros para a verificação da matrícula atual
    matriculaReal = 0
    listaMatricula = list()

    # Informações para o cadastramento do aluno
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    sala = int(input("Qual a sala do aluno(digite a numeração):\n"
                     "1 - Classe A\n"
                     "2 - Classe B\n"
                     "3 - Classe C\n"))

    # Laço que irá forçar uma das 3 opções de sala
    while True:
        if sala in [1, 2, 3]:
            break

        sala = int(input("Qual a sala do aluno:\n"
                         "1 - A\n"
                         "2 - B\n"
                         "3 - C\n"))

    # A parti da opção irá selecionar a sala adequada
    match sala:
        case 1:
            sala = "A"

        case 2:
            sala = "B"

        case 3:
            sala = "C"

    # Conexão para verificar se as informações mencionadas já existem
    verificacao = requests.get(f"{link}/.json")

    # Condisão é necessaria, pois só entrará se existir algum aluno previamente cadastrado
    if verificacao.text != 'null':
        for i in verificacao.json():

            info = verificacao.json()[i]

            while nome == info["Nome"] and idade == info["Idade"] and sala == info["Sala"]:
                print("Aluno já cadastrado")
                nome = input("Digite o nome do aluno: ")
                idade = int(input("Digite a idade do aluno: "))
                sala = int(input("Qual a sala do aluno(digite a numeração):\n"
                                 "1 - Classe A\n"
                                 "2 - Classe B\n"
                                 "3 - Classe C\n"))

                while True:
                    if sala in [1, 2, 3]:
                        break

                    sala = int(input("Qual a sala do aluno:\n"
                                     "1 - A\n"
                                     "2 - B\n"
                                     "3 - C\n"))

                match sala:
                    case 1:
                        sala = "A"

                    case 2:
                        sala = "B"

                    case 3:
                        sala = "C"

    """Verificação de buracos de matricula, onde não será possivel pular numeros de matriculas, não podendo
    ficar 1, 3, 5."""
    if matricula != 1:
        # Adicionará todas as matrículas a uma lista
        for i in Alunos.json():
            listaMatricula.append(Alunos.json()[i]["Matricula"])

        # Verificação se não há buracos na lista
        for i in range(1, matricula + 1):
            if i not in listaMatricula:
                matriculaReal = i
                break
            # Se não houver a matrícula atual será inserida
            else:
                matriculaReal = matricula
                matricula += 1
    else:
        matriculaReal = matricula

    # Adicionando as infomações do aluno no dicionário
    NovoAluno = {"Nome": nome, "Idade": idade, "Matricula": matriculaReal, "Sala": sala}

    # Mandando as iformações do aluno para o banco de dados
    requests.post(f"{link}/.json", data=json.dumps(NovoAluno))

    # Atualização do número da matrícula atual
    requests.patch(f"{chaveMat}/.json", data=json.dumps({"Matricula": matricula}))

    listaMatricula.clear()


def apagarAluno(link):
    confirmacao = 0

    Alunos = requests.get(f"{link}/.json")

    if Alunos.text != "null":
        for i in Alunos.json():

            print("==========================================")

            for j in Alunos.json()[i]:
                print(f"{j}: {Alunos.json()[i][j]}")
    else:
        print("Nenhum Aluno Cadastrado")

    matricula = int(input("Digite o numero da matricula para deletar: "))

    for i in Alunos.json():
        for j in Alunos.json()[i]:
            if matricula == Alunos.json()[i][j]:
                requests.delete(f"{link}/{i}/.json")
                confirmacao += 1

    if confirmacao == 0:
        print("Aluno não encontrado")


def verAlunos(link):
    Alunos = requests.get(f"{link}/.json")

    if Alunos.text != "null":
        for i in Alunos.json():

            print("==========================================")

            for j in Alunos.json()[i]:
                print(f"{j}: {Alunos.json()[i][j]}")
    else:
        print("Nenhum Aluno Cadastrado")


def altAlunos(link):
    contador = 0

    Alunos = requests.get(f"{link}/.json")

    if Alunos.text != "null":
        for i in Alunos.json():

            print("==========================================")

            for j in Alunos.json()[i]:
                print(f"{j}: {Alunos.json()[i][j]}")
    else:
        print("Nenhum Aluno Cadastrado")

    matricula = int(input("Digite o numero da matricula para alterar: "))

    for i in Alunos.json():
        for j in Alunos.json()[i]:
            if matricula == Alunos.json()[i][j]:
                nome = input("Digite o nome do aluno: ")
                idade = int(input("Digite a idade do aluno: "))
                sala = int(input("Qual a sala do aluno(digite a numeração):\n"
                                 "1 - Classe A\n"
                                 "2 - Classe B\n"
                                 "3 - Classe C\n"))

                while True:
                    if sala in [1, 2, 3]:
                        break

                    sala = int(input("Qual a sala do aluno:\n"
                                     "1 - A\n"
                                     "2 - B\n"
                                     "3 - C\n"))

                match sala:
                    case 1:
                        sala = "A"

                    case 2:
                        sala = "B"

                    case 3:
                        sala = "C"

                newAluno = {"Nome": nome, "Idade": idade, "Matricula": matricula, "Sala": sala}

                requests.patch(f"{link}/{i}/.json", data=json.dumps(newAluno))
                contador += 1

    if contador == 0:
        print("Aluno não encontrado")

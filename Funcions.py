import json
import requests


def novoAluno(matricula, link, chaveMat):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    sala = input("Qual a sala do aluno: ")

    verificacao = requests.get(f"{link}/.json")

    if verificacao.text != 'null':
        for i in verificacao.json():

            a = verificacao.json()[i]

            while nome == a["Nome"] and idade == a["Idade"] and sala == a["Sala"]:
                print("Aluno já cadastrado")
                nome = input("Digite outro nome: ")
                idade = int(input("Digite novamente a idade do aluno: "))
                sala = input("Digite novamente a Sala: ")

    Alunos = {"Nome": nome, "Idade": idade, "Matricula": matricula, "Sala": sala}

    requests.post(f"{link}/.json", data=json.dumps(Alunos))

    requests.patch(f"{chaveMat}/.json", data=json.dumps({"Matricula": matricula + 1}))


def apagarAluno(link):
    contador = 0

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
                contador += 1

    if contador == 0:
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
                sala = input("Qual a sala do aluno: ")

                newAluno = {"Nome": nome, "Idade": idade, "Matricula": matricula, "Sala": sala}

                requests.patch(f"{link}/{i}/.json", data=json.dumps(newAluno))
                contador += 1

    if contador == 0:
        print("Aluno não encontrado")

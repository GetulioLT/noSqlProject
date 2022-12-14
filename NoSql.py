import json
import requests

mat = requests.get("https://teste-in-getu-default-rtdb.firebaseio.com/.json")

if mat.text == "null":
    requests.post("https://teste-in-getu-default-rtdb.firebaseio.com/.json", data=json.dumps({"Matricula": 1}))

mat = requests.get("https://teste-in-getu-default-rtdb.firebaseio.com/.json")

for i in mat.json():
    for j in mat.json()[i]:
        if j == "Matricula":
            chaveMat = f"https://teste-in-getu-default-rtdb.firebaseio.com/{i}"

matricula = requests.get(f"{chaveMat}/.json").json()["Matricula"]
link = "https://teste-in-getu-default-rtdb.firebaseio.com/Alunos"


def novoAluno(matricula):
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


# def apagarAluno():


# def verAlunos():


print("Bem Vindo ao Sitema Escolar")

while True:
    escolha = int(input("Para prosseguir Digite uma das opções:\n" +
                        "1 - Cadastrar novo Aluno\n" +
                        "2 - Ver Todos os Alunos\n" +
                        "3 - Deletar um aluno\n" +
                        "0 - Sair\n"))

    match escolha:
        case 1:
            novoAluno(matricula)
            input("Matricula Feita, Aperte enter para continuar")
            matricula += 1

        case 0:
            break

    print("\n" * 124)

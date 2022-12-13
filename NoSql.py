import requests, json
from Funcions import *

mat = requests.get("https://teste-in-getu-default-rtdb.firebaseio.com/.json").json()["Matricula"]

matricula = mat
link = "https://teste-in-getu-default-rtdb.firebaseio.com/Alunos"

def novoAluno(matricula):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    sala = input("Qual a sala do aluno: ")

    verificacao = requests.get(f"{link}/.json")

    if verificacao.text != 'null':
        for i in verificacao.json():

            a = verificacao.json()[i]

            if nome == a["Nome"] and idade == a["Idade"] and sala == a["Sala"]:
                print("Aluno já cadastrado")
                nome = input("Digite outro nome: ")
                idade = int(input("Digite novamente a idade do aluno: "))
                sala = input("Digite novamente a Sala: ")

    
    Alunos = {"Nome" : nome, "Idade" : idade, "Matricula" : matricula, "Sala" : sala}

    matricula += 1

    requisicao = requests.post(f"{link}/.json", data=json.dumps(Alunos))

    requests.patch("https://teste-in-getu-default-rtdb.firebaseio.com/.json", data=json.dumps({"Matricula": matricula}))

#def apagarAluno():


#def verAlunos():

'''Alunos = {"Nome" : "Eduardo", "Idade" : 20, "Turma" : "B", "Matricula" : "0001"}

requisicao = requests.post(f"{link}/Alunos/.json", data= json.dumps(Alunos))

#Alunos = {"Nome" : "João", "Idade" : 19, "Turma" : "A", "Matricula" : "0010"}

requisicao = requests.patch(f"{link}/Alunos/-NJAak5DZGYNEc5PvANi/.json" , data=json.dumps(Alunos))
requisicao = requests.get(f"{link}/.json")

for i in requisicao.json():
    for j in requisicao.json()[i]:
        #print(f"{j} : {requisicao.json()[i][j]}")

        print(j)

        for k in requisicao.json()[i][j]:
            
            print(f"{k} : {requisicao.json()[i][j][k]}")
        
        print("==============================")


requisicao = requests.delete(f"{link}/Alunos/-NJAak5DZGYNEc5PvANi/.json")

print(requisicao)
print(requisicao.text)'''



print("Bem Vindo ao Sitema Escolar")

while True:
    escolha = int(input("Para prosseguir Digite uma das opções:\n"+
    "1 - Cadastrar novo Aluno\n"+
    "2 - Ver Todos os Alunos\n" +
    "3 - Deletar um aluno\n" +
    "0 - Sair\n"))

    match escolha:
        case 1:
            novoAluno(matricula)
            input("Matricula Feita, Aperte enter para continuar")

        case 0:
            break


    print ("\n" * 130) 
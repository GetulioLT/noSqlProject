from Funcions import *

link_mat = "https://teste-in-getu-default-rtdb.firebaseio.com/"

mat = requests.get(f"{link_mat}.json")

if mat.text == "null":
    requests.post(f"{link_mat}.json",
                  data=json.dumps({"Matricula": 1}))

mat = requests.get(f"{link_mat}.json")

for i in mat.json():
    for j in mat.json()[i]:
        if j == "Matricula":
            chaveMat = f"{link_mat}{i}"

matricula = requests.get(f"{chaveMat}/.json").json()["Matricula"]
link = "https://teste-in-getu-default-rtdb.firebaseio.com/Alunos"

print("Bem Vindo ao Sitema Escolar")

while True:
    escolha = int(input("Para prosseguir Digite uma das opções:\n" +
                        "1 - Cadastrar novo Aluno\n" +
                        "2 - Ver Todos os Alunos\n" +
                        "3 - Deletar um aluno\n" +
                        "4 - Resetar sistema\n" +
                        "5 - Alterar informações\n" +
                        "0 - Sair\n"))

    match escolha:
        case 1:
            novoAluno(matricula, link, chaveMat)
            input("Matricula Feita, Aperte enter para continuar...")
            matricula += 1

        case 2:
            verAlunos(link)
            input("==========================================\n" +
                  "Aperte enter para continuar...")

        case 3:
            apagarAluno(link)
            input("Aluno deletado com sucesso, Aperte enter para continuar...")

        case 4:
            requests.delete("https://teste-in-getu-default-rtdb.firebaseio.com/.json")

        case 5:
            altAlunos(link)

        case 0:
            break

        case _:
            print("Essa opção não existe")
            input("Aperte enter pra continuar...")

    print("\n" * 50)

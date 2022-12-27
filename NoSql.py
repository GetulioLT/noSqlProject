'''
Pagina de código com todo o controle do banco de dados, tendo primeiramente a
importação da pagina de código das funções.
'''

#Importação da pag funcions
from Funcions import *

#Link do bancos de dados
link = "https://teste-in-getu-default-rtdb.firebaseio.com/"

#link para pegar o valor atual de matricula
link_mat = link

#Adicionado ao link a parte de alunos, para assim criar uma aba só pros alunos
link += "Alunos"

#Pegando o valor atual da matricula e atribuindo a uma variavel
mat = requests.get(f"{link_mat}.json")

#Condição de verificação do sistema, caso não tenha nenhum dado iniciar a matricula em 1
if mat.text == "null":
    requests.post(f"{link_mat}.json",
                  data=json.dumps({"Matricula": 1}))

#Requisitando a matricula novamente
mat = requests.get(f"{link_mat}.json")

#Pegando o link da matricula, onde irá buscar qual a chave aleatoria atual
for i in mat.json():
    for j in mat.json()[i]:
        if j == "Matricula":
            chaveMat = f"{link_mat}{i}"

#Pegando o numero da matricula
matricula = requests.get(f"{chaveMat}/.json").json()["Matricula"]

print("Bem Vindo ao Sitema Escolar")

#Laço idefinido que irá roda o sistem de modo a se repetir até digitar 0
while True:
    escolha = int(input("Para prosseguir Digite uma das opções:\n" +
                        "1 - Cadastrar novo Aluno\n" +
                        "2 - Ver Todos os Alunos\n" +
                        "3 - Deletar um aluno\n" +
                        "4 - Resetar sistema\n" +
                        "5 - Alterar informações\n" +
                        "0 - Sair\n"))

    #Irá analisar a escolha e a parti dela fazer uma ação logo em seguida
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
            matricula = 1
            input("Sistema resetado com sucesso, Aperte enter para continuar...")

        case 5:
            altAlunos(link)

        case 0:
            break

        case _:
            print("Essa opção não existe")
            input("Aperte enter pra continuar...")

    print("\n" * 50)

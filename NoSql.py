"""
Pagina de código com todo o controle do banco de dados, tendo primeiramente a
importação da pagina de código das funções.
"""

# Importação da pag. Funcions
from Funcions import *

# Conexão do banco de dados
link = "https://nosql-46e99-default-rtdb.firebaseio.com/"

# link para pegar o valor atual de matricula
link_mat = link

# Adicionado ao link a parte de alunos, para assim criar uma aba só pros alunos
link += "Alunos"

# Pegando o valor atual da matrícula e atribuindo a uma variavel
mat = requests.get(f"{link_mat}.json")

# Condição de verificação do sistema, caso não tenha nenhum dado iniciar a matrícula em 1
if mat.text == "null":
    requests.post(f"{link_mat}.json",
                  data=json.dumps({"Matricula": 1}))

# Requisitando a matricula novamente
mat = requests.get(f"{link_mat}.json")

# Pegando o link da matricula, onde irá buscar qual a chave aleatoria atual
for i in mat.json():
    for j in mat.json()[i]:
        if j == "Matricula":
            chaveMat = f"{link_mat}{i}"

# Pegando o número da matricula
matricula = requests.get(f"{chaveMat}/.json").json()["Matricula"]

print("Bem Vindo ao Sitema Escolar")

# Laço idefinido que irá roda o sistem de modo a se repetir até digitar 0
while True:
    escolha = int(input("Para prosseguir Digite uma das opções:\n"
                        "1 - Cadastrar novo Aluno\n"
                        "2 - Ver Todos os Alunos\n"
                        "3 - Deletar um aluno\n"
                        "4 - Resetar sistema\n"
                        "5 - Alterar informações\n"
                        "0 - Sair\n"))

    # Irá analisar a escolha e a parti dela fazer uma ação logo em seguida
    match escolha:
        # Primeira opção irá fazer o cadastro de um novo aluno
        case 1:
            novoAluno(matricula, link, chaveMat)
            input("Matricula Feita, Aperte enter para continuar...")
            matricula += 1

        # Irá Pegar todos os alunos até então cadastrados no sistema
        case 2:
            verAlunos(link)
            input("==========================================\n" +
                  "Aperte enter para continuar...")

        # Irá deletar um aluno especifico
        case 3:
            apagarAluno(link)
            input("Aluno deletado com sucesso, Aperte enter para continuar...")

        # Irá resetar o sistema geral
        case 4:
            requests.delete(f"{link_mat}.json")
            matricula = 1
            input("Sistema resetado com sucesso, Aperte enter para continuar...")

        # Irá alterar as informações de um aluno especifico
        case 5:
            altAlunos(link)
            input("Dados atualizados com sucesso, Aperte enter para continuar...")

        # Finalizará o sistema
        case 0:
            break

        # Quando for selecionado uma opção que não existe irá cair nesse case
        case _:
            print("Essa opção não existe")
            input("Aperte enter pra continuar...")

    print("\n" * 50)

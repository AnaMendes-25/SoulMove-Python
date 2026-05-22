
atividades = []  # lista que vai guardar todas as atividades cadastradas pelos usuários.

modalidades = ("Ciclismo", "Corrida/Caminhada") # tupla que nao pode ser alterada

def calcular_pontos(modalidade, distancia, commute): 
    if modalidade == "Ciclismo":
        if commute == "S":
            pontos = distancia * 12
        else:
            pontos = distancia * 8

    elif modalidade == "Corrida/Caminhada": 
        if commute == "S":
            pontos = distancia * 9
        else:
            pontos = distancia * 6

    return pontos


def registrar_atividade():
    print("\n--- Registrar Atividade ---")

    nome = input("Digite seu nome: ")

    if nome == "": # verifica se o nome ficou vazio.
        print("Erro: o nome não pode ficar vazio.")
        return

    print("\nEscolha a modalidade:")
    print("1 - Ciclismo")
    print("2 - Corrida/Caminhada")

    opcao_modalidade = input("Digite a opção: ")

    if opcao_modalidade == "1":
        modalidade = modalidades[0] # se escolheu 1, a modalidade será o primeiro item da tupla.

    elif opcao_modalidade == "2":
        modalidade = modalidades[1]

    else:
        print("Erro: modalidade inválida.")
        return

    commute = input("Foi um deslocamento para trabalho/faculdade? Digite S ou N: ")
    commute = commute.upper()

    if commute != "S" and commute != "N":
        print("Erro: digite apenas S ou N.")
        return

    distancia = float(input("Digite a distância em km: "))

    if distancia <= 0:
        print("Erro: a distância precisa ser maior que zero.")
        return

    comprovante = input("Digite o nome da foto ou print de comprovação: ")

    if comprovante == "":
        print("Erro: precisa informar um comprovante.")
        return

    pontos = calcular_pontos(modalidade, distancia, commute) #Aqui chamamos a função calcular_pontos

    atividade = [nome, modalidade, commute, distancia, comprovante, pontos] # Aqui criamos uma lista com todos os dados da atividade.

    atividades.append(atividade)

    print("\nAtividade cadastrada com sucesso!")
    print("Pontos ganhos:", pontos)


def mostrar_historico(): # mostrar todas as atividades cadastradas.
    print("\n--- Histórico de Atividades ---")

    if len(atividades) == 0:
        print("Nenhuma atividade cadastrada.")
    else:
        for atividade in atividades: # “Para cada atividade dentro da lista atividades, faça isso…”
            print("----------------------")
            print("Nome:", atividade[0])
            print("Modalidade:", atividade[1])
            print("Commute:", atividade[2])
            print("Distância:", atividade[3], "km")
            print("Comprovante:", atividade[4])
            print("Pontos:", atividade[5])


def mostrar_dashboard(): # pontos totais de um usuário.
    print("\n--- Meu Dashboard ---")

    nome_pesquisado = input("Digite seu nome: ")

    total = 0 # Depois, o programa vai somar os pontos do usuário nela.

    for atividade in atividades:
        if atividade[0] == nome_pesquisado: # Verifica se o nome NA atividade(0 é o nome) é igual ao nome pesquisado.
            total = total + atividade[5]

    print("Usuário:", nome_pesquisado)
    print("Total de pontos:", total)

    if total < 100:
        print("Nível: Iniciante")
    elif total < 300:
        print("Nível: Eco Atleta")
    else:
        print("Nível: Mestre SoulMove")


def menu(): 
    while True:
        print("\n====== SOULMOVE ======")
        print("1 - Registrar atividade")
        print("2 - Ver dashboard")
        print("3 - Ver histórico")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                registrar_atividade()

            case "2":
                mostrar_dashboard()

            case "3":
                mostrar_historico()

            case "4":
                print("Saindo do sistema...")
                break

            case _: # vazio 
                print("Opção inválida. Escolha uma opção de 1 a 4.")


menu() # chama a função menu para iniciar o programa.
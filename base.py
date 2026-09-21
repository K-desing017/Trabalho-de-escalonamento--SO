import random

# Define o maior tempo que o programa pode simular.
MAXIMO_TEMPO_EXECUCAO = 65535

# Quantidade de processos que serão utilizados no programa.
n_processos = 3


def main():

    # Cria uma lista para armazenar o tempo de execução de cada processo.
    tempo_execucao = [0] * n_processos

    # Cria uma lista para armazenar o momento em que cada processo chega.
    tempo_chegada = [0] * n_processos

    # Cria uma lista para armazenar a prioridade de cada processo.
    prioridade = [0] * n_processos

    # Cria uma lista para armazenar o tempo que cada processo ficou esperando.
    tempo_espera = [0] * n_processos

    # Cria uma lista para armazenar quanto tempo falta para cada processo terminar.
    tempo_restante = [0] * n_processos

    # Mantém o menu funcionando até o usuário escolher sair.
    while True:

        print("\n===== MENU =====")
        print("1 - Popular processos")
        print("2 - FCFS")
        print("3 - SJF Preemptivo")
        print("4 - SJF Não-Preemptivo")
        print("5 - Prioridade Preemptivo")
        print("6 - Prioridade Não-Preemptivo")
        print("7 - Round Robin")
        print("8 - Mostrar processos")
        print("9 - Sair")

        # Lê a opção escolhida pelo usuário.
        opcao = int(input("Escolha uma opção: "))

        # Opção para criar/preencher os processos.
        if opcao == 1:
            popular_processos(
                tempo_execucao,
                tempo_chegada,
                prioridade,
                tempo_espera,
                tempo_restante
            )

        # Executa o algoritmo FCFS.
        elif opcao == 2:
            FCFS(
                tempo_execucao,
                tempo_espera,
                tempo_restante,
                tempo_chegada
            )

        # Executa o SJF preemptivo.
        # True informa para a função que o algoritmo deve ser preemptivo.
        elif opcao == 3:
            SJF(
                True,
                tempo_execucao,
                tempo_espera,
                tempo_restante,
                tempo_chegada
            )

        # Executa o SJF não-preemptivo.
        # False informa para a função que o processo não pode ser interrompido.
        elif opcao == 4:
            SJF(
                False,
                tempo_execucao,
                tempo_espera,
                tempo_restante,
                tempo_chegada
            )

        # Essas partes ainda serão implementadas posteriormente.
        elif opcao == 5:
            print("Prioridade Preemptivo ainda não implementado.")

        elif opcao == 6:
            print("Prioridade Não-Preemptivo ainda não implementado.")

        elif opcao == 7:
            print("Round Robin ainda não implementado.")

        # Mostra os dados dos processos cadastrados.
        elif opcao == 8:
            imprime_processos(
                tempo_execucao,
                tempo_chegada,
                prioridade
            )

        # Encerra o programa.
        elif opcao == 9:
            print("Programa encerrado.")
            break

        # Caso o usuário escolha uma opção que não existe.
        else:
            print("Opção inválida.")


def popular_processos(
        tempo_execucao,
        tempo_chegada,
        prioridade,
        tempo_espera,
        tempo_restante
):

    print("\nSerá aleatório?")
    print("1 - Sim")
    print("2 - Não")

    # Pergunta se os dados dos processos serão gerados
    # automaticamente ou informados pelo usuário.
    opcao = int(input("Escolha: "))

    # Percorre todos os processos para preencher seus dados.
    for i in range(n_processos):

        # Se escolher 1, os valores são gerados aleatoriamente.
        if opcao == 1:

            # Gera um tempo de execução entre 1 e 10.
            tempo_execucao[i] = random.randint(1, 10)

            # Gera um tempo de chegada entre 1 e 10.
            tempo_chegada[i] = random.randint(1, 10)

            # Gera uma prioridade entre 1 e 15.
            prioridade[i] = random.randint(1, 15)

        # Se escolher qualquer outra opção, o usuário informa os valores.
        else:

            print("\nProcesso", i)

            # Recebe o tempo de execução do processo.
            tempo_execucao[i] = int(
                input("Tempo de execução: ")
            )

            # Recebe o tempo de chegada do processo.
            tempo_chegada[i] = int(
                input("Tempo de chegada: ")
            )

            # Recebe a prioridade do processo.
            prioridade[i] = int(
                input("Prioridade: ")
            )

        # Todo processo começa com tempo de espera igual a zero.
        tempo_espera[i] = 0

        # No início, o tempo restante é igual ao tempo total de execução.
        tempo_restante[i] = tempo_execucao[i]


def imprime_processos(
        tempo_execucao,
        tempo_chegada,
        prioridade
):

    print("\n===== PROCESSOS =====")

    # Percorre todos os processos e mostra seus dados.
    for i in range(n_processos):

        print(
            "P" + str(i),
            "exec=" + str(tempo_execucao[i]),
            "chegada=" + str(tempo_chegada[i]),
            "prioridade=" + str(prioridade[i])
        )


def imprime_stats(espera):

    # Variável utilizada para somar o tempo de espera de todos os processos.
    soma = 0

    print("\n===== TEMPO DE ESPERA =====")

    # Percorre todos os processos para mostrar o tempo de espera.
    for i in range(n_processos):

        print(
            "P" + str(i) + ":",
            espera[i]
        )

        # Adiciona o tempo de espera do processo à soma.
        soma = soma + espera[i]

    # Calcula o tempo médio de espera.
    media = soma / n_processos

    print("Tempo médio de espera:", media)


def FCFS(execucao, espera, restante, chegada):

    # Cria cópias das listas para que o algoritmo
    # não altere os dados originais dos processos.
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)

    # Começa executando o primeiro processo da lista.
    processo_em_execucao = 0

    # Percorre os tempos da simulação.
    for i in range(1, MAXIMO_TEMPO_EXECUCAO):

        print(
            "tempo[" + str(i) +
            "]: processo[" + str(processo_em_execucao) +
            "] restante=" +
            str(tempo_restante[processo_em_execucao])
        )

        # Verifica se o processo ainda não começou a executar.
        # Nesse momento, calcula o seu tempo de espera.
        if tempo_execucao[processo_em_execucao] == tempo_restante[processo_em_execucao]:
            tempo_espera[processo_em_execucao] = i - 1

        # Verifica se o processo está no seu último tempo de execução.
        if tempo_restante[processo_em_execucao] == 1:

            # Se for o último processo, encerra a execução do FCFS.
            if processo_em_execucao == (n_processos - 1):
                break

            # Caso contrário, passa para o próximo processo.
            else:
                processo_em_execucao = processo_em_execucao + 1

        # Se ainda não terminou, diminui um do tempo restante.
        else:
            tempo_restante[processo_em_execucao] = (
                tempo_restante[processo_em_execucao] - 1
            )

    # Mostra o tempo de espera de cada processo e a média.
    imprime_stats(tempo_espera)


def SJF(preemptivo, execucao, espera, restante, chegada):

    # Faz cópias das listas originais.
    # Assim, executar o SJF não modifica os dados cadastrados.
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)
    tempo_chegada = list(chegada)

    # Representa o tempo atual da simulação.
    tempo_atual = 1

    # Conta quantos processos já terminaram.
    processos_finalizados = 0

    # Continua executando enquanto ainda houver processos
    # que não terminaram.
    while processos_finalizados < n_processos:

        # Lista que vai guardar os processos que já chegaram
        # e ainda possuem tempo de execução.
        processos_disponiveis = []

        # Percorre todos os processos para verificar
        # quais podem ser executados naquele momento.
        for i in range(n_processos):

            # O processo está disponível quando:
            # 1. Seu tempo de chegada já foi atingido.
            # 2. Ainda existe tempo para ele executar.
            if (
                tempo_chegada[i] <= tempo_atual
                and tempo_restante[i] > 0
            ):
                processos_disponiveis.append(i)

        # Se nenhum processo estiver disponível,
        # o relógio avança para o próximo processo que chegará.
        if len(processos_disponiveis) == 0:

            tempo_atual = min(
                tempo_chegada[i]
                for i in range(n_processos)
                if tempo_restante[i] > 0
            )

            continue

        # =====================================================
        # SJF PREEMPTIVO
        # =====================================================
        # No SJF preemptivo, também conhecido como Shortest
        # Remaining Time First, o processo escolhido é aquele
        # que possui o menor tempo RESTANTE.
        #
        # Como ele é preemptivo, pode ser interrompido caso
        # outro processo tenha um tempo restante menor.
        if preemptivo:

            # Escolhe, entre os processos disponíveis,
            # aquele que possui o menor tempo restante.
            processo = min(
                processos_disponiveis,
                key=lambda i: tempo_restante[i]
            )

            # Mostra qual processo está executando naquele momento.
            print(
                "tempo[" + str(tempo_atual) +
                "]: processo[" + str(processo) +
                "] restante=" +
                str(tempo_restante[processo])
            )

            # Executa o processo durante uma unidade de tempo.
            tempo_restante[processo] = (
                tempo_restante[processo] - 1
            )

            # Avança o relógio da simulação em uma unidade.
            tempo_atual = tempo_atual + 1

            # Verifica se o processo terminou.
            if tempo_restante[processo] == 0:

                # Calcula o tempo de espera:
                # tempo de conclusão - tempo de chegada
                # - tempo total de execução.
                tempo_espera[processo] = (
                    tempo_atual
                    - tempo_chegada[processo]
                    - tempo_execucao[processo]
                )

                # Aumenta a quantidade de processos finalizados.
                processos_finalizados = (
                    processos_finalizados + 1
                )

        # =====================================================
        # SJF NÃO-PREEMPTIVO
        # =====================================================
        # No SJF não-preemptivo, escolhemos o processo disponível
        # com o menor TEMPO TOTAL DE EXECUÇÃO.
        #
        # Depois que o processo começa, ele continua executando
        # até terminar. Ele não pode ser interrompido.
        else:

            # Escolhe o processo disponível que possui
            # o menor tempo total de execução.
            processo = min(
                processos_disponiveis,
                key=lambda i: tempo_execucao[i]
            )

            # Executa o processo até que seu tempo restante
            # seja igual a zero.
            while tempo_restante[processo] > 0:

                # Mostra o processo que está executando
                # e quanto tempo ainda falta.
                print(
                    "tempo[" + str(tempo_atual) +
                    "]: processo[" + str(processo) +
                    "] restante=" +
                    str(tempo_restante[processo])
                )

                # Diminui uma unidade do tempo restante.
                tempo_restante[processo] = (
                    tempo_restante[processo] - 1
                )

                # Avança o tempo da simulação.
                tempo_atual = tempo_atual + 1

            # Quando o processo termina, calcula seu tempo de espera.
            tempo_espera[processo] = (
                tempo_atual
                - tempo_chegada[processo]
                - tempo_execucao[processo]
            )

            # Registra que mais um processo foi finalizado.
            processos_finalizados = (
                processos_finalizados + 1
            )

    # Depois que todos os processos terminarem,
    # mostra os tempos de espera e a média.
    imprime_stats(tempo_espera)


# Inicia a execução do programa.
main()

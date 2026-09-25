"""
Sistemas Operacionais - IFRS Campus Restinga - ADS 3N - 2026/2
Trabalho de Desenvolvimento: simulador de algoritmos de escalonamento de processos.

Codigo-base em Python. Equivalente ao base.java, com a mesma estrutura de dados
(listas paralelas), o mesmo menu e a mesma saida.

FCFS, SJF preemptivo e SJF nao preemptivo implementados.
Prioridade e Round Robin ainda serao implementados.
"""

# Importa a biblioteca random para gerar valores aleatorios.
import random


# Define o tempo maximo da simulacao.
MAXIMO_TEMPO_EXECUCAO = 65535

# Define a quantidade de processos.
n_processos = 3

# Ela é a função principal que organiza e controla a execução do programa.
def main():

    # Lista que armazena o tempo total de execucao de cada processo.
    tempo_execucao = [0] * n_processos

    # Lista que armazena o momento em que cada processo chega.
    tempo_chegada = [0] * n_processos

    # Lista que armazena a prioridade de cada processo.
    prioridade = [0] * n_processos

    # Lista que armazena o tempo que cada processo ficou esperando.
    tempo_espera = [0] * n_processos

    # Lista que armazena quanto tempo ainda falta para cada processo terminar.
    tempo_restante = [0] * n_processos

    # Preenche os dados dos processos.
    popular_processos(
        tempo_execucao,
        tempo_espera,
        tempo_restante,
        tempo_chegada,
        prioridade
    )

    # Mostra os processos cadastrados.
    imprime_processos(
        tempo_execucao,
        tempo_espera,
        tempo_restante,
        tempo_chegada,
        prioridade
    )

    # Mantem o menu funcionando ate o usuario escolher a opcao 9.
    while True:

        # Mostra as opcoes disponiveis.
        alg = int(input(
            "Escolha o algoritmo?: "
            "[1=FCFS "
            "2=SJF Preemptivo "
            "3=SJF Nao Preemptivo "
            "4=Prioridade Preemptivo "
            "5=Prioridade Nao Preemptivo "
            "6=Round_Robin "
            "7=Imprime lista de processos "
            "8=Popular processos novamente "
            "9=Sair]: "
        ))

        # Executa o FCFS.
        if alg == 1:

            FCFS(
                tempo_execucao,
                tempo_espera,
                tempo_restante,
                tempo_chegada
            )

        # Executa o SJF preemptivo.
        # True significa que o algoritmo pode interromper processos.
        elif alg == 2:

            SJF(
                True,
                tempo_execucao,
                tempo_espera,
                tempo_restante,
                tempo_chegada
            )

        # Executa o SJF nao preemptivo.
        # False significa que o processo nao sera interrompido.
        elif alg == 3:

            SJF(
                False,
                tempo_execucao,
                tempo_espera,
                tempo_restante,
                tempo_chegada
            )

        # Prioridade preemptivo ainda nao implementado.
        elif alg == 4:

            PRIORIDADE(
                True,
                tempo_execucao,
                tempo_espera,
                tempo_restante,
                tempo_chegada,
                prioridade
            )

        # Prioridade nao preemptivo ainda nao implementado.
        elif alg == 5:

            PRIORIDADE(
                False,
                tempo_execucao,
                tempo_espera,
                tempo_restante,
                tempo_chegada,
                prioridade
            )

        # Round Robin ainda nao implementado.
        elif alg == 6:

            Round_Robin(
                tempo_execucao,
                tempo_espera,
                tempo_restante
            )

        # Mostra novamente os processos.
        elif alg == 7:

            imprime_processos(
                tempo_execucao,
                tempo_espera,
                tempo_restante,
                tempo_chegada,
                prioridade
            )

        # Permite criar uma nova lista de processos.
        elif alg == 8:

            popular_processos(
                tempo_execucao,
                tempo_espera,
                tempo_restante,
                tempo_chegada,
                prioridade
            )

            # Mostra os novos processos.
            imprime_processos(
                tempo_execucao,
                tempo_espera,
                tempo_restante,
                tempo_chegada,
                prioridade
            )

        # Encerra o programa.
        elif alg == 9:
            break

        # Trata uma opcao que nao existe.
        else:
            print("Opcao invalida.")


def popular_processos(
        tempo_execucao,
        tempo_espera,
        tempo_restante,
        tempo_chegada,
        prioridade
):

    # Pergunta se os dados serao gerados aleatoriamente.
    aleatorio = int(input("Sera aleatorio?:  "))

    # Percorre todos os processos.
    for i in range(n_processos):

        # Se o usuario escolher 1, gera os valores automaticamente.
        if aleatorio == 1:

            # Gera o tempo de execucao entre 1 e 10.
            tempo_execucao[i] = random.randint(1, 10)

            # Gera o tempo de chegada entre 1 e 10.
            tempo_chegada[i] = random.randint(1, 10)

            # Gera a prioridade entre 1 e 15.
            prioridade[i] = random.randint(1, 15)

        # Caso contrario, o usuario informa os valores.
        else:

            # Recebe o tempo de execucao.
            tempo_execucao[i] = int(
                input(
                    "Digite o tempo de execucao do processo[" +
                    str(i) + "]:  "
                )
            )

            # Recebe o tempo de chegada.
            tempo_chegada[i] = int(
                input(
                    "Digite o tempo de chegada do processo[" +
                    str(i) + "]:  "
                )
            )

            # Recebe a prioridade.
            prioridade[i] = int(
                input(
                    "Digite a prioridade do processo[" +
                    str(i) + "]:  "
                )
            )

        # No inicio, o tempo restante e igual ao tempo total.
        tempo_restante[i] = tempo_execucao[i]

        # Inicialmente nenhum processo possui tempo de espera.
        tempo_espera[i] = 0


def imprime_processos(
        tempo_execucao,
        tempo_espera,
        tempo_restante,
        tempo_chegada,
        prioridade
):

    # Percorre todos os processos.
    for i in range(n_processos):

        # Mostra as informacoes de cada processo.
        print(
            "Processo[" + str(i) +
            "]: tempo_execucao=" + str(tempo_execucao[i]) +
            " tempo_restante=" + str(tempo_restante[i]) +
            " tempo_chegada=" + str(tempo_chegada[i]) +
            " prioridade=" + str(prioridade[i])
        )


def imprime_stats(espera):

    # Cria uma copia da lista de tempos de espera.
    tempo_espera = list(espera)

    # Variavel utilizada para somar todos os tempos de espera.
    tempo_espera_total = 0.0

    # Percorre todos os processos.
    for i in range(n_processos):

        # Mostra o tempo de espera de cada processo.
        print(
            "Processo[" + str(i) +
            "]: tempo_espera=" +
            str(tempo_espera[i])
        )

        # Soma o tempo de espera ao total.
        tempo_espera_total = (
            tempo_espera_total + tempo_espera[i]
        )

    # Calcula e mostra o tempo medio de espera.
    print(
        "Tempo medio de espera: " +
        str(tempo_espera_total / n_processos)
    )


def FCFS(execucao, espera, restante, chegada):

    # Faz copias das listas para nao modificar os dados originais.
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)

    # Comeca pelo processo 0.
    processo_em_execucao = 0

    # Percorre o tempo da simulacao.
    for i in range(1, MAXIMO_TEMPO_EXECUCAO):

        # Mostra o processo atual e seu tempo restante.
        print(
            "tempo[" + str(i) +
            "]: processo[" +
            str(processo_em_execucao) +
            "] restante=" +
            str(tempo_restante[processo_em_execucao])
        )

        # Se o tempo restante e igual ao tempo total,
        # significa que o processo ainda nao tinha executado.
        if tempo_execucao[processo_em_execucao] == tempo_restante[processo_em_execucao]:

            # Calcula o tempo que ele ficou esperando.
            tempo_espera[processo_em_execucao] = i - 1

        # Verifica se falta apenas uma unidade de tempo.
        if tempo_restante[processo_em_execucao] == 1:

            # Se for o ultimo processo, encerra o algoritmo.
            if processo_em_execucao == (n_processos - 1):
                break

            # Caso contrario, passa para o proximo processo.
            else:
                processo_em_execucao = (
                    processo_em_execucao + 1
                )

        # Se o processo ainda nao terminou,
        # diminui uma unidade do tempo restante.
        else:

            tempo_restante[processo_em_execucao] = (
                tempo_restante[processo_em_execucao] - 1
            )

    # Mostra os tempos de espera e a media.
    imprime_stats(tempo_espera)


def SJF(preemptivo, execucao, espera, restante, chegada):

    # Faz copias das listas.
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)
    tempo_chegada = list(chegada)

    # Comeca a simulacao no tempo 1.
    tempo_atual = 1

    # Conta quantos processos ja terminaram.
    processos_finalizados = 0

    # Continua enquanto existirem processos nao finalizados.
    while processos_finalizados < n_processos:

        # Lista dos processos que ja chegaram
        # e ainda possuem tempo para executar.
        processos_disponiveis = []

        # Verifica todos os processos.
        for i in range(n_processos):

            # O processo esta disponivel se:
            # - ja chegou;
            # - ainda nao terminou.
            if (
                tempo_chegada[i] <= tempo_atual
                and tempo_restante[i] > 0
            ):

                processos_disponiveis.append(i)

        # Se nenhum processo estiver disponivel,
        # avanca o tempo para a proxima chegada.
        if len(processos_disponiveis) == 0:

            tempo_atual = min(
                tempo_chegada[i]
                for i in range(n_processos)
                if tempo_restante[i] > 0
            )

            continue

        # ==================================================
        # SJF PREEMPTIVO
        # ==================================================
        #SJF preemptivo: escolhe o processo com menor tempo restante e pode interromper o processo atual
        if preemptivo:

            # Escolhe o processo que possui
            # o menor tempo restante.
            processo = min(
                processos_disponiveis,
                key=lambda i: tempo_restante[i]
            )

            # Mostra qual processo esta executando.
            print(
                "tempo[" + str(tempo_atual) +
                "]: processo[" +
                str(processo) +
                "] restante=" +
                str(tempo_restante[processo])
            )

            # Executa o processo por uma unidade de tempo.
            tempo_restante[processo] = (
                tempo_restante[processo] - 1
            )

            # Avanca o tempo da simulacao.
            tempo_atual = tempo_atual + 1

            # Verifica se o processo terminou.
            if tempo_restante[processo] == 0:

                # Calcula o tempo de espera.
                #
                # Tempo de espera =
                # tempo de termino
                # - tempo de chegada
                # - tempo de execucao
                tempo_espera[processo] = (
                    tempo_atual
                    - tempo_chegada[processo]
                    - tempo_execucao[processo]
                )

                # Registra que mais um processo terminou.
                processos_finalizados = (
                    processos_finalizados + 1
                )

        # ==================================================
        # SJF NAO PREEMPTIVO
        # ==================================================
        #SJF não preemptivo: escolhe o processo com menor tempo de execução e deixa ele terminar antes de trocar. ele não interrope o processo atual
        else:

            # Escolhe o processo disponivel
            # com o menor tempo TOTAL de execucao.
            processo = min(
                processos_disponiveis,
                key=lambda i: tempo_execucao[i]
            )

            # Continua executando o mesmo processo
            # ate que ele termine.
            while tempo_restante[processo] > 0:

                # Mostra o processo que esta executando.
                print(
                    "tempo[" + str(tempo_atual) +
                    "]: processo[" +
                    str(processo) +
                    "] restante=" +
                    str(tempo_restante[processo])
                )

                # Diminui uma unidade do tempo restante.
                tempo_restante[processo] = (
                    tempo_restante[processo] - 1
                )

                # Avanca o tempo.
                tempo_atual = tempo_atual + 1

            # Quando termina, calcula o tempo de espera.
            tempo_espera[processo] = (
                tempo_atual
                - tempo_chegada[processo]
                - tempo_execucao[processo]
            )

            # Registra que o processo terminou.
            processos_finalizados = (
                processos_finalizados + 1
            )

    # Mostra os tempos de espera e a media.
    imprime_stats(tempo_espera)


def PRIORIDADE(
        preemptivo,
        execucao,
        espera,
        restante,
        chegada,
        prioridade
):

    # Faz copias das listas para preparar o algoritmo.
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)
    tempo_chegada = list(chegada)
    prioridade_temp = list(prioridade)

    # Prioridade ainda sera implementado.
    print("Prioridade ainda nao implementado.")

    # Mostra as estatisticas atuais.
    imprime_stats(tempo_espera)


def Round_Robin(execucao, espera, restante):

    # Faz copias das listas para preparar o algoritmo.
    tempo_execucao = list(execucao)
    tempo_espera = list(espera)
    tempo_restante = list(restante)

    # Round Robin ainda sera implementado.
    print("Round Robin ainda nao implementado.")

    # Mostra as estatisticas atuais.
    imprime_stats(tempo_espera)


# Chama a funcao principal e inicia o programa.
main()

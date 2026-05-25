"""""
Projeto: Jogo Super Trunfo - Automóveis
Desenvolvedores: Nícolas Kenzo Santiago Takehara e Lucas Bergamo Ciciliano
"""

import random

gabarito = ["Nome", "Velocidade (km/h)", "Tanque (litros)", "Ano (int)"]

# Cria as cartas para o jogo


def criar_baralho():
    return [
        ["Toyota Yaris Cross", 175, 36, 2024],
        ["Ferrari F40", 324, 120, 1987],
        ["Lamborghini Aventador", 350, 90, 2011],
        ["Bugatti Chiron", 420, 100, 2016],
        ["Porsche 911", 310, 64, 2023],
        ["McLaren P1", 350, 72, 2013],
        ["Audi R8", 330, 83, 2021],
        ["BYD Song Plus", 170, 60, 2023],
        ["Ford Mustang GT", 250, 61, 2022],
        ["Chevrolet Corvette", 312, 70, 2020],
        ["Nissan GT-R", 315, 74, 2019],
        ["BMW M3", 290, 59, 2021]
    ]

# Decoração


def linha():
    print("=" * 50)

# Mostra a carta do topo (carta atual)


def mostrar_carta(num_jogador, carta):
    print("\n" + "=" * 50)
    print("VEZ DO JOGADOR", num_jogador)
    linha()
    print("CARTA:", carta[0])
    linha()
    for i in range(1, len(gabarito)):
        print(f"[{i}] {gabarito[i]:<20} : {carta[i]}")
    linha()

# Começa uma rodada/turno


def jogar_rodada(quem_escolhe, mao1, mao2, monte_espera, modo):
    num_oponente = 2 if quem_escolhe == 1 else 1

    # Define a carta atacante e defensora
    if quem_escolhe == 1:
        carta_atq = mao1.pop(0)
        carta_def = mao2.pop(0)
    else:
        carta_atq = mao2.pop(0)
        carta_def = mao1.pop(0)

    mostrar_carta(quem_escolhe, carta_atq)

    # Escolhe um atributo da carta
    if modo == 1 and quem_escolhe == 2:
        indice = random.randint(1, len(gabarito) - 1)
        print("O Computador escolheu:", gabarito[indice])
    else:
        indice = int(
            input(f"Jogador {quem_escolhe}, escolha o atributo (1-3): "))

    v_atq, v_def = carta_atq[indice], carta_def[indice]

    print(
        f"\nComparando {gabarito[indice]}: J{quem_escolhe}({v_atq}) vs J{num_oponente}({v_def})")

    # Verifica o vencedor da rodada
    if v_atq > v_def:
        print(f"Vencedor: JOGADOR {quem_escolhe}")
        if quem_escolhe == 1:
            mao1.extend([carta_atq, carta_def] + monte_espera)
        else:
            mao2.extend([carta_atq, carta_def] + monte_espera)

        monte_espera = []
        proximo_turno = quem_escolhe

    elif v_def > v_atq:
        print(f"Vencedor: JOGADOR {num_oponente}")
        if quem_escolhe == 1:
            mao2.extend([carta_def, carta_atq] + monte_espera)
        else:
            mao1.extend([carta_def, carta_atq] + monte_espera)

        monte_espera = []
        proximo_turno = num_oponente

    # Caso de empate
    else:
        print("Empate! Cartas vão para o monte de espera.")
        monte_espera.extend([carta_atq, carta_def])
        proximo_turno = quem_escolhe

    input("\n[Enter para continuar]")

    return proximo_turno, mao1, mao2, monte_espera

# Inicia a partida


def iniciar(modo):
    baralho = criar_baralho()
    random.shuffle(baralho)

    metade = len(baralho) // 2

    mao1 = []
    mao2 = []

    for _ in range(metade):
        mao1.append(baralho.pop(0))

    while baralho:
        mao2.append(baralho.pop(0))

    monte_espera = []
    turno = 1
    rodada = 1

    while len(mao1) > 0 and len(mao2) > 0:
        print(
            f"\nRODADA {rodada} | J1: {len(mao1)} | J2: {len(mao2)} | Monte: {len(monte_espera)}")

        turno, mao1, mao2, monte_espera = jogar_rodada(
            turno, mao1, mao2, monte_espera, modo)

        rodada += 1

    # Vencedor final
    print("\n" + "="*50)
    print("VENCEDOR: JOGADOR", (1 if len(mao1) > 0 else 2))
    print("="*50)

    input("[Enter para voltar ao menu]")

# Menu inicial/principal


def menu():
    while True:
        print("\n--- SUPER TRUNFO ---")
        print("1. Single Player\n2. Multiplayer\n3. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            iniciar(1)

        elif opcao == "2":
            iniciar(2)

        elif opcao == "3":
            print("Saindo...")
            break


menu()

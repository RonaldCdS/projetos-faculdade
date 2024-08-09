import time

def print_slow(str):
    for letter in str:
        print(letter, end="")
        time.sleep(0.1)
    print()

def intro():
    print_slow("Você acorda em uma sala escura...")
    print_slow("Não há nada além do som da sua respiração e o eco de gotas caindo ao longe...")
    print_slow("Você precisa sair daqui, mas há algo... ou alguém... observando você.")
    decision_1()

def decision_1():
    print_slow("\nHá uma porta à sua frente. Você pode tentar abri-la.")
    print_slow("O que você faz?")
    print_slow("1. Abrir a porta lentamente.")
    print_slow("2. Procurar algo na sala antes de sair.")
    
    choice = input("\nEscolha 1 ou 2: ")

    if choice == "1":
        print_slow("\nA porta range alto enquanto você a abre...")
        print_slow("Uma figura sombria aparece diante de você!")
        print_slow("Fim de jogo.")
    elif choice == "2":
        print_slow("\nVocê tateia ao redor da sala e encontra uma lanterna!")
        print_slow("Agora você pode ver melhor e se preparar para o que está por vir...")
        decision_2()
    else:
        print_slow("\nEscolha inválida. Tente novamente.")
        decision_1()

def decision_2():
    print_slow("\nCom a lanterna em mãos, você se aproxima da porta...")
    print_slow("Você ouve passos do outro lado.")
    print_slow("O que você faz?")
    print_slow("1. Abrir a porta rapidamente e enfrentar o que está lá fora.")
    print_slow("2. Esperar e escutar mais atentamente.")

    choice = input("\nEscolha 1 ou 2: ")

    if choice == "1":
        print_slow("\nVocê abre a porta com força...")
        print_slow("Mas não há ninguém. Apenas o som de passos que se afastam.")
        print_slow("Você escapou... por enquanto.")
        print_slow("Fim de jogo.")
    elif choice == "2":
        print_slow("\nVocê espera, e os passos começam a se aproximar...")
        print_slow("Antes que você possa reagir, algo o agarra!")
        print_slow("Fim de jogo.")
    else:
        print_slow("\nEscolha inválida. Tente novamente.")
        decision_2()

if __name__ == "__main__":
    intro()

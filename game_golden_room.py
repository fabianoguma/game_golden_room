from sys import exit

def gold_room():
    print("essa sala esta cheia de ouro. agora pode pega quanto quiser")

    escolha = input("> ")
    if "0" in escolha or "1" in escolha:
        quanto = int(escolha)
    else:
        morto("cara, aprenda a digita um numero")

    if quanto < 50:

        print("legal, vc nao e ganacioso, voce venceu")
        exit(0)
    else:

        print("voce esta morto por ser ganacioso!")
        exit(0)

def urso_da_sala():
    print("o urso esta aqui")
    print("o urso tem um monte de mel")
    print("o urso gordo está na frente de outra porta")
    print("como você vai mover o urso?")
    print("1 pega o mel?\n 2-bate no urso?" )
    urso_movendo = False

    while True:
        escolha = input("> ")
        if escolha == "pega o mel":
           morto("o urso olha para você e dá um tapa na sua cara")
        elif escolha == "bate no urso" and not urso_movendo:
            print("o urso esta se movendo para a porta. ")
            print("você pode passar por ele  agora, voce ve uma porta ")
            print("escolha 1-abri a porta, ou \n2-sair")
            urso_movendo = True
        elif escolha == "bate no urso " and urso_movendo:
            morto("o urso fica puto e mastiga sua perna")
        elif escolha == "abri a porta" and urso_movendo:
            gold_room()
        elif escolha == "sai":
            comeca()
        else:
            print("eu não tenho ideia do que isso significa")

def demo_sala():
    print("aqui e a grande sala do demonio ")
    print("ele que olha para você e você fica insano")
    print("você foge por sua vida ou come sua cabeça")
    print("1-fugi ou 2-luta")

    escolha = input("> ")

    if "fugi" in escolha or  escolha == 1   :
        comeca()
    elif "cabeça" in escolha:
        morto("bem, ele te comeu")
    else:
        demo_sala()


def morto(porque):
    print(porque,"voce morreu")
    exit(0)

def comeca():
    print("voce esta numa sala escura ")
    print("em frente tem duas portas pra direita e para esquerda")
    print("escolha uma e vai")

    escolha= input("> ")

    if escolha == "esquerda":
        urso_da_sala()
    elif escolha == "direita":
        demo_sala()

    else:
        morto("você tropeça pela sala até morrer de fome")

comeca()

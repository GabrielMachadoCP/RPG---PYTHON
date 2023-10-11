# Ana Zerlin        RM 98065
# Bianca Dancs      RM 551645
# Gabriel Pimentel  RM 99880
# Hellen Assis      RM 98284

#Imports
import random
import ficha
import textos

#Inimigos
inimigos = {
    "mantecora" : {
        "Nome" : "Mantecóra",
        "Habilidade" : 11,
        "Energia" : 11
    },

    "mosca_gigante" : {
        "Nome" : "Mosca Gigante",
        "Habilidade" : 7,
        "Energia" : 7
    },

    "minotauro" : {
        "Nome" : "Minotauro",
        "Habilidade" : 9,
        "Energia" : 9
    },

    "orca1" : {
        "Nome" : "Primeira Orca",
        "Habilidade" : 5,
        "Energia" : 5
    },

    "orca2" : {
        "Nome" : "Segunda Orca",
        "Habilidade" : 6,
        "Energia" : 4
    },

    "goblin1" : {
    "Nome" : "Primeiro Goblin",
    "Habilidade" : 5,
    "Energia" : 4
    },

    "goblin2" : {
        "Nome" : "Segundo Goblin",
        "Habilidade" : 5,
        "Energia" : 5
    },

    "hobgoblin1" : {
    "Nome" : "Primeiro Hobgoblin",
    "Habilidade" : 7,
    "Energia" : 5
    },

    "hobgoblin2" : {
        "Nome" : "Segundo Hobgoblin",
        "Habilidade" : 6,
        "Energia" : 5
    },

    "erva" : {
        "Nome" : "Erva",
        "Habilidade" : 9,
        "Energia" : 9
    },

    "anao" : {
        "Nome" : "Anao",
        "Habilidade" : 8,
        "Energia" : 6
    },

    "cao1" : {
    "Nome" : "Primeiro Cão de Guarda",
    "Habilidade" : 7,
    "Energia" : 7
    },

    "cao2" : {
        "Nome" : "Segundo Cão de Guarda",
        "Habilidade" : 7,
        "Energia" : 8
    },

    "guardiao1" : {
    "Nome" : "Primeiro Guardião Voador",
    "Habilidade" : 7,
    "Energia" : 8
    },

    "guardiao2" : {
        "Nome" : "Segundo Guardião Voador",
        "Habilidade" : 8,
        "Energia" : 8
    },

    "besta" : {
        "Nome" : "Besta Sangrenta",
        "Habilidade" : 12,
        "Energia" : 10
    },

    "diabo_poco" : {
        "Nome" : "Diabo do Poço",
        "Habilidade" : 12,
        "Energia" : 15
    },

    "imitador" : {
        "Nome" : "Imitador",
        "Habilidade" : 9,
        "Energia" : 8
    },

    "verme_rocha" : {
        "Nome" : "Verme da Rocha",
        "Habilidade" : 7,
        "Energia" : 11
    },

    "throm" : {
        "Nome" : "Throm",
        "Habilidade" : 10,
        "Energia" : 12
    },

    "ninja" : {
        "Nome" : "Ninja",
        "Habilidade" : 11,
        "Energia" : 9
    },

    "demonio_espelho" : {
        "Nome" : "Demônio do Espelho",
        "Habilidade" : 10,
        "Energia" : 10
    },

    "guerreiro_esqueleto" : {
        "Nome" : "Guerreiro-Esqueleto",
        "Habilidade" : 8,
        "Energia" : 6
    },

    "troll_caverna" : {
        "Nome" : "Troll da Caverna",
        "Habilidade" : 10,
        "Energia" : 11
    },

    "homem_caverna" : {
        "Nome" : "Homem da Caverna",
        "Habilidade" : 7,
        "Energia" : 7
    }
}

#Itens
pecas_de_ouro = 0
moringa = 0
corda = 0

#Apresentação
print("Bem-vindo ao Calabouço da Morte")

#Mostrando a ficha
print("=" * 50)
print("SUA FICHA\n")

#Recuperando valores para a ficha com a função
habilidade, energia, sorte = ficha.fichaValores()

ficha = {
        "Habilidade" : habilidade,
        "Energia" : energia,
        "Sorte" : sorte,
        "Provisoes" : 10
        }

print(f"Habilidade: {ficha['Habilidade']}")
print(f"Energia: {ficha['Energia']}")
print(f"Sorte: {ficha['Sorte']}")
print(f"Provisões: {ficha['Provisoes']}")
print("=" * 50)

#Começando a condição de looping
while energia > 0:
    print(textos.T1())
    resposta = input().lower()
    if resposta == "sim":
        #ganha duas peças de ouro
        pecas_de_ouro += 2
        print(textos.T66())
        resposta = input().lower()
        
        #Indo para o oeste
        if resposta == "sim":
            print(textos.T293())
            resposta = input().lower()
            #Continuando no oeste
            if resposta == "sim":
                print(textos.T137())
                resposta = input().lower()
                #Tocando o sino
                if resposta == "sim":
                    print(textos.T220())
                    escolha = int(input())
                    match escolha:
                        #gritar = morte
                        case 1:
                            #Goblin te mata
                            print(textos.T61())
                            energia = 0
                        #Abafar o sino
                        case 2:
                            #Abafa o sino e segue a oeste
                            print(textos.T346())
                            #Vai em direção ao norte tumultuado
                            print(textos.T362())
                            #encontra dois Hobgoblins
                            print(textos.T264())
                            escolha = int(input())
                            match escolha:
                                #conversar com eles
                                case 1:
                                    #batalha com os dois goblins
                                    print(textos.T130())
                                    #Matando o primeiro HobGoblin
                                    print("Briga com o HobGoblin1...\n")
                                    while inimigos["hobgoblin1"]["Energia"] > 0:
                                        ataqueInimigo = inimigos["hobgoblin1"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                                        meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)
                                        print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                                        input("Jogue os dados...")
                                        print(f"O seu ataque foi de: {meuAtaque}\n")
                                        #causando dano
                                        if meuAtaque > ataqueInimigo:
                                            print("Quer testar sua sorte para causar mais dano?")
                                            testarSorte = input().lower()
                                            if testarSorte == 'não':
                                                inimigos["hobgoblin1"]["Energia"] -= 2
                                                print("\nA energia atual do inimigo é:", inimigos["hobgoblin1"]["Energia"])
                                            elif testarSorte == 'sim':
                                                input("Jogue os dados para testar sua sorte...\n")
                                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                if teste_da_sorte <= sorte:
                                                    print("Você teve sorte! Causou o dobro de dano")
                                                    inimigos["hobgoblin1"]["Energia"] -= 4
                                                    sorte -= 1
                                                    print("A energia atual do inimigo é:", inimigos["hobgoblin1"]["Energia"])
                                                    print(f"Sua sorte agora é {sorte}")
                                                else:
                                                    print("Você não teve sorte, causou menos dano!")
                                                    inimigos["hobgoblin1"]["Energia"] -= 1
                                                    sorte -= 1
                                                    print("A energia atual do inimigo é:", inimigos["hobgoblin1"]["Energia"])
                                                    print(f"Sua sorte agora é {sorte}")
                                        #tomando dano
                                        elif meuAtaque < ataqueInimigo:
                                            print("Quer testar sua sorte para receber menos dano?")
                                            testarSorte = input().lower()
                                            if testarSorte == 'não':
                                                energia -= 2
                                                print(f"\nSua energia atual é {energia}")
                                            elif testarSorte == 'sim':
                                                input("Jogue os dados para testar sua sorte...\n")
                                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                if teste_da_sorte <= sorte:
                                                    print("Você teve sorte! Recebeu menos dano!")
                                                    energia -= 1
                                                    sorte -= 1
                                                    print(f"Sua energia atual é {energia}")
                                                    print(f"Sua sorte agora é {sorte}")
                                                else:
                                                    print("Você não teve sorte, recebeu mais dano!")
                                                    energia -= 3
                                                    sorte -= 1
                                                    print(f"Sua energia atual é {energia}")
                                                    print(f"Sua sorte agora é {sorte}")
                                    #Matando o segundo HobGoblin
                                    print("Briga com o HobGoblin2...\n")
                                    while inimigos["hobgoblin2"]["Energia"] > 0:
                                        ataqueInimigo = inimigos["hobgoblin2"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                                        meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)
                                        print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                                        input("Jogue os dados...")
                                        print(f"O seu ataque foi de: {meuAtaque}\n")
                                        #causando dano
                                        if meuAtaque > ataqueInimigo:
                                            print("Quer testar sua sorte para causar mais dano?")
                                            testarSorte = input().lower()
                                            if testarSorte == 'não':
                                                inimigos["hobgoblin2"]["Energia"] -= 2
                                                print("\nA energia atual do inimigo é:", inimigos["hobgoblin2"]["Energia"])
                                            elif testarSorte == 'sim':
                                                input("Jogue os dados para testar sua sorte...\n")
                                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                if teste_da_sorte <= sorte:
                                                    print("Você teve sorte! Causou o dobro de dano")
                                                    inimigos["hobgoblin2"]["Energia"] -= 4
                                                    sorte -= 1
                                                    print("A energia atual do inimigo é:", inimigos["hobgoblin2"]["Energia"])
                                                    print(f"Sua sorte agora é {sorte}")
                                                else:
                                                    print("Você não teve sorte, causou menos dano!")
                                                    inimigos["hobgoblin2"]["Energia"] -= 1
                                                    sorte -= 1
                                                    print("A energia atual do inimigo é:", inimigos["hobgoblin2 "]["Energia"])
                                                    print(f"Sua sorte agora é {sorte}")
                                        #tomando dano
                                        elif meuAtaque < ataqueInimigo:
                                            print("Quer testar sua sorte para receber menos dano?")
                                            testarSorte = input().lower()
                                            if testarSorte == 'não':
                                                energia -= 2
                                                print(f"\nSua energia atual é {energia}")
                                            elif testarSorte == 'sim':
                                                input("Jogue os dados para testar sua sorte...\n")
                                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                if teste_da_sorte <= sorte:
                                                    print("Você teve sorte! Recebeu menos dano!")
                                                    energia -= 1
                                                    sorte -= 1
                                                    print(f"Sua energia atual é {energia}")
                                                    print(f"Sua sorte agora é {sorte}")
                                                else:
                                                    print("Você não teve sorte, recebeu mais dano!")
                                                    energia -= 3
                                                    sorte -= 1
                                                    print(f"Sua energia atual é {energia}")
                                                    print(f"Sua sorte agora é {sorte}")
                                    print("Parabéns você sobreviveu!\n")
                                    print(textos.T9())
                                    resposta = input().lower()
                                    #Tomar o líquido?
                                    if resposta == 'sim':
                                        print(textos.T158())
                                        habilidade -= 1
                                        energia -= 4
                                        print(textos.T275())
                                    elif resposta == 'não':
                                        print(textos.T375())
                                        moringa +=1
                                        print(textos.T110())
                                        escolha = int(input())
                                        #Postes
                                        match escolha:
                                            #Passar ao lado dos postes
                                            case 1:
                                                print(textos.T58())
                                                input("Jogue dois dados...")
                                                teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                                                if teste_da_habilidade <= habilidade:
                                                    #Segue ao leste
                                                    print(textos.T80())
                                                    #Fim do tunel, segue ao norte
                                                    print(textos.T313())
                                                    print(textos.T32())
                                                    print(textos.T37())
                                                    resposta = input().lower()
                                                    if resposta == 'sim':
                                                        print(textos.T351())
                                                        #possui corda
                                                        if corda != 0:
                                                            print(textos.T396())
                                                        #Não possui corda
                                                        elif corda == 0:
                                                            print(textos.T186())
                                                    elif resposta == 'não':
                                                        print(textos.T239())
                                                else:
                                                    #Esbarra no poste = chuva de farpas
                                                    print(textos.T246())
                                                    sorte -= 2
                                                    farpas = random.randint(1,6) + random.randint(1,6)
                                                    energia -= farpas
                                                    print("Você Sobreviveu às farpas!")
                                                    #Fim do tunel, segue ao norte
                                                    print(textos.T313())
                                                    print(textos.T32())
                                                    print(textos.T37())
                                                    resposta = input().lower()
                                                    #pegar as joias?
                                                    if resposta == 'sim':
                                                        print(textos.T351())
                                                        #possui corda
                                                        if corda != 0:
                                                            print(textos.T396())
                                                        #Não possui corda
                                                        elif corda == 0:
                                                            print(textos.T186())
                                                    elif resposta == 'não':
                                                        print(textos.T239())
                                            #Passar por cima dos postes = chuva de farpas
                                            case 2:
                                                print(textos.T223())
                                                sorte -= 2
                                                farpas = random.randint(1,6) + random.randint(1,6)
                                                energia -= farpas
                                                print("Você Sobreviveu às farpas!")
                                                #Fim do tunel, segue ao norte
                                                print(textos.T313())
                                                print(textos.T32())
                                                print(textos.T37())
                                                resposta = input().lower()
                                                #pegar as joias?
                                                if resposta == 'sim':
                                                    print(textos.T351())
                                                    #possui corda
                                                    if corda != 0:
                                                        print(textos.T396())
                                                    #Não possui corda
                                                    elif corda == 0:
                                                        print(textos.T186())
                                                elif resposta == 'não':
                                                    print(textos.T239())
                                #Atacá-los
                                case 2:
                                    #Mata um e luta com o outro goblin
                                    print(textos.T51())
                                    #Matando o HobGoblin restante
                                    print("Briga com o HobGoblin2...\n")
                                    while inimigos["hobgoblin2"]["Energia"] > 0:
                                        ataqueInimigo = inimigos["hobgoblin2"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                                        meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)
                                        print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                                        input("Jogue os dados...")
                                        print(f"O seu ataque foi de: {meuAtaque}\n")
                                        #causando dano
                                        if meuAtaque > ataqueInimigo:
                                            print("Quer testar sua sorte para causar mais dano?")
                                            testarSorte = input().lower()
                                            if testarSorte == 'não':
                                                inimigos["hobgoblin2"]["Energia"] -= 2
                                                print("\nA energia atual do inimigo é:", inimigos["hobgoblin2"]["Energia"])
                                            elif testarSorte == 'sim':
                                                input("Jogue os dados para testar sua sorte...\n")
                                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                if teste_da_sorte <= sorte:
                                                    print("Você teve sorte! Causou o dobro de dano")
                                                    inimigos["hobgoblin2"]["Energia"] -= 4
                                                    sorte -= 1
                                                    print("A energia atual do inimigo é:", inimigos["hobgoblin2"]["Energia"])
                                                    print(f"Sua sorte agora é {sorte}")
                                                else:
                                                    print("Você não teve sorte, causou menos dano!")
                                                    inimigos["hobgoblin2"]["Energia"] -= 1
                                                    sorte -= 1
                                                    print("A energia atual do inimigo é:", inimigos["hobgoblin2 "]["Energia"])
                                                    print(f"Sua sorte agora é {sorte}")
                                        #tomando dano
                                        elif meuAtaque < ataqueInimigo:
                                            print("Quer testar sua sorte para receber menos dano?")
                                            testarSorte = input().lower()
                                            if testarSorte == 'não':
                                                energia -= 2
                                                print(f"\nSua energia atual é {energia}")
                                            elif testarSorte == 'sim':
                                                input("Jogue os dados para testar sua sorte...\n")
                                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                if teste_da_sorte <= sorte:
                                                    print("Você teve sorte! Recebeu menos dano!")
                                                    energia -= 1
                                                    sorte -= 1
                                                    print(f"Sua energia atual é {energia}")
                                                    print(f"Sua sorte agora é {sorte}")
                                                else:
                                                    print("Você não teve sorte, recebeu mais dano!")
                                                    energia -= 3
                                                    sorte -= 1
                                                    print(f"Sua energia atual é {energia}")
                                                    print(f"Sua sorte agora é {sorte}")
                                    print("Parabéns você sobreviveu!\n")
                                    print(textos.T9())
                                    resposta = input().lower()
                                    #Tomar o líquido?
                                    if resposta == 'sim':
                                        print(textos.T158())
                                        habilidade -= 1
                                        energia -= 4
                                        print(textos.T275())
                                    elif resposta == 'não':
                                        print(textos.T375())
                                        moringa +=1
                                        print(textos.T110())
                                        escolha = int(input())
                                        #Postes
                                        match escolha:
                                            #Passar ao lado dos postes
                                            case 1:
                                                print(textos.T58())
                                                input("Jogue dois dados...")
                                                teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                                                if teste_da_habilidade <= habilidade:
                                                    #Segue ao leste
                                                    print(textos.T80())
                                                    #Fim do tunel, segue ao norte
                                                    print(textos.T313())
                                                    print(textos.T32())
                                                    print(textos.T37())
                                                    resposta = input().lower()
                                                    #pegar as joias?
                                                    if resposta == 'sim':
                                                        print(textos.T351())
                                                        #possui corda
                                                        if corda != 0:
                                                            print(textos.T396())
                                                        #Não possui corda
                                                        elif corda == 0:
                                                            print(textos.T186())
                                                    elif resposta == 'não':
                                                        print(textos.T239())
                                                else:
                                                    #Esbarra no poste = chuva de farpas
                                                    print(textos.T246())
                                                    sorte -= 2
                                                    farpas = random.randint(1,6) + random.randint(1,6)
                                                    energia -= farpas
                                                    print("Você Sobreviveu às farpas!")
                                                    #Fim do tunel, segue ao norte
                                                    print(textos.T313())
                                                    print(textos.T32())
                                                    print(textos.T37())
                                                    resposta = input().lower()
                                                    #pegar as joias?
                                                    if resposta == 'sim':
                                                        print(textos.T351())
                                                        #possui corda
                                                        if corda != 0:
                                                            print(textos.T396())
                                                        #Não possui corda
                                                        elif corda == 0:
                                                            print(textos.T186())
                                                    elif resposta == 'não':
                                                        print(textos.T239())
                                            #Passar por cima dos postes = chuva de farpas
                                            case 2:
                                                print(textos.T223())
                                                sorte -= 2
                                                farpas = random.randint(1,6) + random.randint(1,6)
                                                energia -= farpas
                                                print("Você Sobreviveu às farpas!")
                                                #Fim do tunel, segue ao norte
                                                print(textos.T313())
                                                print(textos.T32())
                                                print(textos.T37())
                                                resposta = input().lower()
                                                #pegar as joias?
                                                if resposta == 'sim':
                                                    print(textos.T351())
                                                    #possui corda
                                                    if corda != 0:
                                                        print(textos.T396())
                                                    #Não possui corda
                                                    elif corda == 0:
                                                        print(textos.T186())
                                                elif resposta == 'não':
                                                    print(textos.T239())
                                #Tentar passar despercebido
                                case 3 :
                                    #corre dos goblins indo ao norte
                                    print(textos.T355())
                elif resposta == "não":
                    #Vai em direção ao norte tumultuado
                    print(textos.T362())
                    #dois Hobgoblins e uma bolsa de couro
                    print(textos.T264())
                    escolha = int(input())
                    match escolha:
                        #conversar com eles
                        case 1:
                            #batalha com os dois goblins
                            print(textos.T130())
                            #Matando o primeiro HobGoblin
                            print("Briga com o HobGoblin1...\n")
                            while inimigos["hobgoblin1"]["Energia"] > 0:
                                ataqueInimigo = inimigos["hobgoblin1"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                                meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)
                                print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                                input("Jogue os dados...")
                                print(f"O seu ataque foi de: {meuAtaque}\n")
                                #causando dano
                                if meuAtaque > ataqueInimigo:
                                    print("Quer testar sua sorte para causar mais dano?")
                                    testarSorte = input().lower()
                                    if testarSorte == 'não':
                                        inimigos["hobgoblin1"]["Energia"] -= 2
                                        print("\nA energia atual do inimigo é:", inimigos["hobgoblin1"]["Energia"])
                                    elif testarSorte == 'sim':
                                        input("Jogue os dados para testar sua sorte...\n")
                                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                        if teste_da_sorte <= sorte:
                                            print("Você teve sorte! Causou o dobro de dano")
                                            inimigos["hobgoblin1"]["Energia"] -= 4
                                            sorte -= 1
                                            print("A energia atual do inimigo é:", inimigos["hobgoblin1"]["Energia"])
                                            print(f"Sua sorte agora é {sorte}")
                                        else:
                                            print("Você não teve sorte, causou menos dano!")
                                            inimigos["hobgoblin1"]["Energia"] -= 1
                                            sorte -= 1
                                            print("A energia atual do inimigo é:", inimigos["hobgoblin1"]["Energia"])
                                            print(f"Sua sorte agora é {sorte}")
                                #tomando dano
                                elif meuAtaque < ataqueInimigo:
                                    print("Quer testar sua sorte para receber menos dano?")
                                    testarSorte = input().lower()
                                    if testarSorte == 'não':
                                        energia -= 2
                                        print(f"\nSua energia atual é {energia}")
                                    elif testarSorte == 'sim':
                                        input("Jogue os dados para testar sua sorte...\n")
                                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                        if teste_da_sorte <= sorte:
                                            print("Você teve sorte! Recebeu menos dano!")
                                            energia -= 1
                                            sorte -= 1
                                            print(f"Sua energia atual é {energia}")
                                            print(f"Sua sorte agora é {sorte}")
                                        else:
                                            print("Você não teve sorte, recebeu mais dano!")
                                            energia -= 3
                                            sorte -= 1
                                            print(f"Sua energia atual é {energia}")
                                            print(f"Sua sorte agora é {sorte}")
                            #Matando o segundo HobGoblin
                            print("Briga com o HobGoblin2...\n")
                            while inimigos["hobgoblin2"]["Energia"] > 0:
                                ataqueInimigo = inimigos["hobgoblin2"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                                meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)
                                print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                                input("Jogue os dados...")
                                print(f"O seu ataque foi de: {meuAtaque}\n")
                                #causando dano
                                if meuAtaque > ataqueInimigo:
                                    print("Quer testar sua sorte para causar mais dano?")
                                    testarSorte = input().lower()
                                    if testarSorte == 'não':
                                        inimigos["hobgoblin2"]["Energia"] -= 2
                                        print("\nA energia atual do inimigo é:", inimigos["hobgoblin2"]["Energia"])
                                    elif testarSorte == 'sim':
                                        input("Jogue os dados para testar sua sorte...\n")
                                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                        if teste_da_sorte <= sorte:
                                            print("Você teve sorte! Causou o dobro de dano")
                                            inimigos["hobgoblin2"]["Energia"] -= 4
                                            sorte -= 1
                                            print("A energia atual do inimigo é:", inimigos["hobgoblin2"]["Energia"])
                                            print(f"Sua sorte agora é {sorte}")
                                        else:
                                            print("Você não teve sorte, causou menos dano!")
                                            inimigos["hobgoblin2"]["Energia"] -= 1
                                            sorte -= 1
                                            print("A energia atual do inimigo é:", inimigos["hobgoblin2 "]["Energia"])
                                            print(f"Sua sorte agora é {sorte}")
                                #tomando dano
                                elif meuAtaque < ataqueInimigo:
                                    print("Quer testar sua sorte para receber menos dano?")
                                    testarSorte = input().lower()
                                    if testarSorte == 'não':
                                        energia -= 2
                                        print(f"\nSua energia atual é {energia}")
                                    elif testarSorte == 'sim':
                                        input("Jogue os dados para testar sua sorte...\n")
                                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                        if teste_da_sorte <= sorte:
                                            print("Você teve sorte! Recebeu menos dano!")
                                            energia -= 1
                                            sorte -= 1
                                            print(f"Sua energia atual é {energia}")
                                            print(f"Sua sorte agora é {sorte}")
                                        else:
                                            print("Você não teve sorte, recebeu mais dano!")
                                            energia -= 3
                                            sorte -= 1
                                            print(f"Sua energia atual é {energia}")
                                            print(f"Sua sorte agora é {sorte}")
                            print("Parabéns você sobreviveu!\n")
                            print(textos.T9())
                            resposta = input().lower()
                            #tomar o líquido?
                            if resposta == 'sim':
                                print(textos.T158())
                                habilidade -= 1
                                energia -= 4
                                print(textos.T275())
                            elif resposta == 'não':
                                print(textos.T375())
                                moringa +=1
                                print(textos.T110())
                                escolha = int(input())
                                #Postes
                                match escolha:
                                    #Passar ao lado dos postes
                                    case 1:
                                        print(textos.T58())
                                        input("Jogue dois dados...")
                                        teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                                        if teste_da_habilidade <= habilidade:
                                            #Segue ao leste
                                            print(textos.T80())
                                            #Fim do tunel, segue ao norte
                                            print(textos.T313())
                                            print(textos.T32())
                                            print(textos.T37())
                                            resposta = input().lower()
                                            #pegar as joias?
                                            if resposta == 'sim':
                                                print(textos.T351())
                                                #possui corda
                                                if corda != 0:
                                                    print(textos.T396())
                                                #Não possui corda
                                                elif corda == 0:
                                                    print(textos.T186())
                                            elif resposta == 'não':
                                                print(textos.T239())
                                        else:
                                            #Esbarra no poste = chuva de farpas
                                            print(textos.T246())
                                            sorte -= 2
                                            farpas = random.randint(1,6) + random.randint(1,6)
                                            energia -= farpas
                                            print("Você Sobreviveu às farpas!")
                                            #Fim do tunel, segue ao norte
                                            print(textos.T313())
                                            print(textos.T32())
                                            print(textos.T37())
                                            resposta = input().lower()
                                            #pegar as joias?
                                            if resposta == 'sim':
                                                print(textos.T351())
                                                #possui corda
                                                if corda != 0:
                                                    print(textos.T396())
                                                #Não possui corda
                                                elif corda == 0:
                                                    print(textos.T186())
                                            elif resposta == 'não':
                                                print(textos.T239())
                                    #Passar por cima dos postes = chuva de farpas
                                    case 2:
                                        print(textos.T223())
                                        sorte -= 2
                                        farpas = random.randint(1,6) + random.randint(1,6)
                                        energia -= farpas
                                        print("Você Sobreviveu às farpas!")
                                        #Fim do tunel, segue ao norte
                                        print(textos.T313())
                                        print(textos.T32())
                                        print(textos.T37())
                                        resposta = input().lower()
                                        #pegar as joias?
                                        if resposta == 'sim':
                                            print(textos.T351())
                                            #possui corda
                                            if corda != 0:
                                                print(textos.T396())
                                            #Não possui corda
                                            elif corda == 0:
                                                print(textos.T186())
                                        elif resposta == 'não':
                                            print(textos.T239())
                        #Atacá-los
                        case 2:
                            #batalha com apenas um goblin
                            print(textos.T51())
                            #Mata um e luta com o outro goblin
                            print(textos.T51())
                            #Matando o HobGoblin restante
                            print("Briga com o HobGoblin2...\n")
                            while inimigos["hobgoblin2"]["Energia"] > 0:
                                ataqueInimigo = inimigos["hobgoblin2"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                                meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)
                                print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                                input("Jogue os dados...")
                                print(f"O seu ataque foi de: {meuAtaque}\n")
                                #causando dano
                                if meuAtaque > ataqueInimigo:
                                    print("Quer testar sua sorte para causar mais dano?")
                                    testarSorte = input().lower()
                                    if testarSorte == 'não':
                                        inimigos["hobgoblin2"]["Energia"] -= 2
                                        print("\nA energia atual do inimigo é:", inimigos["hobgoblin2"]["Energia"])
                                    elif testarSorte == 'sim':
                                        input("Jogue os dados para testar sua sorte...\n")
                                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                        if teste_da_sorte <= sorte:
                                            print("Você teve sorte! Causou o dobro de dano")
                                            inimigos["hobgoblin2"]["Energia"] -= 4
                                            sorte -= 1
                                            print("A energia atual do inimigo é:", inimigos["hobgoblin2"]["Energia"])
                                            print(f"Sua sorte agora é {sorte}")
                                        else:
                                            print("Você não teve sorte, causou menos dano!")
                                            inimigos["hobgoblin2"]["Energia"] -= 1
                                            sorte -= 1
                                            print("A energia atual do inimigo é:", inimigos["hobgoblin2 "]["Energia"])
                                            print(f"Sua sorte agora é {sorte}")
                                #tomando dano
                                elif meuAtaque < ataqueInimigo:
                                    print("Quer testar sua sorte para receber menos dano?")
                                    testarSorte = input().lower()
                                    if testarSorte == 'não':
                                        energia -= 2
                                        print(f"\nSua energia atual é {energia}")
                                    elif testarSorte == 'sim':
                                        input("Jogue os dados para testar sua sorte...\n")
                                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                        if teste_da_sorte <= sorte:
                                            print("Você teve sorte! Recebeu menos dano!")
                                            energia -= 1
                                            sorte -= 1
                                            print(f"Sua energia atual é {energia}")
                                            print(f"Sua sorte agora é {sorte}")
                                        else:
                                            print("Você não teve sorte, recebeu mais dano!")
                                            energia -= 3
                                            sorte -= 1
                                            print(f"Sua energia atual é {energia}")
                                            print(f"Sua sorte agora é {sorte}")
                            print("Parabéns você sobreviveu!\n")
                            print(textos.T9())
                            resposta = input().lower()
                            #tomar o líquido?
                            if resposta == 'sim':
                                print(textos.T158())
                                habilidade -= 1
                                energia -= 4
                                print(textos.T275())
                            elif resposta == 'não':
                                print(textos.T375())
                                moringa +=1
                                print(textos.T110())
                                escolha = int(input())
                                #Postes
                                match escolha:
                                    #Passar ao lado dos postes
                                    case 1:
                                        print(textos.T58())
                                        input("Jogue dois dados...")
                                        teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                                        if teste_da_habilidade <= habilidade:
                                            #Segue ao leste
                                            print(textos.T80())
                                            #Fim do tunel, segue ao norte
                                            print(textos.T313())
                                            print(textos.T32())
                                            print(textos.T37())
                                            resposta = input().lower()
                                            #pegar as joias?
                                            if resposta == 'sim':
                                                print(textos.T351())
                                                #possui corda
                                                if corda != 0:
                                                    print(textos.T396())
                                                #Não possui corda
                                                elif corda == 0:
                                                    print(textos.T186())
                                            elif resposta == 'não':
                                                print(textos.T239())
                                        else:
                                            #Esbarra no poste = chuva de farpas
                                            print(textos.T246())
                                            sorte -= 2
                                            farpas = random.randint(1,6) + random.randint(1,6)
                                            energia -= farpas
                                            print("Você Sobreviveu às farpas!")
                                            #Fim do tunel, segue ao norte
                                            print(textos.T313())
                                            print(textos.T32())
                                            print(textos.T37())
                                            resposta = input().lower()
                                            #pegar as joias?
                                            if resposta == 'sim':
                                                print(textos.T351())
                                                #possui corda
                                                if corda != 0:
                                                    print(textos.T396())
                                                #Não possui corda
                                                elif corda == 0:
                                                    print(textos.T186())
                                            elif resposta == 'não':
                                                print(textos.T239())
                                    #Passar por cima dos postes = chuva de farpas
                                    case 2:
                                        print(textos.T223())
                                        sorte -= 2
                                        farpas = random.randint(1,6) + random.randint(1,6)
                                        energia -= farpas
                                        print("Você Sobreviveu às farpas!")
                                        #Fim do tunel, segue ao norte
                                        print(textos.T313())
                                        print(textos.T32())
                                        print(textos.T37())
                                        #pegar as joias?
                                        resposta = input().lower()
                                        if resposta == 'sim':
                                            print(textos.T351())
                                            #possui corda
                                            if corda != 0:
                                                print(textos.T396())
                                            #Não possui corda
                                            elif corda == 0:
                                                print(textos.T186())
                                        elif resposta == 'não':
                                            print(textos.T239())
                        #Tentar passar despercebido
                        case 3 :
                            #corre dos goblins indo ao norte
                            print(textos.T355())
            #Mudando para o norte
            elif resposta == "não":
                print(textos.T387())
        #Indo para o Leste
        elif resposta == "não":
            print(textos.T119())

    elif resposta == "não":
        print(textos.T66())
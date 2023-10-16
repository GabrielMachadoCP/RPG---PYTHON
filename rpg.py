# Ana Zerlin        RM 98065
# Bianca Dancs      RM 551645
# Gabriel Pimentel  RM 99880
# Hellen Assis      RM 98284

#Imports
import random

import ficha
import textos
import inimigos

#Itens
venceu = False
pecas_de_ouro = 0
moringa = 0
corda = 0
punhal = 0
rubi = 0
esmeralda = 0
escudo = 1

#Apresentação
print("=" * 50)
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

#Variáveis para inicialização
sorteFixa = sorte
habilidadeFixa = habilidade
energiaFixa = energia

cont = 0

#Introdução da história
print("=" * 50)
continuar = input("A história começa aqui...\n")
print(textos.intro())
print("=" * 50)

#Começando a condição de looping
while energia > 0 or venceu == False :
    #Primeira opção
    print(textos.T1())
    resposta = int(input("Escolha: "))
    #Abrindo a caixa
    if resposta == 1 :
        print(textos.T270())
        pecas_de_ouro += 2
        input("\nGuarde suas peças de ouro..💰")

    #Continuando
    print(textos.T66())
    resposta = int(input("Escolha: "))
        
    #Indo para o leste
    if resposta == 2 :
        print(textos.T119())
        resposta = int(input("Escolha: "))

        if resposta == 1 :
            print(textos.T56())

        print(textos.T13())

    print(textos.T293())
    resposta = int(input("Escolha: "))

    #Seguindo no oeste
    if resposta == 1 :
        print(textos.T137())
        resposta = int(input("Escolha: "))

        #Tocando o sino
        if resposta == 1 :
            print(textos.T220())
            escolha = int(input("Escolha: "))

            match escolha :
                #Gritar = morte
                case 1 :
                    #Goblin te mata
                    print(textos.T61())
                    energia = 0

                #Abafar o sino
                case 2 :
                    #Abafa o sino e segue a oeste
                    print(textos.T346())

    #Continua a jornada para oeste
    print(textos.T362())

    #Encontra dois Hobgoblins
    print(textos.T264())
    escolha = int(input("Escolha: "))

    match escolha :
        #Tenta conversar com eles
        case 1 :
            #Batalha
            print(textos.T130())

            #Matando o primeiro Hobgoblin
            print("Briga com o Hobgoblin Nº1...\n")

            while inimigos.inimigos["hobgoblin1"]["Energia"] > 0 :
                ataqueInimigo = inimigos.inimigos["hobgoblin1"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)

                print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                input("Jogue os dados...🎲")
                print(f"O seu ataque foi de: {meuAtaque}\n")

                #Causando dano
                if meuAtaque > ataqueInimigo :
                    print("Quer testar sua sorte para causar mais dano?")
                    testarSorte = input().lower()

                    if testarSorte == "sim" :
                        if sorte > 0 :
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("Você teve sorte! Causou o dobro de dano")
                                inimigos.inimigos["hobgoblin1"]["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", inimigos.inimigos["hobgoblin1"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Você não teve sorte, causou menos dano!")
                                inimigos.inimigos["hobgoblin1"]["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", inimigos.inimigos["hobgoblin1"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            inimigos.inimigos["hobgoblin1"]["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["hobgoblin1"]["Energia"])

                    else :
                        inimigos.inimigos["hobgoblin1"]["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["hobgoblin1"]["Energia"])

                #Tomando dano
                else :
                    print("Quer testar sua sorte para receber menos dano?")
                    testarSorte = input().lower()

                    if testarSorte == "sim" :
                        if sorte > 0 :
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("Você teve sorte! Recebeu menos dano!")
                                energia -= 1
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Você não teve sorte, recebeu mais dano!")
                                energia -= 3
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            energia -= 2
                            print(f"\nSua energia atual é {energia}")

                    else :
                        energia -= 2
                        print(f"\nSua energia atual é {energia}")

            #Matando o segundo HobGoblin
            print("Briga com o Hobgoblin Nº2...\n")

            while inimigos.inimigos["hobgoblin2"]["Energia"] > 0 :
                ataqueInimigo = inimigos.inimigos["hobgoblin2"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)

                print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                input("Jogue os dados...🎲")
                print(f"O seu ataque foi de: {meuAtaque}\n")

                #Causando dano
                if meuAtaque > ataqueInimigo :
                    print("Quer testar sua sorte para causar mais dano?")
                    testarSorte = input().lower()

                    if testarSorte == "sim" :
                        if sorte > 0 :
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("Você teve sorte! Causou o dobro de dano")
                                inimigos.inimigos["hobgoblin2"]["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", inimigos.inimigos["hobgoblin2"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Você não teve sorte, causou menos dano!")
                                inimigos.inimigos["hobgoblin2"]["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", inimigos.inimigos["hobgoblin2"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            inimigos.inimigos["hobgoblin2"]["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["hobgoblin2"]["Energia"])

                    else :
                        inimigos.inimigos["hobgoblin2"]["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["hobgoblin2"]["Energia"])

                #Tomando dano
                else :
                    print("Quer testar sua sorte para receber menos dano?")
                    testarSorte = input().lower()

                    if testarSorte == "sim" :
                        if sorte > 0 :
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("Você teve sorte! Recebeu menos dano!")
                                energia -= 1
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Você não teve sorte, recebeu mais dano!")
                                energia -= 3
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            energia -= 2
                            print(f"\nSua energia atual é {energia}")

                    else :
                        energia -= 2
                        print(f"\nSua energia atual é {energia}")

            print("Parabéns você sobreviveu!\n")
            print(textos.T9())
            escolha = int(input("Escolha: "))

            #Toma o líquido
            if resposta == 1 :
                print(textos.T158())
                habilidade -= 1
                energia -= 4
                print(textos.T275())

                #Teste a sua sorte
                sorte -= 1
                input("Jogue os dados para testar sua sorte...\n")
                teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                if teste_da_sorte >= sorte :
                    print(textos.T309())
                    energia -= 3

                    if energia > 0 :
                        input("Teste sua sorte")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                        if teste_da_sorte >= sorte :
                            print(textos.T193())
                            energia = 0

                        else :
                            print(textos.T231())

            print(textos.T110())
            escolha = int(input("Escolha: "))

            #Postes
            match escolha :
                #Passar ao lado dos postes
                case 1 :
                    print(textos.T58())
                    input("Jogue dois dados...")
                    teste_da_habilidade = random.randint(1,6) + random.randint(1,6)

                    if teste_da_habilidade <= habilidade :
                        #Segue ao leste
                        print(textos.T80())

                #Subindo os postes
                case 2 :
                    print(textos.T223)
                    sorte -= 2
                    input("Jogue dois dados...")
                    farpas = random.randint(1,6) + random.randint(1,6)
                    energia -= farpas

                    if energia > 0 :
                        print(textos.T223_2())


            #Fim do tunel, segue ao norte
            print(textos.T313())
            print(textos.T32())
            print(textos.T37())
            resposta = int(input("Escolha: "))

            #Sobe no ídolo
            if resposta == 1 :
                print(textos.T351())
                print(f"Inverntário: - Corda: {corda}")
                cordaPergunta = input("Sim ou não?")

                #Possui corda
                if corda != 0 :
                    print(textos.T396())
                    resposta = int(input("Escolha: "))

                    #Pegar a joia da direita = morte
                    if resposta == 2 :
                        print(textos.T34())
                        energia = 0

                    #Pega a joia da esquerda
                    elif resposta == 1 :
                        print(textos.T151())

                        #Matando o primeiro guardião
                        print("Briga com o Guardião Voador Nº1...\n")

                        while inimigos.inimigos["guardiao1"]["Energia"] > 0 :
                            ataqueInimigo = inimigos.inimigos["guardiao1"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                            meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6) - 2

                            print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                            input("Jogue os dados...🎲")
                            print(f"O seu ataque foi de: {meuAtaque}\n")

                            #Causando dano
                            if meuAtaque > ataqueInimigo :
                                print("Quer testar sua sorte para causar mais dano?")
                                testarSorte = input().lower()

                                if testarSorte == "sim" :
                                    if sorte > 0 :
                                        input("Jogue os dados para testar sua sorte...\n")
                                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                        if teste_da_sorte <= sorte :
                                            print("Você teve sorte! Causou o dobro de dano")
                                            inimigos.inimigos["guardiao1"]["Energia"] -= 4
                                            sorte -= 1
                                            print("A energia atual do inimigo é: ", inimigos.inimigos["guardiao1"]["Energia"])
                                            print(f"Sua sorte agora é {sorte}")

                                        else :
                                            print("Você não teve sorte, causou menos dano!")
                                            inimigos.inimigos["guardiao1"]["Energia"] -= 1
                                            sorte -= 1
                                            print("A energia atual do inimigo é:", inimigos.inimigos["guardiao1"]["Energia"])
                                            print(f"Sua sorte agora é {sorte}")
                                    
                                    else :
                                        print("Você infelizmente não tem mais sorte")
                                        inimigos.inimigos["guardiao1"]["Energia"] -= 2
                                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["guardiao1"]["Energia"])

                                else :
                                    inimigos.inimigos["guardiao1"]["Energia"] -= 2
                                    print("\nA energia atual do inimigo é: ", inimigos.inimigos["guardiao1"]["Energia"])

                            #Tomando dano
                            else :
                                print("Quer testar sua sorte para receber menos dano?")
                                testarSorte = input().lower()

                                if testarSorte == "sim" :
                                    if sorte > 0 :
                                        input("Jogue os dados para testar sua sorte...\n")
                                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                        if teste_da_sorte <= sorte :
                                            print("Você teve sorte! Recebeu menos dano!")
                                            energia -= 1
                                            sorte -= 1
                                            print(f"Sua energia atual é {energia}")
                                            print(f"Sua sorte agora é {sorte}")

                                        else :
                                            print("Você não teve sorte, recebeu mais dano!")
                                            energia -= 3
                                            sorte -= 1
                                            print(f"Sua energia atual é {energia}")
                                            print(f"Sua sorte agora é {sorte}")

                                    else :
                                        print("Você infelizmente não tem mais sorte")
                                        energia -= 2
                                        print(f"\nSua energia atual é {energia}")

                                else :
                                    energia -= 2
                                    print(f"\nSua energia atual é {energia}")

                        #Matando o segundo Guardião Voador
                        print("Briga com o Guardião Voador Nº2...\n")

                        while inimigos.inimigos["guardiao2"]["Energia"] > 0 :
                            ataqueInimigo = inimigos.inimigos["guardiao2"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                            meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6) - 2

                            print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                            input("Jogue os dados...🎲")
                            print(f"O seu ataque foi de: {meuAtaque}\n")

                            #Causando dano
                            if meuAtaque > ataqueInimigo :
                                print("Quer testar sua sorte para causar mais dano?")
                                testarSorte = input().lower()

                                if testarSorte == "sim" :
                                    if sorte > 0 :
                                        input("Jogue os dados para testar sua sorte...\n")
                                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                        if teste_da_sorte <= sorte :
                                            print("Você teve sorte! Causou o dobro de dano")
                                            inimigos.inimigos["guardiao2"]["Energia"] -= 4
                                            sorte -= 1
                                            print("A energia atual do inimigo é: ", inimigos.inimigos["guardiao2"]["Energia"])
                                            print(f"Sua sorte agora é {sorte}")

                                        else :
                                            print("Você não teve sorte, causou menos dano!")
                                            inimigos.inimigos["guardiao2"]["Energia"] -= 1
                                            sorte -= 1
                                            print("A energia atual do inimigo é:", inimigos.inimigos["guardiao2"]["Energia"])
                                            print(f"Sua sorte agora é {sorte}")
                                            
                                    else :
                                        print("Você infelizmente não tem mais sorte")
                                        inimigos.inimigos["guardiao2"]["Energia"] -= 2
                                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["guardiao2"]["Energia"])

                                else :
                                    inimigos.inimigos["guardiao2"]["Energia"] -= 2
                                    print("\nA energia atual do inimigo é: ", inimigos.inimigos["guardiao2"]["Energia"])

                            #Tomando dano
                            else :
                                print("Quer testar sua sorte para receber menos dano?")
                                testarSorte = input().lower()

                                if testarSorte == "sim" :
                                    if sorte > 0 :
                                        input("Jogue os dados para testar sua sorte...\n")
                                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                        if teste_da_sorte <= sorte :
                                            print("Você teve sorte! Recebeu menos dano!")
                                            energia -= 1
                                            sorte -= 1
                                            print(f"Sua energia atual é {energia}")
                                            print(f"Sua sorte agora é {sorte}")

                                        else :
                                            print("Você não teve sorte, recebeu mais dano!")
                                            energia -= 3
                                            sorte -= 1
                                            print(f"Sua energia atual é {energia}")
                                            print(f"Sua sorte agora é {sorte}")

                                    else :
                                        print("Você infelizmente não tem mais sorte")
                                        energia -= 2
                                        print(f"\nSua energia atual é {energia}")

                                else :
                                    energia -= 2
                                    print(f"\nSua energia atual é {energia}")

                        print("\nParabéns você sobreviveu! E agora tem uma esmeralda.")
                        print(textos.T240())
                        esmeralda += 1
                        resposta = int(input("Escolha: "))

                        if resposta == 1 :
                            print(textos.T34())
                            energia = 0

                        elif resposta == 2 :
                            print(textos.T89())
                            #Teste a sua sorte
                            sorte -= 1
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("Você teve sorte!")
                                print(textos.T54())
                                corda += 1
                                print(textos.T239()) #completar
                            else:
                                print("Você não teve sorte!")
                                print(textos.T261())
                                print(textos.T239()) #completar

                #Não possui corda
                elif corda == 0 :
                    print(textos.T186())
                    #Testando a sorte
                    input("Jogue os dados para testar sua sorte...\n")
                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                    sorte -= 1
                    
                    if teste_da_sorte >= sorte :
                        print("Você não teve sorte!")
                        print(textos.T358())
                        #Você cai e perde energia
                        energia -= 2
                    
                    else :
                        print("Você teve sorte!")
                        print(textos.T260())
                        resposta = int(input("Escolha: "))
                        
                        #Arrancando o olho direito
                        if resposta == 2 :
                            print(textos.T140())
                            energia = 0

                        else :
                            print(textos.T166())

                            #Matando o primeiro guardião
                            print("Briga com o Guardião Voador Nº1...\n")

                            while inimigos.inimigos["guardiao1"]["Energia"] > 0 :
                                ataqueInimigo = inimigos.inimigos["guardiao1"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                                meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6) - 3

                                print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                                input("Jogue os dados...🎲")
                                print(f"O seu ataque foi de: {meuAtaque}\n")

                                #Causando dano
                                if meuAtaque > ataqueInimigo :
                                    print("Quer testar sua sorte para causar mais dano?")
                                    testarSorte = input().lower()

                                    if testarSorte == "sim" :
                                        if sorte > 0 :
                                            input("Jogue os dados para testar sua sorte...\n")
                                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                            if teste_da_sorte <= sorte :
                                                print("Você teve sorte! Causou o dobro de dano")
                                                inimigos.inimigos["guardiao1"]["Energia"] -= 4
                                                sorte -= 1
                                                print("A energia atual do inimigo é: ", inimigos.inimigos["guardiao1"]["Energia"])
                                                print(f"Sua sorte agora é {sorte}")

                                            else :
                                                print("Você não teve sorte, causou menos dano!")
                                                inimigos.inimigos["guardiao1"]["Energia"] -= 1
                                                sorte -= 1
                                                print("A energia atual do inimigo é:", inimigos.inimigos["guardiao1"]["Energia"])
                                                print(f"Sua sorte agora é {sorte}")
                                        
                                        else :
                                            print("Você infelizmente não tem mais sorte")
                                            inimigos.inimigos["guardiao1"]["Energia"] -= 2
                                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["guardiao1"]["Energia"])

                                    else :
                                        inimigos.inimigos["guardiao1"]["Energia"] -= 2
                                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["guardiao1"]["Energia"])

                                #Tomando dano
                                else :
                                    print("Quer testar sua sorte para receber menos dano?")
                                    testarSorte = input().lower()

                                    if testarSorte == "sim" :
                                        if sorte > 0 :
                                            input("Jogue os dados para testar sua sorte...\n")
                                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                            if teste_da_sorte <= sorte :
                                                print("Você teve sorte! Recebeu menos dano!")
                                                energia -= 1
                                                sorte -= 1
                                                print(f"Sua energia atual é {energia}")
                                                print(f"Sua sorte agora é {sorte}")

                                            else :
                                                print("Você não teve sorte, recebeu mais dano!")
                                                energia -= 3
                                                sorte -= 1
                                                print(f"Sua energia atual é {energia}")
                                                print(f"Sua sorte agora é {sorte}")

                                        else :
                                            print("Você infelizmente não tem mais sorte")
                                            energia -= 2
                                            print(f"\nSua energia atual é {energia}")

                                    else :
                                        energia -= 2
                                        print(f"\nSua energia atual é {energia}")

                            #Matando o segundo Guardião Voador
                            print("Briga com o Guardião Voador Nº2...\n")

                            while inimigos.inimigos["guardiao2"]["Energia"] > 0 :
                                ataqueInimigo = inimigos.inimigos["guardiao2"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                                meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6) - 3

                                print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                                input("Jogue os dados...🎲")
                                print(f"O seu ataque foi de: {meuAtaque}\n")

                                #Causando dano
                                if meuAtaque > ataqueInimigo :
                                    print("Quer testar sua sorte para causar mais dano?")
                                    testarSorte = input().lower()

                                    if testarSorte == "sim" :
                                        if sorte > 0 :
                                            input("Jogue os dados para testar sua sorte...\n")
                                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                            if teste_da_sorte <= sorte :
                                                print("Você teve sorte! Causou o dobro de dano")
                                                inimigos.inimigos["guardiao2"]["Energia"] -= 4
                                                sorte -= 1
                                                print("A energia atual do inimigo é: ", inimigos.inimigos["guardiao2"]["Energia"])
                                                print(f"Sua sorte agora é {sorte}")

                                            else :
                                                print("Você não teve sorte, causou menos dano!")
                                                inimigos.inimigos["guardiao2"]["Energia"] -= 1
                                                sorte -= 1
                                                print("A energia atual do inimigo é:", inimigos.inimigos["guardiao2"]["Energia"])
                                                print(f"Sua sorte agora é {sorte}")
                                                
                                        else :
                                            print("Você infelizmente não tem mais sorte")
                                            inimigos.inimigos["guardiao2"]["Energia"] -= 2
                                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["guardiao2"]["Energia"])

                                    else :
                                        inimigos.inimigos["guardiao2"]["Energia"] -= 2
                                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["guardiao2"]["Energia"])

                                #Tomando dano
                                else :
                                    print("Quer testar sua sorte para receber menos dano?")
                                    testarSorte = input().lower()

                                    if testarSorte == "sim" :
                                        if sorte > 0 :
                                            input("Jogue os dados para testar sua sorte...\n")
                                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                            if teste_da_sorte <= sorte :
                                                print("Você teve sorte! Recebeu menos dano!")
                                                energia -= 1
                                                sorte -= 1
                                                print(f"Sua energia atual é {energia}")
                                                print(f"Sua sorte agora é {sorte}")

                                            else :
                                                print("Você não teve sorte, recebeu mais dano!")
                                                energia -= 3
                                                sorte -= 1
                                                print(f"Sua energia atual é {energia}")
                                                print(f"Sua sorte agora é {sorte}")

                                        else :
                                            print("Você infelizmente não tem mais sorte")
                                            energia -= 2
                                            print(f"\nSua energia atual é {energia}")

                                    else :
                                        energia -= 2
                                        print(f"\nSua energia atual é {energia}")

                            print("\nParabéns você sobreviveu! E agora tem uma esmeralda.")
                            print(textos.T11())
                            esmeralda += 1
                            resposta = int(input("Escolha: "))

                            if resposta == 1 :
                                print(textos.T140())
                                energia = 0

                            else :
                                print(textos.T46())

                        #Não subindo no ídolo/tentar subir e falhar/subiu e já pegou a pedra
                        print(textos.T239())
                        resposta = int(input("Escolha: "))

                    #Abrino a porta
                    if resposta == 1  :
                        print(textos.T102())
                        #você gritará:
                        escolha = int(input())
                        match escolha:
                            case 1:
                                print(textos.T133())
                                teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                                if teste_da_habilidade <= habilidade:
                                    print("Você foi habilidoso!")
                                    print(textos.T178())
                                    #Segue ao norte
                                    print(textos.T344())
                                    resposta = input().lower()
                                    #atravessa o facho de luz
                                    if resposta == 'sim':
                                        print(textos.T229())
                                        print(textos.T107)
                                        resposta = input().lower()
                                        #tentar a porta pesada
                                        if resposta == 'sim':
                                            print(textos.T168())
                                            resposta = input().lower()
                                            #pegar o punhal?
                                            if resposta == 'sim':
                                                print(textos.T94())
                                                punhal += 1
                                                print(textos.T174())
                                                #teste a sua sorte
                                                sorte -= 1
                                                input("Jogue os dados para testar sua sorte...\n")
                                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                if teste_da_sorte <= sorte:
                                                    print("Você teve sorte!")
                                                    print(textos.T39())
                                                    #Batalha com a mosca
                                                    print("Prefere fugir da luta?")
                                                    resposta  = input().lower()
                                                    if resposta == 'sim':
                                                        print("Você fugiu, mas perdeu energia!")
                                                        print("Quer testar sua sorte e diminuir o dano?")
                                                        resposta = input().lower()
                                                        if resposta == 'sim':
                                                            #teste a sua sorte
                                                            sorte -= 1
                                                            input("Jogue os dados para testar sua sorte...\n")
                                                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                            if teste_da_sorte <= sorte:
                                                                print("Você teve sorte! Perdeu 1 de energia")
                                                                energia -= 1
                                                                print(textos.T267()) #completar
                                                            else:
                                                                print("Você não teve sorte! Perdeu 3 de energia")
                                                                energia -= 3
                                                                print(textos.T267()) #completar
                                                        elif resposta == 'não':
                                                            print("Você perdeu 2 de energia")
                                                            energia -= 2
                                                            print(textos.T267()) #completar
                                                    elif resposta == 'não':
                                                        print("Que comece a luta!")
                                                        print("Briga com a Mosca...\n")
                                                        while inimigos.inimigos["mosca_gigante"]["Energia"] > 0:
                                                            ataqueInimigo = inimigos.inimigos["mosca_gigante"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                                                            meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)
                                                            print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                                                            input("Jogue os dados...")
                                                            print(f"O seu ataque foi de: {meuAtaque}\n")
                                                            #causando dano
                                                            if meuAtaque > ataqueInimigo:
                                                                print("Quer testar sua sorte para causar mais dano?")
                                                                testarSorte = input().lower()
                                                                if testarSorte == 'não':
                                                                    inimigos.inimigos["mosca_gigante"]["Energia"] -= 2
                                                                    print("\nA energia atual do inimigo é:", inimigos.inimigos["mosca_gigante"]["Energia"])
                                                                elif testarSorte == 'sim':
                                                                    input("Jogue os dados para testar sua sorte...\n")
                                                                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                                    if teste_da_sorte <= sorte:
                                                                        print("Você teve sorte! Causou o dobro de dano")
                                                                        inimigos.inimigos["mosca_gigante"]["Energia"] -= 4
                                                                        sorte -= 1
                                                                        print("A energia atual do inimigo é:", inimigos.inimigos["mosca_gigante"]["Energia"])
                                                                        print(f"Sua sorte agora é {sorte}")
                                                                    else:
                                                                        print("Você não teve sorte, causou menos dano!")
                                                                        inimigos.inimigos["mosca_gigante"]["Energia"] -= 1
                                                                        sorte -= 1
                                                                        print("A energia atual do inimigo é:", inimigos.inimigos["mosca_gigante"]["Energia"])
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
                                                        print(textos.T111())
                                                        print(textos.T267()) #completar

                                                else:
                                                    print("Você não teve sorte!")
                                                    print(textos.T350())
                                                    dano = random.randint(1,6)
                                                    energia -= dano
                                                    print(textos.T39()) #completar
                                            elif resposta == 'não':
                                                print(textos.T267())
                                                resposta = input().lower()
                                                #Oeste
                                                if resposta == 'sim':
                                                    print(textos.T352())
                                                    resposta = input().lower()
                                                    #lutar com o verme
                                                    if resposta == 'sim':
                                                        print(textos.T254())
                                                        #Batalha com o verme 
                                                        print("Prefere fugir da luta?")
                                                    resposta  = input().lower()
                                                    if resposta == 'sim':
                                                        print("Você fugiu, mas perdeu energia!")
                                                        print("Quer testar sua sorte e diminuir o dano?")
                                                        resposta = input().lower()
                                                        if resposta == 'sim':
                                                            #teste a sua sorte
                                                            sorte -= 1
                                                            input("Jogue os dados para testar sua sorte...\n")
                                                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                            if teste_da_sorte <= sorte:
                                                                print("Você teve sorte! Perdeu 1 de energia")
                                                                energia -= 1
                                                            else:
                                                                print("Você não teve sorte! Perdeu 3 de energia")
                                                                energia -= 3
                                                        elif resposta == 'não':
                                                            print("Você perdeu 2 de energia")
                                                            energia -= 2
                                                            print(textos.T267()) #completar
                                                    elif resposta == 'não':
                                                        print("Que comece a luta!")
                                                        print("Briga com a Mosca...\n")
                                                        while inimigos.inimigos["mosca_gigante"]["Energia"] > 0:
                                                            ataqueInimigo = inimigos.inimigos["mosca_gigante"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                                                            meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)
                                                            print(f"O ataque do inimigo foi de: {ataqueInimigo}")
                                                            input("Jogue os dados...")
                                                            print(f"O seu ataque foi de: {meuAtaque}\n")
                                                            #causando dano
                                                            if meuAtaque > ataqueInimigo:
                                                                print("Quer testar sua sorte para causar mais dano?")
                                                                testarSorte = input().lower()
                                                                if testarSorte == 'não':
                                                                    inimigos.inimigos["mosca_gigante"]["Energia"] -= 2
                                                                    print("\nA energia atual do inimigo é:", inimigos.inimigos["mosca_gigante"]["Energia"])
                                                                elif testarSorte == 'sim':
                                                                    input("Jogue os dados para testar sua sorte...\n")
                                                                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                                    if teste_da_sorte <= sorte:
                                                                        print("Você teve sorte! Causou o dobro de dano")
                                                                        inimigos.inimigos["mosca_gigante"]["Energia"] -= 4
                                                                        sorte -= 1
                                                                        print("A energia atual do inimigo é:", inimigos.inimigos["mosca_gigante"]["Energia"])
                                                                        print(f"Sua sorte agora é {sorte}")
                                                                    else:
                                                                        print("Você não teve sorte, causou menos dano!")
                                                                        inimigos.inimigos["mosca_gigante"]["Energia"] -= 1
                                                                        sorte -= 1
                                                                        print("A energia atual do inimigo é:", inimigos.inimigos["mosca_gigante"]["Energia"])
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
                                                        print(textos.T76())
                                                    elif resposta == 'não':
                                                        print(textos.T68())
                                                        escolha = int(input())
                                                        match escolha:
                                                            case 1:
                                                                print(textos.T271())
                                                                habilidade -= 1
                                                                escudo = 0
                                                                print(textos.T237()) #completar
                                                            case 2:
                                                                print(textos.T30())
                                                                #teste a sua sorte
                                                                sorte -= 1
                                                                input("Jogue os dados para testar sua sorte...\n")
                                                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                                                if teste_da_sorte <= sorte:
                                                                    print("Você teve sorte!")
                                                                    print(textos.T160())
                                                                    print(textos.T237()) 
                                                                    resposta = input().lower()
                                                                    #abrir a porta
                                                                    if resposta == 'sim':
                                                                        print(textos.T12())
                                                                        escolha = int(input())
                                                                        match escolha:
                                                                            case 1:
                                                                                print(textos.T382())
                                                                                escolha = int(input())
                                                                                match escolha:
                                                                                    case 1:
                                                                                        print(textos.T144()) #errado
                                                                                        print(textos.T85())
                                                                                        energia = 0

                                                                                    case 2:
                                                                                        print(textos.T227()) #errado
                                                                                        print(textos.T85())
                                                                                        energia = 0
                                                                                    case 3:
                                                                                        print(textos.T391()) #certo
                                                                                        if habilidade < habilidadeFixa:
                                                                                            habilidade += 1
                                                                                        if energia < energiaFixa:
                                                                                            energia += 1
                                                                                        if sorte < sorteFixa:
                                                                                            sorte += 1
                                                                                        print(textos.T100())
                                                                                        resposta = input().lower()
                                                                                        #abrir a outra porta
                                                                                        if resposta == 'sim':
                                                                                            print(textos.T87())
                                                                                            print(textos.T381())
                                                                                            resposta = input().lower()
                                                                                            #pegar o pergaminho
                                                                                            if resposta == 'sim':
                                                                                                print(textos.T331())
                                                                                                #batalha com o esqueleto-guerreiro #continuar
                                                                                            elif resposta == 'não':
                                                                                                print(textos.T128())
                                                                                                resposta = input().lower()
                                                                                                #atravessar a passagem
                                                                                                if resposta == 'sim':
                                                                                                    print(textos.T35())
                                                                                                    resposta = input().lower()
                                                                                                    #Bater no alçapão
                                                                                                    if resposta == 'sim':
                                                                                                        print(textos.T333())
                                                                                                        energia = 0 #morte
                                                                                                    #abrir o alçapão
                                                                                                    elif resposta == 'não':
                                                                                                        print(textos.T124())
                                                                                                        #batalha com os goblins #continuar
                                                                                                #para e comer cogumelos
                                                                                                elif resposta == 'não':
                                                                                                    print(textos.T233())
                                                                                                    energia = 0 #morte
                                                                                        elif resposta == 'não':
                                                                                            print(textos.T217())
                                                                                            escudo = 0
                                                                                            if escudo == 0:
                                                                                                habilidade -= 1
                                                                                            print(textos.T36())
                                                                                            teste_duplo = random.randint(1,6) + random.randint(1,6)
                                                                                            if teste_duplo <= habilidade and teste_duplo <= energia:
                                                                                                print(textos.T340())
                                                                                                print(textos.T381()) #completar
                                                                                            else:
                                                                                                print(textos.T7())
                                                                                                energia = 0
                                                                            case 2:
                                                                                print(textos.T195())
                                                                                print(textos.T382()) #completar
                                                                            case 3:
                                                                                print(textos.T250())
                                                                                escolha = int(input())
                                                                                match escolha:
                                                                                    case 1:
                                                                                        print(textos.T44()) #morte
                                                                                        energia = 0
                                                                                    case 2:
                                                                                        print(textos.T195())
                                                                                        print(textos.T382()) #completar
                                                                                    case 3:
                                                                                        print(textos.T382()) #completar

                                                                    #seguir ao norte
                                                                    elif resposta == 'não':
                                                                        print(textos.T100()) #completar
                                                                else:
                                                                    print("Você não teve sorte!")
                                                                    print(textos.T319())
                                                                    print(textos.T285())
                                                                    habilidade -= 1
                                                                    energia -= 2
                                                                    rubi += 1
                                                                    print(textos.T237()) #completar
                                                            case 3:
                                                                print(textos.T212())
                                                                print(textos.T285())
                                                                habilidade -= 1
                                                                energia -= 2
                                                                rubi += 1
                                                                print(textos.T237()) #completar
                                                #Leste
                                                elif resposta == 'não':
                                                    print(textos.T68()) 
                                        #seguir pelo tunel
                                        elif resposta == 'não':
                                            print(textos.T267())
                                    #contorna o facho de luz
                                    elif resposta == 'não':
                                        print(textos.T107())
                                        resposta = input().lower()
                                        #tentar a porta pesada
                                        if resposta == 'sim':
                                            print(textos.T168())
                                        #seguir pelo tunel
                                        elif resposta == 'não':
                                            print(textos.T267())
                                else:
                                    print("Faltou habilidade!")
                                    print(textos.T17())
                                    #morte
                                    energia = 0
                            case 2:
                                print(textos.T251())
                                #entra de novo no tunel e segue ao norte
                                print(textos.T344())
                    elif resposta == 'não':
                        print(textos.T344())
        elif resposta == 'não':
            print(textos.T239())
            resposta = input().lower()
            #quer abrir a porta?
            if resposta == 'sim':
                print(textos.T102())
                #você gritará:
                escolha = int(input())
                match escolha:
                    case 1:
                        print(textos.T133())
                        teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                        if teste_da_habilidade <= habilidade:
                            print("Você foi habilidoso!")
                            print(textos.T178())
                            #segue ao norte
                            print(textos.T344())
                        else:
                            print("Faltou habilidade!")
                            print(textos.T17())
                            #morte
                            energia = 0
                    case 2:
                        print(textos.T251())
                        #entra de novo no tunel e segue ao norte
                        print(textos.T344())                                                                        
            elif resposta == 'não':
                print(textos.T344())
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
                            resposta = input().lower()
                            #pegar a joia da esquerda
                            if resposta == 'sim':
                                print(textos.T151())
                                #Batalha com os guardiões voadores
                            #pegar a joia da direita = morte
                            elif resposta =='não':
                                print(textos.T34())
                                energia = 0
                        #Não possui corda
                        elif corda == 0:
                            print(textos.T186())
                            #teste a sua sorte
                            sorte -= 1
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                            if teste_da_sorte <= sorte:
                                print("Você teve sorte!")
                                print(textos.T260())
                                resposta = input().lower()
                                #arrancar o olho da esquerda
                                if resposta == 'sim':
                                    print(textos.T166())
                                #arrancar o olho da direita 
                                elif resposta =='não':
                                    print(textos.T140())
                            else:
                                print("Você não teve sorte!")
                                print(textos.T358())
                                #Você cai e perde energia, segue para o norte
                                energia -= 2
                                print(textos.T239())
                                resposta = input().lower()
                                #quer abrir a porta?
                                if resposta == 'sim':
                                    print(textos.T102())
                                    #você gritará:
                                    escolha = int(input())
                                    match escolha:
                                        case 1:
                                            print(textos.T133())
                                            teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                                            if teste_da_habilidade <= habilidade:
                                                print("Você foi habilidoso!")
                                                print(textos.T178())
                                                #segue ao norte
                                                print(textos.T344())
                                            else:
                                                print("Faltou habilidade!")
                                                print(textos.T17())
                                                #morte
                                                energia = 0
                                        case 2:
                                            print(textos.T251())
                                            #entra de novo no tunel e segue ao norte
                                            print(textos.T344())
                                elif resposta == 'não':
                                    print(textos.T344())
                    elif resposta == 'não':
                        print(textos.T239())
                        resposta = input().lower()
                        #quer abrir a porta?
                        if resposta == 'sim':
                            print(textos.T102())
                            #você gritará:
                            escolha = int(input())
                            match escolha:
                                case 1:
                                    print(textos.T133())
                                    teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                                    if teste_da_habilidade <= habilidade:
                                        print("Você foi habilidoso!")
                                        print(textos.T178())
                                        #segue ao norte
                                        print(textos.T344())
                                    else:
                                        print("Faltou habilidade!")
                                        print(textos.T17())
                                        #morte
                                        energia = 0
                                case 2:
                                    print(textos.T251())
                                    #entra de novo no tunel e segue ao norte
                                    print(textos.T344())
                        elif resposta == 'não':
                            print(textos.T344())
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
                        resposta = input().lower()
                        #pegar a joia da esquerda
                        if resposta == 'sim':
                            print(textos.T151())
                            #Batalha com os guardiões voadores
                        #pegar a joia da direita = morte
                        elif resposta =='não':
                            print(textos.T34())
                            energia = 0
                    #Não possui corda
                    elif corda == 0:
                        print(textos.T186())
                        #teste a sua sorte
                        sorte -= 1
                        input("Jogue os dados para testar sua sorte...\n")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                        if teste_da_sorte <= sorte:
                            print("Você teve sorte!")
                            print(textos.T260())
                            resposta = input().lower()
                            #arrancar o olho da esquerda
                            if resposta == 'sim':
                                print(textos.T166())
                            #arrancar o olho da direita 
                            elif resposta =='não':
                                print(textos.T140())
                        else:
                            print("Você não teve sorte!")
                            print(textos.T358())
                            #Você cai e perde energia, segue para o norte
                            energia -= 2
                            print(textos.T239())
                            resposta = input().lower()
                            #quer abrir a porta?
                            if resposta == 'sim':
                                print(textos.T102())
                                #você gritará:
                                escolha = int(input())
                                match escolha:
                                    case 1:
                                        print(textos.T133())
                                        teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                                        if teste_da_habilidade <= habilidade:
                                            print("Você foi habilidoso!")
                                            print(textos.T178())
                                            #segue ao norte
                                            print(textos.T344())
                                        else:
                                            print("Faltou habilidade!")
                                            print(textos.T17())
                                            #morte
                                            energia = 0
                                    case 2:
                                        print(textos.T251())
                                        #entra de novo no tunel e segue ao norte
                                        print(textos.T344())
                            elif resposta == 'não':
                                print(textos.T344())                                                                    
                elif resposta == 'não':
                    print(textos.T239())
                    resposta = input().lower()
                    #quer abrir a porta?
                    if resposta == 'sim':
                        print(textos.T102())
                        #você gritará:
                        escolha = int(input())
                        match escolha:
                            case 1:
                                print(textos.T133())
                                teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                                if teste_da_habilidade <= habilidade:
                                    print("Você foi habilidoso!")
                                    print(textos.T178())
                                    #segue ao norte
                                    print(textos.T344())
                                else:
                                    print("Faltou habilidade!")
                                    print(textos.T17())
                                    #morte
                                    energia = 0
                            case 2:
                                print(textos.T251())
                                #entra de novo no tunel e segue ao norte
                                print(textos.T344())
                    elif resposta == 'não':
                        print(textos.T344())                                                           
    else:
        print("Você não teve sorte!")
        print(textos.T309())
        energia -= 3
        #teste a sua sorte de novo
        sorte -= 1
        input("Jogue os dados para testar sua sorte...\n")
        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
        if teste_da_sorte <= sorte:
            print("Você teve sorte!")
            print(textos.T231())
            print(textos.T110())
        else:
            # acido queima = morte
            print("Você não teve sorte!")
            print(textos.T193())
            energia = 0
elif resposta == 'não':
    print(textos.T375())
    moringa +=1
    print(textos.T110())
#Atacá-los
case 2:
#Mata um e luta com o outro goblin
print(textos.T51())
#Matando o HobGoblin restante
print("Briga com o HobGoblin2...\n")
while inimigos.inimigos["hobgoblin2"]["Energia"] > 0:
    ataqueInimigo = inimigos.inimigos["hobgoblin2"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
    meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)
    print(f"O ataque do inimigo foi de: {ataqueInimigo}")
    input("Jogue os dados...")
    print(f"O seu ataque foi de: {meuAtaque}\n")
    #causando dano
    if meuAtaque > ataqueInimigo:
        print("Quer testar sua sorte para causar mais dano?")
        testarSorte = input().lower()
        if testarSorte == 'não':
            inimigos.inimigos["hobgoblin2"]["Energia"] -= 2
            print("\nA energia atual do inimigo é:", inimigos.inimigos["hobgoblin2"]["Energia"])
        elif testarSorte == 'sim':
            input("Jogue os dados para testar sua sorte...\n")
            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
            if teste_da_sorte <= sorte:
                print("Você teve sorte! Causou o dobro de dano")
                inimigos.inimigos["hobgoblin2"]["Energia"] -= 4
                sorte -= 1
                print("A energia atual do inimigo é:", inimigos.inimigos["hobgoblin2"]["Energia"])
                print(f"Sua sorte agora é {sorte}")
            else:
                print("Você não teve sorte, causou menos dano!")
                inimigos.inimigos["hobgoblin2"]["Energia"] -= 1
                sorte -= 1
                print("A energia atual do inimigo é:", inimigos.inimigos["hobgoblin2 "]["Energia"])
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
        #teste a sua sorte
        sorte -= 1
        input("Jogue os dados para testar sua sorte...\n")
        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
        if teste_da_sorte <= sorte:
            print("Você teve sorte!")
            print(textos.T231())
            print(textos.T110()) #completar
    elif resposta == 'não':
        print(textos.T375())
        moringa +=1
        print(textos.T110()) #completar
        #Tentar passar despercebido
        case 3 :
        #corre dos goblins indo ao norte
        print(textos.T355()) #continuar
            
            
    #         #não tocar o sino
    #         elif resposta == "não":
    #             print(textos.T362()) 
    #     #Mudando para o norte
    #     elif resposta == "não":
    #         print(textos.T387()) 
    # #Indo para o Leste
    # elif resposta == "não":
    #     print(textos.T119()) 
    # #Não abrir a caixa
    # elif resposta == 2:
    #     print(textos.T66()) 
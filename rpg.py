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
tubo_oco_madeira = 0
taça = 0

#Variáveis adicionadas para auxiliar mais para frente
beber = ""

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
            resposta = int(input("Escolha: "))
            
            if resposta == 1 :
                print(textos.T373())
            
            else :
                print(textos.T215())
                energia -= 2

        print(textos.T13())
        resposta = int(input("Escolha: "))
        
        if resposta == 1 :
            print(textos.T147())
            energia += 1
            beber = "sim"
        
        else :
            beber = "não"

        print(textos.T182())

        #Se bebeu o líquido
        if beber == "sim" :
            print(textos.T25)
        
        #Se não bebeu o líquido
        elif beber == "não" :
            print(textos.T242())
            input("Jogue os dados...🎲")
            sobrevive = random.randint(1,6) + random.randint(1,6)
            
            if sobrevive <= habilidade :
                print(textos.T48())
            
            else :
                print(textos.T366())
                energia = 0
        
        print(textos.T197())
        resposta = int(input("Escolha: "))
        
        if resposta == 1 :
            print(textos.T171())
            energia -= 4
            corda += 1
        
        elif resposta == 2 :
            print(textos.T156())
            escolha = int(input("Escolha: "))
            
            if escolha == 1 :
                print(textos.T208())
                corda += 1
        
        print(textos.T326())
        input("Jogue o dado...🎲")
        teste = random.randint(1,6)
        
        if teste == 1 or teste == 2 :
            print(textos.T91())
            
            #Matando a primeira Orca
            print("Briga com a Orca Nº1...\n")

            while inimigos.inimigos["orca1"]["Energia"] > 0 :
                ataqueInimigo = inimigos.inimigos["orca1"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6) - 4

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
                                inimigos.inimigos["orca1"]["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", inimigos.inimigos["orca1"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Você não teve sorte, causou menos dano!")
                                inimigos.inimigos["orca1"]["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", inimigos.inimigos["orca1"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            inimigos.inimigos["orca1"]["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca1"]["Energia"])

                    else :
                        inimigos.inimigos["orca1"]["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca1"]["Energia"])

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

            #Matando a segunda Orca
            print("Briga com a Orca Nº2...\n")

            while inimigos.inimigos["orca2"]["Energia"] > 0 :
                ataqueInimigo = inimigos.inimigos["orca2"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
                meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6) - 4

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
                                inimigos.inimigos["orca2"]["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", inimigos.inimigos["orca2"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Você não teve sorte, causou menos dano!")
                                inimigos.inimigos["orca2"]["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", inimigos.inimigos["orca2"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            inimigos.inimigos["orca2"]["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca2"]["Energia"])

                    else :
                        inimigos.inimigos["orca2"]["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca2"]["Energia"])

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
        
        if teste == 3 or teste == 4 :
            print(textos.T189())
            energia -= 3
        
            #Matando a primeira Orca
            print("Briga com a Orca Nº1...\n")

            while inimigos.inimigos["orca1"]["Energia"] > 0 :
                ataqueInimigo = inimigos.inimigos["orca1"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                inimigos.inimigos["orca1"]["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", inimigos.inimigos["orca1"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Você não teve sorte, causou menos dano!")
                                inimigos.inimigos["orca1"]["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", inimigos.inimigos["orca1"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            inimigos.inimigos["orca1"]["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca1"]["Energia"])

                    else :
                        inimigos.inimigos["orca1"]["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca1"]["Energia"])

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

            #Matando a segunda Orca
            print("Briga com a Orca Nº2...\n")

            while inimigos.inimigos["orca2"]["Energia"] > 0 :
                ataqueInimigo = inimigos.inimigos["orca2"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                inimigos.inimigos["orca2"]["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", inimigos.inimigos["orca2"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Você não teve sorte, causou menos dano!")
                                inimigos.inimigos["orca2"]["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", inimigos.inimigos["orca2"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            inimigos.inimigos["orca2"]["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca2"]["Energia"])

                    else :
                        inimigos.inimigos["orca2"]["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca2"]["Energia"])

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
            
        if teste == 5 or teste == 6 :
            print(textos.T380())
            
            #Matando a primeira Orca
            print("Briga com a Orca Nº1...\n")

            while inimigos.inimigos["orca1"]["Energia"] > 0 :
                ataqueInimigo = inimigos.inimigos["orca1"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                inimigos.inimigos["orca1"]["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", inimigos.inimigos["orca1"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Você não teve sorte, causou menos dano!")
                                inimigos.inimigos["orca1"]["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", inimigos.inimigos["orca1"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            inimigos.inimigos["orca1"]["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca1"]["Energia"])

                    else :
                        inimigos.inimigos["orca1"]["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca1"]["Energia"])

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

            #Matando a segunda Orca
            print("Briga com a Orca Nº2...\n")

            while inimigos.inimigos["orca2"]["Energia"] > 0 :
                ataqueInimigo = inimigos.inimigos["orca2"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                inimigos.inimigos["orca2"]["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", inimigos.inimigos["orca2"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Você não teve sorte, causou menos dano!")
                                inimigos.inimigos["orca2"]["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", inimigos.inimigos["orca2"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            inimigos.inimigos["orca2"]["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca2"]["Energia"])

                    else :
                        inimigos.inimigos["orca2"]["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["orca2"]["Energia"])

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
        
        print("\nParabéns, você sobreviveu!")
        print(textos.T257())
        pecas_de_ouro += 1
        tubo_oco_madeira += 1

        print(textos.T164())
        resposta = int(input("Escolha: "))
        
        #Entrando na câmara
        if resposta == 1 :
            print(textos.T299())
            escolha = int(input("Escolha: "))
            
            #Vasculhando o bárbaro
            if escolha == 1 :
                print(textos.T126())
                resposta = int(input("Escolha: "))
                
                #Comendo a carne
                if resposta == 1 :
                    print(textos.T226())
                    energia += 3
                    escolha = int(input("Escolha: "))
                    
                    #Entrando na alcova
                    if escolha == 1 :
                        print(textos.T41_2())
                        resposta = int(input("Escolha: "))
                        
                        #Bebendo o líquido
                        if escolha == 1 :
                            print(textos.T98())
                            input("Teste sua sorte...")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                            
                            #Tendo sorte
                            if teste_da_sorte <= sorte :
                                print(textos.T105_2())
                                taça += 1
                            
                            #Não tendo sorte
                            elif teste_da_sorte >= sorte :
                                print(textos.T235())
                                energia -= 2
                                print(textos.T73_2())
                                input("...🚪")
                
                #Não comendo a carne, MESMO SABENDO DELA, e indo até a alcova
                elif resposta == 2 :
                    print(textos.T41_3())
                    escolha = int(input("Escolha: "))
                    
                    #Bebendo o líquido
                    if escolha == 1 :
                        print(textos.T98())
                        input("Teste sua sorte...")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                        
                        #Tendo sorte
                        if teste_da_sorte <= sorte :
                            print(textos.T105_2())
                            taça += 1
                        
                        #Não tendo sorte
                        elif teste_da_sorte >= sorte :
                            print(textos.T235())
                            energia -= 2
                            print(textos.T73_2())
                            input("...🚪")
                    
                    #Voltando para a carne e comendo
                    elif escolha == 2 :
                        print(textos.T226_2())
                        energia += 3
                        resposta = int(input("Escolha: "))
                        
                        #Voltando para tomar o líquido
                        if resposta == 1 :
                            print(textos.T98())
                            input("Teste sua sorte...")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                            
                            #Tendo sorte
                            if teste_da_sorte <= sorte :
                                print(textos.T105_2())
                                taça += 1
                            
                            #Não tendo sorte
                            elif teste_da_sorte >= sorte :
                                print(textos.T235())
                                energia -= 2
                                print(textos.T73_2())
                                input("...🚪")

            #Indo direto para a alcova
            elif escolha == 2 :
                print(textos.T41())
                resposta = int(input("Escolha: "))
                
                #Bebendo o líquido
                if resposta == 1 :
                    print(textos.T98())
                    input("Teste sua sorte...")
                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                    
                    #Tendo sorte
                    if teste_da_sorte <= sorte :
                        print(textos.T105())
                        taça += 1
                        escolha = int(input("Escolha: "))
                        
                        #Vasculhando o Bárbaro antes de ir embora
                        if escolha == 1 :
                            print(textos.T126_2())
                            resposta = int(input("Escolha: "))
                            
                            #Comendo a carne antes de ir embora
                            if resposta == 1 :
                                print(textos.T226_3())
                    
                    #Não tendo sorte
                    elif teste_da_sorte >= sorte :
                        print(textos.T235())
                        energia -= 2
                        print(textos.T73_2())
                        input("...🚪")
                
                #Vasculhando o bárbaro

        #AQUI É NÃO ENTRANDO NA PORTA OU DEPOIS DE VOCÊ SAIR DELA, É A CONTINUAÇÃO
        print(textos.T83())
        
    #CONTINUAÇÃO, VOCÊ TAVA FAZENDO AQUI EM CIMA AINDA =======================================================================
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
                                print(textos.T239())

                            else:
                                print("Você não teve sorte!")
                                print(textos.T261())
                                print(textos.T239()) #completar
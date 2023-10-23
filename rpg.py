# Ana Zerlin        RM 98065
# Bianca Dancs      RM 551645
# Gabriel Pimentel  RM 99880
# Hellen Assis      RM 98284

#LINHA QUE ESTOU TRABALHANDO NO MOMENTO: 2299

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
punhal_ornamental = 0
rubi = 0
esmeralda = 0
escudo = 1
tubo_oco_madeira = 0
taça = 0
anel_de_ouro = 0
objeto_redondo_pequeno = 0

#Variáveis adicionadas para auxiliar mais para frente
beber = ""

#Apresentação
print("=" * 50)
print("Bem-vindo ao Calabouço da Morte")

#Mostrando a ficha
print("=" * 50)
print("SUA FICHA\n")

#Recuperando valores para a ficha com a função
habilidade, energia, sorte, provisoes = ficha.fichaValores()

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
    
    #Indo para o oeste - ESCOLHA PRINCIPAL 1
    if resposta == 1 :
        print(textos.T293())
        resposta = int(input("Escolha: "))

        #Seguindo no oeste - ESCOLHA SECUNDÁRIA 1
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
            
            #Tenta conversar com eles
            if escolha == 1 :
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

                print("\nParabéns você sobreviveu!")
                
                if energiaFixa - energia >= 4 :
                    print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                    resposta = input("\nSim ou Não?").lower()
                    
                    if resposta == "sim" :
                        energia += 4
                        provisoes -=1
                
                print(textos.T9())
                escolha = int(input("Escolha: "))

                #Toma o líquido
                if resposta == 1 :
                    print(textos.T158())
                    habilidade -= 1
                    energia -= 4
                    
                    if energiaFixa - energia >= 4 :
                        print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                        resposta = input("\nSim ou Não?").lower()
                        
                        if resposta == "sim" :
                            energia += 4
                            provisoes -=1
                    
                    print(textos.T275())
                    
                    #Teste a sua sorte
                    sorte -= 1
                    input("Teste sua sorte...\n")
                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                    #Não tendo sorte
                    if teste_da_sorte >= sorte :
                        print(textos.T309())
                        energia -= 3
                        
                        if energiaFixa - energia >= 4 :
                            print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                            resposta = input("\nSim ou Não?").lower()
                            
                            if resposta == "sim" :
                                energia += 4
                                provisoes -=1

                        if energia > 0 :
                            input("Teste sua sorte")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            #Não tendo sorte de novo
                            if teste_da_sorte >= sorte :
                                print(textos.T193())
                                energia = 0
                            
                            #Finalmente tendo sorte
                            else :
                                print(textos.T231())
                    
                    #Tendo sorte
                    else :
                        print(textos.T231())
                
                #Colocando um pano no líquido
                else :
                    print(textos.T375())
                    moringa += 1
            
            #Ataca eles de uma vez
            elif escolha == 2 :
                print(textos.T51())
                
                #Matando o Hobgoblin restante
                print("Briga com o Hobgoblin restante...\n")
                
                while inimigos.inimigos["hobgoblin"]["Energia"] > 0 :
                    ataqueInimigo = inimigos.inimigos["hobgoblin"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                    inimigos.inimigos["hobgoblin"]["Energia"] -= 4
                                    sorte -= 1
                                    print("A energia atual do inimigo é: ", inimigos.inimigos["hobgoblin"]["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("Você não teve sorte, causou menos dano!")
                                    inimigos.inimigos["hobgoblin"]["Energia"] -= 1
                                    sorte -= 1
                                    print("A energia atual do inimigo é:", inimigos.inimigos["hobgoblin"]["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Infelizmente você não tem mais sorte")
                                inimigos.inimigos["hobgoblin"]["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", inimigos.inimigos["hobgoblin"]["Energia"])

                        else :
                            inimigos.inimigos["hobgoblin"]["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["hobgoblin"]["Energia"])

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
                            
                print("\nParabéns você sobreviveu!")
                
                if energiaFixa - energia >= 4 :
                    print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                    resposta = input("\nSim ou Não?").lower()
                    
                    if resposta == "sim" :
                        energia += 4
                        provisoes -=1
                
                print(textos.T9())
                escolha = int(input("Escolha: "))

                #Toma o líquido
                if resposta == 1 :
                    print(textos.T158())
                    habilidade -= 1
                    energia -= 4
                    
                    if energiaFixa - energia >= 4 :
                        print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                        resposta = input("\nSim ou Não?").lower()
                        
                        if resposta == "sim" :
                            energia += 4
                            provisoes -=1
                    
                    print(textos.T275())
                    
                    #Teste a sua sorte
                    sorte -= 1
                    input("Teste sua sorte...\n")
                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                    #Não tendo sorte
                    if teste_da_sorte >= sorte :
                        print(textos.T309())
                        energia -= 3
                        
                        if energiaFixa - energia >= 4 :
                            print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                            resposta = input("\nSim ou Não?").lower()
                            
                            if resposta == "sim" :
                                energia += 4
                                provisoes -=1

                        if energia > 0 :
                            input("Teste sua sorte")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            #Não tendo sorte de novo
                            if teste_da_sorte >= sorte :
                                print(textos.T193())
                                energia = 0
                            
                            #Finalmente tendo sorte
                            else :
                                print(textos.T231())
                    
                    #Tendo sorte
                    else :
                        print(textos.T231())
                
                #Colocando um pano no líquido
                else :
                    print(textos.T375())
                    moringa += 1
            
            #Passando despercebido
            elif escolha == 3 :
                print(textos.T355())

            #NO 137 TODOS CHEGAM NO 110
            print(textos.T110())
            escolha = int(input("Escolha: "))

            #Caminhando entre os postes
            if escolha == 1 :
                print(textos.T58())
                input("Jogue os dados...🎲")
                teste_da_habilidade = random.randint(1,6) + random.randint(1,6)

                #Passando o teste
                if teste_da_habilidade <= habilidade :
                    #Segue ao leste
                    print(textos.T80())
                
                #Não passando no teste
                else :
                    print(textos.T246())
                    sorte -= 2
                    input("Jogue os dados...🎲")
                    farpas = random.randint(1,6) + random.randint(1,6)
                    energia -= farpas
                    print(f"\nVocê foi acertado por {farpas} farpas")

                    if energia > 0 :
                        print(textos.T246_2())

            #Subindo os postes
            elif escolha == 2 :
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
        
        #Seguindo para o norte -  ESCOLHA SECUNDÁRIA 2
        elif resposta == 2 :
            print(textos.T387())
            
            #Matando o Homem da Caverna
            print("Briga com o Homem da Caverna...\n")

            while inimigos.inimigos["homem_caverna"]["Energia"] > 0 :
                ataqueInimigo = inimigos.inimigos["homem_caverna"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                inimigos.inimigos["homem_caverna"]["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", inimigos.inimigos["homem_caverna"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Você não teve sorte, causou menos dano!")
                                inimigos.inimigos["homem_caverna"]["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", inimigos.inimigos["homem_caverna"]["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            inimigos.inimigos["homem_caverna"]["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["homem_caverna"]["Energia"])

                    else :
                        inimigos.inimigos["homem_caverna"]["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", inimigos.inimigos["homem_caverna"]["Energia"])

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
            
            print("\nParabéns você sobreviveu!")
            
            if energiaFixa - energia >= 4 :
                print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                resposta = input("\nSim ou Não?").lower()
                
                if resposta == "sim" :
                    energia += 4
                    provisoes -=1
            
            print(textos.T114())
            escolha = int(input("Escolha: "))
            
            #Colocando a munheira
            if escolha == 1 :
                print(textos.T336())
                habilidade -= 4
            
            print(textos.T298())
            resposta = int(input("Escolha: "))
            
            #Abrindo a moxila e pegando a moeda
            if resposta == 1 :
                print(textos.T304())
                energia -= 6

                if energiaFixa - energia >= 4 :
                    print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                    resposta = input("\nSim ou Não?").lower()
                    
                    if resposta == "sim" :
                        energia += 4
                        provisoes -=1
                
                print(textos.T20())
                habilidade -= 1
                pecas_de_ouro += 1
            
            print(textos.T279())
            print(textos.T32())
    
    #Indo para o leste - ESCOLHA PRINCIPAL 2
    elif resposta == 2 :
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
            
            print("\nParabéns você sobreviveu!")
            
            if energiaFixa - energia >= 4 :
                print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                resposta = input("\nSim ou Não?").lower()
                
                if resposta == "sim" :
                    energia += 4
                    provisoes -=1
        
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
            
            print("\nParabéns você sobreviveu!")
            
            if energiaFixa - energia >= 4 :
                print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                resposta = input("\nSim ou Não?").lower()
                
                if resposta == "sim" :
                    energia += 4
                    provisoes -=1
        
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
            
            print("\nParabéns você sobreviveu!")
            
            if energiaFixa - energia >= 4 :
                print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                resposta = input("\nSim ou Não?").lower()
                
                if resposta == "sim" :
                    energia += 4
                    provisoes -=1
        
        print(textos.T257())
        pecas_de_ouro += 1
        tubo_oco_madeira += 1

        print(textos.T164())
        resposta = int(input("Escolha: "))
        
        #ENTRANDO NA CÂMARA
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
                                energia += 3
                    
                    #Não tendo sorte
                    elif teste_da_sorte >= sorte :
                        print(textos.T235())
                        energia -= 2
                        print(textos.T73())
                        escolha = int(input("Escolha: "))
                        
                        #Voltando para vasculhar antes de ir embora
                        if escolha == 1 :
                            print(textos.T126_2())
                            resposta = int(input("Escolha: "))
                            
                            #Comendo a carne antes de ir embora
                            if resposta == 1 :
                                print(textos.T226_3())
                                energia += 3
                
                #Vasculhando o bárbaro
                elif resposta == 2 :
                    print(textos.T126_3())
                    escolha = int(input("Escolha: "))
                    
                    #Comendo a carne
                    if escolha == 1 :
                        print(textos.T226_2())
                        resposta = int(input("Escolha: "))
                        
                        #Voltando para tomar o líquido antes de sair
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
                    
                    #Ignorando a carne e voltando para beber o líquido
                    elif escolha == 2 :
                        print(textos.T98())
                        input("Teste sua sorte...")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                        
                        #Tendo sorte
                        if teste_da_sorte <= sorte :
                            print(textos.T105_3())
                            taça += 1
                            resposta = int(input("Escolha: "))
                            
                            #Comendo a carne antes de ir embora
                            if resposta == 1 :
                                print(textos.T226_3())
                                energia += 3
                        
                        #Não tendo sorte
                        elif teste_da_sorte >= sorte :
                            print(textos.T235())
                            energia -= 2
                            print(textos.T73_3())
                            
                            #Voltando para comer a carne antes de ir embora
                            if resposta == 1 :
                                print(textos.T226_3())
                                energia += 3
        
        print(textos.T83())

    #TUDO CHEGA NO 37
    print(textos.T37())
    resposta = int(input("Escolha: "))

    #Subindo no ídolo
    if resposta == 1 :
        print(textos.T351())
        print(f"Inverntário: - Corda: {corda}")
        cordaPergunta = input("Sim ou não?")

        #Possui corda - CONCLUÍDO
        if corda != 0 :
            print(textos.T396())
            resposta = int(input("Escolha: "))
            corda -= 1

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
                
                if energiaFixa - energia >= 4 :
                    print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                    resposta = input("\nSim ou Não?").lower()
                    
                    if resposta == "sim" :
                        energia += 4
                        provisoes -=1
                
                print(textos.T240())
                esmeralda += 1
                resposta = int(input("Escolha: "))

                #Pegando a joia da direita depois de pegar a da esquerda
                if resposta == 1 :
                    print(textos.T34())
                    energia = 0

                #Descendo do ídolo
                elif resposta == 2 :
                    print(textos.T89())
                    #Teste a sua sorte para tirar a corda
                    sorte -= 1
                    input("Teste sua sorte...\n")
                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                    #Tendo sorte
                    if teste_da_sorte <= sorte :
                        print("Você teve sorte!")
                        print(textos.T54())
                        corda += 1

                    #Não tendo sorte
                    else:
                        print("Você não teve sorte!")
                        print(textos.T261())
        
        #Não possui corda - CONCLUÍDO
        elif corda == 0 :
            print(textos.T186())
            #Testando a sorte
            input("Teste sua sorte...\n")
            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
            sorte -= 1

            #Não tendo sorte
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

                    if energiaFixa - energia >= 4 :
                        print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                        resposta = input("\nSim ou Não?").lower()
                        
                        if resposta == "sim" :
                            energia += 4
                            provisoes -=1
                    
                    print(textos.T11())
                    esmeralda += 1
                    resposta = int(input("Escolha: "))

                    if resposta == 1 :
                        print(textos.T140())
                        energia = 0

                    else :
                        print(textos.T46())
        
    #TODOS OS CAMINHO VÃO VIR PARA O TEXTO 239
    print(textos.T239())
    resposta = int(input("Escolha: "))
    
    #Abrindo a porta
    if resposta == 1 :
        print(textos.T102())
        escolha = int(input("Escolha: "))
        
        #Gritando salve
        if escolha == 1 :
            print(textos.T133())
            input("Jogue os dados...🎲")
            teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
            
            #Passando no teste de habilidade
            if teste_da_habilidade <= habilidade :
                print(textos.T178())
            
            #Não passando no teste
            else :
                print(textos.T17())
                energia = 0
        
        #Falando que o mestre dele é um verme
        elif escolha == 2 :
            print(textos.T251())
            anel_de_ouro += 1
    
    #Seguindo para o norte
    print(textos.T344())
    resposta = int(input("Escolha: "))
    
    #Olhando pelo feixo
    if resposta == 1 :
        print(textos.T229())
    
    #Não olhando
    print(textos.T107())
    resposta = int(input("Escolha: "))
    
    #Tentando a porta
    if resposta == 1 :
        print(textos.T168())
        escolha = int(input("Escolha: "))
        
        #Pegando a adaga
        if escolha == 1 :
            print(textos.T94())
            punhal_ornamental += 1
            print(textos.T174())
            
            #Teste de sorte
            sorte -= 1
            input("Teste sua sorte...\n")
            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
            
            if teste_da_sorte <= sorte :
                print("Você teve sorte!")
                print(textos.T39())
                resposta = int(input("Escolha: "))
                
                #Fugindo
                if resposta == 2 :
                    energia -= 2                            
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
                
                    if energiaFixa - energia >= 4 :
                        print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                        resposta = input("\nSim ou Não?").lower()
                        
                        if resposta == "sim" :
                            energia += 4
                            provisoes -=1
                
                #Ficando para batalhar
                elif resposta == 1 :
                    print("\nQue comece a batalha!")
                    #Matando a Mosca Gigante
                    print("Briga com a Mosca Gigante...\n")

                    while inimigos.inimigos["mosca_gigante"]["Energia"] > 0 :
                        ataqueInimigo = inimigos.inimigos["mosca_gigante"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                        inimigos.inimigos["mosca_gigante"]["Energia"] -= 4
                                        sorte -= 1
                                        print("A energia atual do inimigo é: ", inimigos.inimigos["mosca_gigante"]["Energia"])
                                        print(f"Sua sorte agora é {sorte}")

                                    else :
                                        print("Você não teve sorte, causou menos dano!")
                                        inimigos.inimigos["mosca_gigante"]["Energia"] -= 1
                                        sorte -= 1
                                        print("A energia atual do inimigo é:", inimigos.inimigos["mosca_gigante"]["Energia"])
                                        print(f"Sua sorte agora é {sorte}")
                                        
                                else :
                                    print("Você infelizmente não tem mais sorte")
                                    inimigos.inimigos["mosca_gigante"]["Energia"] -= 2
                                    print("\nA energia atual do inimigo é: ", inimigos.inimigos["mosca_gigante"]["Energia"])

                            else :
                                inimigos.inimigos["mosca_gigante"]["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", inimigos.inimigos["mosca_gigante"]["Energia"])

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
                    
                    print("\nParabéns você sobreviveu!")
                    
                    if energiaFixa - energia >= 4 :
                        print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                        resposta = input("\nSim ou Não?").lower()
                        
                        if resposta == "sim" :
                            energia += 4
                            provisoes -=1
                    
                    print(textos.T111())
    
    #Continuando pelo corredor (TAMBÉM DEPOS DE NÃO PEGAR A FACA OU FUGIR/BATALHAR COM A MOSCA) - TUDO EM CIMA CONCLUÍDO =============
    print(textos.T267())
    resposta = int(input("Escolha: "))
    
    #Seguindo para o oeste
    if resposta == 1 :
        print(textos.T352())
        escolha = int(input("Escolha: "))
        
        #Lutando contra o verme
        if escolha == 1 :
            print(textos.T254_2())
            resposta = int(input("Escolha: "))
            
            #Tendo certeza da luta
            if resposta == 1 :
                print(textos.T254())
                print("Que comece a luta!")
                
                #Matando o Verme da Rocha
                print("Briga com o Verme da Rocha...\n")

                while inimigos.inimigos["verme_rocha"]["Energia"] > 0 :
                    ataqueInimigo = inimigos.inimigos["verme_rocha"]["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                    inimigos.inimigos["verme_rocha"]["Energia"] -= 4
                                    sorte -= 1
                                    print("A energia atual do inimigo é: ", inimigos.inimigos["verme_rocha"]["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("Você não teve sorte, causou menos dano!")
                                    inimigos.inimigos["verme_rocha"]["Energia"] -= 1
                                    sorte -= 1
                                    print("A energia atual do inimigo é:", inimigos.inimigos["verme_rocha"]["Energia"])
                                    print(f"Sua sorte agora é {sorte}")
                                    
                            else :
                                print("Você infelizmente não tem mais sorte")
                                inimigos.inimigos["verme_rocha"]["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", inimigos.inimigos["verme_rocha"]["Energia"])

                        else :
                            inimigos.inimigos["verme_rocha"]["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", inimigos.inimigos["verme_rocha"]["Energia"])

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
                
                print("\nParabéns você sobreviveu!")
                
                if energiaFixa - energia >= 4 :
                    print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                    resposta = input("\nSim ou Não?").lower()
                    
                    if resposta == "sim" :
                        energia += 4
                        provisoes -=1
                
                print(textos.T76())
                escolha = int(input("Escolha: "))
                
                if escolha == 1 :
                    print(textos.T317())
                    energia = 0
            
            #Fugindo do verme
            elif resposta == 2 :
                print("Você fugiu e perdeu 2 pontos de energia!")
                energia -= 2                            
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
                
                if energiaFixa - energia >= 4 :
                    print(f"\nVocê tem {energia} pontos de energia, gostaria de usar uma provisão para recuperar 4 pontos?")
                    resposta = input("\nSim ou Não?").lower()
                    
                    if resposta == "sim" :
                        energia += 4
                        provisoes -=1
                
            #INDEPENDENTE DE LUTAR OU FUGIR, VOCÊ VAI CHEGAR AQUI
            print(textos.T117())
            resposta = int(input("Escolha: "))
            
            #Olhando no espelho
            if resposta == 1 :
                print(textos.T329())
                energia = 0
            
            #Não olhando o espelho
            elif resposta == 2 :
                print(textos.T135())
    
    #Seguindo para o leste
    print(textos.T68())
    resposta = int(input("Escolha: "))
    
    #Jogando o escudo por cima e depois pulando
    if resposta == 1 :
        print(textos.T271())
        escudo -= 1
        habilidade -= 1
    
    #Pular por cima carregando suas posses
    elif resposta == 2 :
        print(textos.T30())
        input("Teste sua sorte...\n")
        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
        
        #Tendo sorte
        if teste_da_sorte <= sorte :
            print(textos.T160())
        
        #Não tendo sorte
        else :
            print(textos.T319())
            print(textos.T285())
            habilidade -= 1
            energia -= 2
            objeto_redondo_pequeno += 1
    
    #Usando a corda
    elif resposta == 3 :
        print(textos.T212())
        print(textos.T285())
        habilidade -= 1
        energia -= 2
        objeto_redondo_pequeno += 1
    
    #Todos do 68 vem para aqui
    print(textos.T237())
    resposta = int(input("Escolha: "))
    
    #Abrindo a porta
    if resposta == 1 :
        print(textos.T12())
        escolha = int(input("Escolha: "))
        
        #Atacar com a espada
        if escolha == 2 :
            print(textos.T195())
            energia -= 1
        
        #Correr pela porta
        elif escolha == 3 :
            print(textos.T250())
            resposta = int(input("Escolha: "))
            
            #Continuar correndo
            if resposta == 1 :
                print(textos.T44())
                energia = 0
            
            elif resposta == 3 :
                print(textos.T195())
                energia -= 1
        
        #Esperando a pergunta
        print(textos.T382())
        resposta = int(input("Escolha: "))
        
        #50KG
        if resposta == 1 :
            print(textos.T144())
            print(textos.T85())
            energia = 0
        
        #75KG
        elif resposta == 2 :
            print(textos.T227())
            print(textos.T85())
            energia = 0
        
        #100KG
        elif resposta == 3 :
            print(textos.T391())
            habilidade += 1
            energia += 1
            sorte += 1
            
    #PARA CIMA ESTÁ TUDO COMPLETO, ESTAREI ALTERANDO SÓ ABAIXO AGORA ================================================================================
    #Não entrando na porta e continuando/Depois de sair
    print(textos.T100())
    resposta = int(input("Escolha: "))
    
    #Abrindo a porta
    if resposta == 1 :
        print(textos.T87())
        print(textos.T381())
    
    #Continuando no corredor
    print(textos.T217())
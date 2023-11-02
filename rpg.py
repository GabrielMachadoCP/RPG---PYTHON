# Ana Zerlin        RM 98065
# Bianca Dancs      RM 551645
# Gabriel Pimentel  RM 99880
# Hellen Assis      RM 98284

#LINHA QUE ESTOU TRABALHANDO NO MOMENTO: 3100
#O CÓDIGO COMEÇA NA LINHA: 40
#Fazer 3030 e 3043!!!

#Imports
import random

import ficha
import textos
import inimigos

#Variáveis de auxílio (auxílio mais para quem está fazendo o código do que para o código em si, só para deixar claro)
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
anel_de_ouro = 0 #ESSE AQUI É O ANEL DOS DESEJOS
objeto_redondo_pequeno = 0
marreta_madeira = 0
espigoes_ferro = 0
bola_madeira = 0
topazio = 0
cranio = 0


#Variáveis adicionadas para auxiliar mais para frente
beber = ""

#O CÓDIGO COMEÇA AQUI
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
provisoes = ficha["Provisoes"]

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
                    #Gritar > MORTE
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

                #Inicializando as variáveis para a batalha
                hobgoblin1_1 = inimigos.inimigos["hobgoblin1"]
                hobgoblin2_1 = inimigos.inimigos["hobgoblin2"]
                
                #Matando o primeiro Hobgoblin
                print("Briga com o Hobgoblin Nº1...\n")
                
                while hobgoblin1_1["Energia"] > 0 :
                    ataqueInimigo = hobgoblin1_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                sorte -= 1

                                if teste_da_sorte <= sorte :
                                    print("\nVocê teve sorte! Causou o dobro de dano")
                                    hobgoblin1_1["Energia"] -= 4
                                    sorte -= 1
                                    print("A energia atual do inimigo é: ", hobgoblin1_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, causou menos dano!")
                                    hobgoblin1_1["Energia"] -= 1
                                    sorte -= 1
                                    print("A energia atual do inimigo é:", hobgoblin1_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Infelizmente você não tem mais sorte")
                                hobgoblin1_1["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", hobgoblin1_1["Energia"])

                        else :
                            hobgoblin1_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", hobgoblin1_1["Energia"])

                    #Tomando dano
                    else :
                        print("Quer testar sua sorte para receber menos dano?")
                        testarSorte = input().lower()

                        if testarSorte == "sim" :
                            if sorte > 0 :
                                input("Jogue os dados para testar sua sorte...\n")
                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                if teste_da_sorte <= sorte :
                                    print("\nVocê teve sorte! Recebeu menos dano!")
                                    energia -= 1
                                    sorte -= 1
                                    print(f"Sua energia atual é {energia}")
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, recebeu mais dano!")
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

                while hobgoblin2_1["Energia"] > 0 :
                    ataqueInimigo = hobgoblin2_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                    print("\nVocê teve sorte! Causou o dobro de dano")
                                    hobgoblin2_1["Energia"] -= 4
                                    sorte -= 1
                                    print("A energia atual do inimigo é: ", hobgoblin2_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, causou menos dano!")
                                    hobgoblin2_1["Energia"] -= 1
                                    sorte -= 1
                                    print("A energia atual do inimigo é:", hobgoblin2_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Infelizmente você não tem mais sorte")
                                hobgoblin2_1["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", hobgoblin2_1["Energia"])

                        else :
                            hobgoblin2_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", hobgoblin2_1["Energia"])

                    #Tomando dano
                    else :
                        print("Quer testar sua sorte para receber menos dano?")
                        testarSorte = input().lower()

                        if testarSorte == "sim" :
                            if sorte > 0 :
                                input("Jogue os dados para testar sua sorte...\n")
                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                if teste_da_sorte <= sorte :
                                    print("\nVocê teve sorte! Recebeu menos dano!")
                                    energia -= 1
                                    sorte -= 1
                                    print(f"Sua energia atual é {energia}")
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, recebeu mais dano!")
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
                    input("\nTeste sua sorte...")
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
                            sorte -= 1

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
                
                #Inicializando as variáveis para a batalha
                hobgoblin_1 = inimigos.inimigos["hobgoblin"]
                
                #Matando o Hobgoblin restante
                print("Briga com o Hobgoblin restante...\n")
                
                while hobgoblin_1["Energia"] > 0 :
                    ataqueInimigo = hobgoblin_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                    print("\nVocê teve sorte! Causou o dobro de dano")
                                    hobgoblin_1["Energia"] -= 4
                                    sorte -= 1
                                    print("A energia atual do inimigo é: ", hobgoblin_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, causou menos dano!")
                                    hobgoblin_1["Energia"] -= 1
                                    sorte -= 1
                                    print("A energia atual do inimigo é:", hobgoblin_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                            else :
                                print("Infelizmente você não tem mais sorte")
                                hobgoblin_1["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", hobgoblin_1["Energia"])

                        else :
                            hobgoblin_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", hobgoblin_1["Energia"])

                    #Tomando dano
                    else :
                        print("Quer testar sua sorte para receber menos dano?")
                        testarSorte = input().lower()

                        if testarSorte == "sim" :
                            if sorte > 0 :
                                input("Jogue os dados para testar sua sorte...\n")
                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                if teste_da_sorte <= sorte :
                                    print("\nVocê teve sorte! Recebeu menos dano!")
                                    energia -= 1
                                    sorte -= 1
                                    print(f"Sua energia atual é {energia}")
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, recebeu mais dano!")
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
                    input("\nTeste sua sorte...")
                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                    sorte -= 1

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
                            sorte -= 1

                            #Não tendo sorte de novo > MORTE
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
                print(textos.T223())
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
            
            #Inicializando as variáveis para a batalha
            homem_caverna_1 = inimigos.inimigos["homem_caverna"]
            
            #Matando o Homem da Caverna
            print("Briga com o Homem da Caverna...\n")

            while homem_caverna_1["Energia"] > 0 :
                ataqueInimigo = homem_caverna_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                print("\nVocê teve sorte! Causou o dobro de dano")
                                homem_caverna_1["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", homem_caverna_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, causou menos dano!")
                                homem_caverna_1["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", homem_caverna_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            homem_caverna_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", homem_caverna_1["Energia"])

                    else :
                        homem_caverna_1["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", homem_caverna_1["Energia"])

                #Tomando dano
                else :
                    print("Quer testar sua sorte para receber menos dano?")
                    testarSorte = input().lower()

                    if testarSorte == "sim" :
                        if sorte > 0 :
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("\nVocê teve sorte! Recebeu menos dano!")
                                energia -= 1
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, recebeu mais dano!")
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
            print(textos.T25())
        
        #Se não bebeu o líquido
        elif beber == "não" :
            print(textos.T242())
            input("Jogue os dados...🎲")
            sobrevive = random.randint(1,6) + random.randint(1,6)
            
            if sobrevive <= habilidade :
                print(textos.T48())
            
            #Falhar no teste > MORTE
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
            
            #Inicializando as variáveis para a batalha
            orca1_1 = inimigos.inimigos["orca1"]
            orca2_1 = inimigos.inimigos["orca2"]
            
            #Matando a primeira Orca
            print("Briga com a Orca Nº1...\n")

            while orca1_1["Energia"] > 0 :
                ataqueInimigo = orca1_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                print("\nVocê teve sorte! Causou o dobro de dano")
                                orca1_1["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", orca1_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, causou menos dano!")
                                orca1_1["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", orca1_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            orca1_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", orca1_1["Energia"])

                    else :
                        orca1_1["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", orca1_1["Energia"])

                #Tomando dano
                else :
                    print("Quer testar sua sorte para receber menos dano?")
                    testarSorte = input().lower()

                    if testarSorte == "sim" :
                        if sorte > 0 :
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("\nVocê teve sorte! Recebeu menos dano!")
                                energia -= 1
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, recebeu mais dano!")
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

            while orca2_1["Energia"] > 0 :
                ataqueInimigo = orca2_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                print("\nVocê teve sorte! Causou o dobro de dano")
                                orca2_1["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", orca2_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, causou menos dano!")
                                orca2_1["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", orca2_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            orca2_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", orca2_1["Energia"])

                    else :
                        orca2_1["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", orca2_1["Energia"])

                #Tomando dano
                else :
                    print("Quer testar sua sorte para receber menos dano?")
                    testarSorte = input().lower()

                    if testarSorte == "sim" :
                        if sorte > 0 :
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("\nVocê teve sorte! Recebeu menos dano!")
                                energia -= 1
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, recebeu mais dano!")
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
            
            #Inicializando as variáveis para a batalha
            orca1_1 = inimigos.inimigos["orca1"]
            orca2_1 = inimigos.inimigos["orca2"]
        
            #Matando a primeira Orca
            print("Briga com a Orca Nº1...\n")

            while orca1_1["Energia"] > 0 :
                ataqueInimigo = orca1_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                print("\nVocê teve sorte! Causou o dobro de dano")
                                orca1_1["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", orca1_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, causou menos dano!")
                                orca1_1["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", orca1_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            orca1_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", orca1_1["Energia"])

                    else :
                        orca1_1["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", orca1_1["Energia"])

                #Tomando dano
                else :
                    print("Quer testar sua sorte para receber menos dano?")
                    testarSorte = input().lower()

                    if testarSorte == "sim" :
                        if sorte > 0 :
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("\nVocê teve sorte! Recebeu menos dano!")
                                energia -= 1
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, recebeu mais dano!")
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

            while orca2_1["Energia"] > 0 :
                ataqueInimigo = orca2_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                print("\nVocê teve sorte! Causou o dobro de dano")
                                orca2_1["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", orca2_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, causou menos dano!")
                                orca2_1["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", orca2_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            orca2_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", orca2_1["Energia"])

                    else :
                        orca2_1["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", orca2_1["Energia"])

                #Tomando dano
                else :
                    print("Quer testar sua sorte para receber menos dano?")
                    testarSorte = input().lower()

                    if testarSorte == "sim" :
                        if sorte > 0 :
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("\nVocê teve sorte! Recebeu menos dano!")
                                energia -= 1
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, recebeu mais dano!")
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
            
            #Inicializando as variáveis para a batalha
            orca1_1 = inimigos.inimigos["orca1"]
            orca2_1 = inimigos.inimigos["orca2"]
            
            #Matando a primeira Orca
            print("Briga com a Orca Nº1...\n")

            while orca1_1["Energia"] > 0 :
                ataqueInimigo = orca1_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                print("\nVocê teve sorte! Causou o dobro de dano")
                                orca1_1["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", orca1_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, causou menos dano!")
                                orca1_1["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", orca1_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            orca1_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", orca1_1["Energia"])

                    else :
                        orca1_1["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", orca1_1["Energia"])

                #Tomando dano
                else :
                    print("Quer testar sua sorte para receber menos dano?")
                    testarSorte = input().lower()

                    if testarSorte == "sim" :
                        if sorte > 0 :
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("\nVocê teve sorte! Recebeu menos dano!")
                                energia -= 1
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, recebeu mais dano!")
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

            while orca2_1["Energia"] > 0 :
                ataqueInimigo = orca2_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                print("\nVocê teve sorte! Causou o dobro de dano")
                                orca2_1["Energia"] -= 4
                                sorte -= 1
                                print("A energia atual do inimigo é: ", orca2_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, causou menos dano!")
                                orca2_1["Energia"] -= 1
                                sorte -= 1
                                print("A energia atual do inimigo é:", orca2_1["Energia"])
                                print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Infelizmente você não tem mais sorte")
                            orca2_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", orca2_1["Energia"])

                    else :
                        orca2_1["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", orca2_1["Energia"])

                #Tomando dano
                else :
                    print("Quer testar sua sorte para receber menos dano?")
                    testarSorte = input().lower()

                    if testarSorte == "sim" :
                        if sorte > 0 :
                            input("Jogue os dados para testar sua sorte...\n")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                            if teste_da_sorte <= sorte :
                                print("\nVocê teve sorte! Recebeu menos dano!")
                                energia -= 1
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, recebeu mais dano!")
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
                            input("\nTeste sua sorte...")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                            sorte -= 1
                            
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
                        input("\nTeste sua sorte...")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                        sorte -= 1
                        
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
                            input("\nTeste sua sorte...")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                            sorte -= 1
                            
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
                    input("\nTeste sua sorte...")
                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                    sorte -= 1
                    
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
                            input("\nTeste sua sorte...")
                            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                            sorte -= 1
                            
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
                        input("\nTeste sua sorte...")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                        sorte -= 1
                        
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

            #Pegar a joia da direita > MORTE
            if resposta == 2 :
                print(textos.T34())
                energia = 0

            #Pega a joia da esquerda
            elif resposta == 1 :
                print(textos.T151())
                
                #Inicializando as variáveis para a batalha
                guardiao1_1 = inimigos.inimigos["guardiao1"]
                guardiao2_1 = inimigos.inimigos["guardiao2"]

                #Matando o primeiro guardião
                print("Briga com o Guardião Voador Nº1...\n")

                while guardiao1_1["Energia"] > 0 :
                    ataqueInimigo = guardiao1_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                    print("\nVocê teve sorte! Causou o dobro de dano")
                                    guardiao1_1["Energia"] -= 4
                                    sorte -= 1
                                    print("A energia atual do inimigo é: ", guardiao1_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, causou menos dano!")
                                    guardiao1_1["Energia"] -= 1
                                    sorte -= 1
                                    print("A energia atual do inimigo é:", guardiao1_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")
                            
                            else :
                                print("Você infelizmente não tem mais sorte")
                                guardiao1_1["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", guardiao1_1["Energia"])

                        else :
                            guardiao1_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", guardiao1_1["Energia"])

                    #Tomando dano
                    else :
                        print("Quer testar sua sorte para receber menos dano?")
                        testarSorte = input().lower()

                        if testarSorte == "sim" :
                            if sorte > 0 :
                                input("Jogue os dados para testar sua sorte...\n")
                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                if teste_da_sorte <= sorte :
                                    print("\nVocê teve sorte! Recebeu menos dano!")
                                    energia -= 1
                                    sorte -= 1
                                    print(f"Sua energia atual é {energia}")
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, recebeu mais dano!")
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

                while guardiao2_1["Energia"] > 0 :
                    ataqueInimigo = guardiao2_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                    print("\nVocê teve sorte! Causou o dobro de dano")
                                    guardiao2_1["Energia"] -= 4
                                    sorte -= 1
                                    print("A energia atual do inimigo é: ", guardiao2_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, causou menos dano!")
                                    guardiao2_1["Energia"] -= 1
                                    sorte -= 1
                                    print("A energia atual do inimigo é:", guardiao2_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")
                                    
                            else :
                                print("Você infelizmente não tem mais sorte")
                                guardiao2_1["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", guardiao2_1["Energia"])

                        else :
                            guardiao2_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", guardiao2_1["Energia"])

                    #Tomando dano
                    else :
                        print("Quer testar sua sorte para receber menos dano?")
                        testarSorte = input().lower()

                        if testarSorte == "sim" :
                            if sorte > 0 :
                                input("Jogue os dados para testar sua sorte...\n")
                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                if teste_da_sorte <= sorte :
                                    print("\nVocê teve sorte! Recebeu menos dano!")
                                    energia -= 1
                                    sorte -= 1
                                    print(f"Sua energia atual é {energia}")
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, recebeu mais dano!")
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

                #Pegando a joia da direita depois de pegar a da esquerda > MORTE
                if resposta == 1 :
                    print(textos.T34())
                    energia = 0

                #Descendo do ídolo
                elif resposta == 2 :
                    print(textos.T89())
                    #Teste a sua sorte para tirar a corda
                    sorte -= 1
                    input("\nTeste sua sorte...")
                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                    #Tendo sorte
                    if teste_da_sorte <= sorte :
                        print("\nVocê teve sorte!")
                        print(textos.T54())
                        corda += 1

                    #Não tendo sorte
                    else:
                        print("\nVocê não teve sorte!")
                        print(textos.T261())
        
        #Não possui corda - CONCLUÍDO
        elif corda == 0 :
            print(textos.T186())
            #Testando a sorte
            input("\nTeste sua sorte...")
            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
            sorte -= 1

            #Não tendo sorte
            if teste_da_sorte >= sorte :
                print("\nVocê não teve sorte!")
                print(textos.T358())
                #Você cai e perde energia
                energia -= 2
            
            else :
                print("\nVocê teve sorte!")
                print(textos.T260())
                resposta = int(input("Escolha: "))
                        
                #Arrancando o olho direito > MORTE
                if resposta == 2 :
                    print(textos.T140())
                    energia = 0

                else :
                    print(textos.T166())
                    
                    #Inicializando as variáveis para a batalha
                    guardiao1_1 = inimigos.inimigos["guardiao1"]
                    guardiao2_1 = inimigos.inimigos["guardiao2"]

                    #Matando o primeiro guardião
                    print("Briga com o Guardião Voador Nº1...\n")

                    while guardiao1_1["Energia"] > 0 :
                        ataqueInimigo = guardiao1_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                        print("\nVocê teve sorte! Causou o dobro de dano")
                                        guardiao1_1["Energia"] -= 4
                                        sorte -= 1
                                        print("A energia atual do inimigo é: ", guardiao1_1["Energia"])
                                        print(f"Sua sorte agora é {sorte}")

                                    else :
                                        print("\nVocê não teve sorte, causou menos dano!")
                                        guardiao1_1["Energia"] -= 1
                                        sorte -= 1
                                        print("A energia atual do inimigo é:", guardiao1_1["Energia"])
                                        print(f"Sua sorte agora é {sorte}")
                                
                                else :
                                    print("Você infelizmente não tem mais sorte")
                                    guardiao1_1["Energia"] -= 2
                                    print("\nA energia atual do inimigo é: ", guardiao1_1["Energia"])

                            else :
                                guardiao1_1["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", guardiao1_1["Energia"])

                        #Tomando dano
                        else :
                            print("Quer testar sua sorte para receber menos dano?")
                            testarSorte = input().lower()

                            if testarSorte == "sim" :
                                if sorte > 0 :
                                    input("Jogue os dados para testar sua sorte...\n")
                                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                    if teste_da_sorte <= sorte :
                                        print("\nVocê teve sorte! Recebeu menos dano!")
                                        energia -= 1
                                        sorte -= 1
                                        print(f"Sua energia atual é {energia}")
                                        print(f"Sua sorte agora é {sorte}")

                                    else :
                                        print("\nVocê não teve sorte, recebeu mais dano!")
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

                    while guardiao2_1["Energia"] > 0 :
                        ataqueInimigo = guardiao2_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                        print("\nVocê teve sorte! Causou o dobro de dano")
                                        guardiao2_1["Energia"] -= 4
                                        sorte -= 1
                                        print("A energia atual do inimigo é: ", guardiao2_1["Energia"])
                                        print(f"Sua sorte agora é {sorte}")

                                    else :
                                        print("\nVocê não teve sorte, causou menos dano!")
                                        guardiao2_1["Energia"] -= 1
                                        sorte -= 1
                                        print("A energia atual do inimigo é:", guardiao2_1["Energia"])
                                        print(f"Sua sorte agora é {sorte}")
                                        
                                else :
                                    print("Você infelizmente não tem mais sorte")
                                    guardiao2_1["Energia"] -= 2
                                    print("\nA energia atual do inimigo é: ", guardiao2_1["Energia"])

                            else :
                                guardiao2_1["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", guardiao2_1["Energia"])

                        #Tomando dano
                        else :
                            print("Quer testar sua sorte para receber menos dano?")
                            testarSorte = input().lower()

                            if testarSorte == "sim" :
                                if sorte > 0 :
                                    input("Jogue os dados para testar sua sorte...\n")
                                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                    if teste_da_sorte <= sorte :
                                        print("\nVocê teve sorte! Recebeu menos dano!")
                                        energia -= 1
                                        sorte -= 1
                                        print(f"Sua energia atual é {energia}")
                                        print(f"Sua sorte agora é {sorte}")

                                    else :
                                        print("\nVocê não teve sorte, recebeu mais dano!")
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

                    #Retirando o olho direito > MORTE
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
            
            #Não passando no teste > MORTE
            else :
                print(textos.T17())
                energia = 0
        
        #Falando que o mestre dele é um verme
        elif escolha == 2 :
            print(textos.T251())
            anel_de_ouro += 1 #ESSE AQUI É O ANEL DOS DESEJOS
    
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
            input("\nTeste sua sorte...")
            teste_da_sorte = random.randint(1,6) + random.randint(1,6)
            
            if teste_da_sorte <= sorte :
                print("\nVocê teve sorte!")
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
                                print("\nVocê teve sorte! Recebeu menos dano!")
                                energia -= 1
                                sorte -= 1
                                print(f"Sua energia atual é {energia}")
                                print(f"Sua sorte agora é {sorte}")

                            else :
                                print("\nVocê não teve sorte, recebeu mais dano!")
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
                    
                    #Inicializando as variáveis para a batalha
                    mosca_gigante_1 = inimigos.inimigos["mosca_gigante"]

                    #Matando a Mosca Gigante
                    print("Briga com a Mosca Gigante...\n")

                    while mosca_gigante_1["Energia"] > 0 :
                        ataqueInimigo = mosca_gigante_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                        print("\nVocê teve sorte! Causou o dobro de dano")
                                        mosca_gigante_1["Energia"] -= 4
                                        sorte -= 1
                                        print("A energia atual do inimigo é: ", mosca_gigante_1["Energia"])
                                        print(f"Sua sorte agora é {sorte}")

                                    else :
                                        print("\nVocê não teve sorte, causou menos dano!")
                                        mosca_gigante_1["Energia"] -= 1
                                        sorte -= 1
                                        print("A energia atual do inimigo é:", mosca_gigante_1["Energia"])
                                        print(f"Sua sorte agora é {sorte}")
                                        
                                else :
                                    print("Você infelizmente não tem mais sorte")
                                    mosca_gigante_1["Energia"] -= 2
                                    print("\nA energia atual do inimigo é: ", mosca_gigante_1["Energia"])

                            else :
                                mosca_gigante_1["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", mosca_gigante_1["Energia"])

                        #Tomando dano
                        else :
                            print("Quer testar sua sorte para receber menos dano?")
                            testarSorte = input().lower()

                            if testarSorte == "sim" :
                                if sorte > 0 :
                                    input("Jogue os dados para testar sua sorte...\n")
                                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                    if teste_da_sorte <= sorte :
                                        print("\nVocê teve sorte! Recebeu menos dano!")
                                        energia -= 1
                                        sorte -= 1
                                        print(f"Sua energia atual é {energia}")
                                        print(f"Sua sorte agora é {sorte}")

                                    else :
                                        print("\nVocê não teve sorte, recebeu mais dano!")
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
                
                #Inicializando as variáveis para a batalha
                verme_rocha_1 = inimigos.inimigos["verme_rocha"]
                
                #Matando o Verme da Rocha
                print("Briga com o Verme da Rocha...\n")

                while verme_rocha_1["Energia"] > 0 :
                    ataqueInimigo = verme_rocha_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                    print("\nVocê teve sorte! Causou o dobro de dano")
                                    verme_rocha_1["Energia"] -= 4
                                    sorte -= 1
                                    print("A energia atual do inimigo é: ", verme_rocha_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, causou menos dano!")
                                    verme_rocha_1["Energia"] -= 1
                                    sorte -= 1
                                    print("A energia atual do inimigo é:", verme_rocha_1["Energia"])
                                    print(f"Sua sorte agora é {sorte}")
                                    
                            else :
                                print("Você infelizmente não tem mais sorte")
                                verme_rocha_1["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", verme_rocha_1["Energia"])

                        else :
                            verme_rocha_1["Energia"] -= 2
                            print("\nA energia atual do inimigo é: ", verme_rocha_1["Energia"])

                    #Tomando dano
                    else :
                        print("Quer testar sua sorte para receber menos dano?")
                        testarSorte = input().lower()

                        if testarSorte == "sim" :
                            if sorte > 0 :
                                input("Jogue os dados para testar sua sorte...\n")
                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                if teste_da_sorte <= sorte :
                                    print("\nVocê teve sorte! Recebeu menos dano!")
                                    energia -= 1
                                    sorte -= 1
                                    print(f"Sua energia atual é {energia}")
                                    print(f"Sua sorte agora é {sorte}")

                                else :
                                    print("\nVocê não teve sorte, recebeu mais dano!")
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
                
                #Explorando o buraco de broca > MORTE
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
                            print("\nVocê teve sorte! Recebeu menos dano!")
                            energia -= 1
                            sorte -= 1
                            print(f"Sua energia atual é {energia}")
                            print(f"Sua sorte agora é {sorte}")

                        else :
                            print("\nVocê não teve sorte, recebeu mais dano!")
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
            
            #Olhando no espelho > MORTE
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
        input("\nTeste sua sorte...")
        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
        sorte -= 1
        
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
            
            #Continuar correndo  > MORTE
            if resposta == 1 :
                print(textos.T44())
                energia = 0
            
            #Atacando com a espada e tendo que escutar o velho
            elif resposta == 3 :
                print(textos.T195())
                energia -= 1
        
        #Esperando a pergunta
        print(textos.T382())
        resposta = int(input("Escolha: "))
        
        #50KG  > MORTE
        if resposta == 1 :
            print(textos.T144())
            print(textos.T85())
            energia = 0
        
        #75KG  > MORTE
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
            
    #Não entrando na porta e continuando/Depois de sair
    print(textos.T100())
    resposta = int(input("Escolha: "))
    
    #Abrindo a porta
    if resposta == 1 :
        print(textos.T87())
        print(textos.T381())
    
    #Continuando no corredor
    #Tendo um escudo
    if escudo != 0 :
        print(textos.T217())
        escudo -= 1
        habilidade -= 1
    
    #Não tendo escudo
    elif escudo == 0 :
        print(textos.T217_2())
    
    print(textos.T36())
    input("Jogue os dados...🎲")
    teste_da_habilidade = random.randint(1,6) + random.randint(1,6)

    #Teste sendo menor que a habiliadade e a energia
    if teste_da_habilidade <= habilidade and teste_da_habilidade <= energia :
        print(textos.T340())
    
    #Teste maior que qualquer um desses > MORTE
    else :
        print(textos.T7())
        energia = 0
    
    print(textos.T381())
    escolha = int(input("Escolha: "))

    #Pegando o pergaminho
    if escolha == 1 :
        print(textos.T331())
        
        #Inicializando as variáveis para a batalha
        guerreiro_esqueleto_1 = inimigos.inimigos["guerreiro_esqueleto"]

        #Matando o Guerreiro Esqueleto
        print("Briga com o Guerreiro Esqueleto...\n")

        while guerreiro_esqueleto_1["Energia"] > 0 :
            ataqueInimigo = guerreiro_esqueleto_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                            print("\nVocê teve sorte! Causou o dobro de dano")
                            guerreiro_esqueleto_1["Energia"] -= 4
                            sorte -= 1
                            print("A energia atual do inimigo é: ", guerreiro_esqueleto_1["Energia"])
                            print(f"Sua sorte agora é {sorte}")

                        else :
                            print("\nVocê não teve sorte, causou menos dano!")
                            guerreiro_esqueleto_1["Energia"] -= 1
                            sorte -= 1
                            print("A energia atual do inimigo é:", guerreiro_esqueleto_1["Energia"])
                            print(f"Sua sorte agora é {sorte}")
                            
                    else :
                        print("Você infelizmente não tem mais sorte")
                        guerreiro_esqueleto_1["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", guerreiro_esqueleto_1["Energia"])

                else :
                    guerreiro_esqueleto_1["Energia"] -= 2
                    print("\nA energia atual do inimigo é: ", guerreiro_esqueleto_1["Energia"])

            #Tomando dano
            else :
                print("Quer testar sua sorte para receber menos dano?")
                testarSorte = input().lower()

                if testarSorte == "sim" :
                    if sorte > 0 :
                        input("Jogue os dados para testar sua sorte...\n")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                        if teste_da_sorte <= sorte :
                            print("\nVocê teve sorte! Recebeu menos dano!")
                            energia -= 1
                            sorte -= 1
                            print(f"Sua energia atual é {energia}")
                            print(f"Sua sorte agora é {sorte}")

                        else :
                            print("\nVocê não teve sorte, recebeu mais dano!")
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
        
        print(textos.T71())

    #Caminhando atá a alcova
    print(textos.T128())
    resposta = int(input("Escolha: "))

    #Parando para comer alguns cogumelos > MORTE
    if resposta == 2 :
        print(textos.T233())
        energia = 0

    #Continua a andar
    print(textos.T35())
    escolha = int(input("Escolha: "))

    #Batendo na porta > MORTE
    if escolha == 1 :
        print(textos.T333())
        energia = 0
    
    print(textos.T124())
    
    #Inicializando as variáveis para a batalha
    goblin1_1 = inimigos.inimigos["goblin1"]
    goblin2_1 = inimigos.inimigos["goblin2"]

    #Brigando com os goblins
    while goblin1_1["Energia"] > 0 and goblin2_1["Energia"] > 0 :
        print("\nQual Goblin você vai querer atacar primeiro? (1) ou (2)")
        resposta = int(input("Escolha: "))

        #Batendo no 1º Goblin
        if resposta == 1 :
            print("Briga com o Goblin Nº1...\n")
            ataqueInimigo = goblin1_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                            print("\nVocê teve sorte! Causou o dobro de dano")
                            goblin1_1["Energia"] -= 4
                            sorte -= 1
                            print("A energia atual do inimigo é: ", goblin1_1["Energia"])
                            print(f"Sua sorte agora é {sorte}")

                        else :
                            print("\nVocê não teve sorte, causou menos dano!")
                            goblin1_1["Energia"] -= 1
                            sorte -= 1
                            print("A energia atual do inimigo é:", goblin1_1["Energia"])
                            print(f"Sua sorte agora é {sorte}")
                    
                    else :
                        print("Você infelizmente não tem mais sorte")
                        goblin1_1["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", goblin1_1["Energia"])

                else :
                    goblin1_1["Energia"] -= 2
                    print("\nA energia atual do inimigo é: ", goblin1_1["Energia"])

            #Tomando dano
            else :
                print("Quer testar sua sorte para receber menos dano?")
                testarSorte = input().lower()

                if testarSorte == "sim" :
                    if sorte > 0 :
                        input("Jogue os dados para testar sua sorte...\n")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                        if teste_da_sorte <= sorte :
                            print("\nVocê teve sorte! Recebeu menos dano!")
                            energia -= 1
                            sorte -= 1
                            print(f"Sua energia atual é {energia}")
                            print(f"Sua sorte agora é {sorte}")

                        else :
                            print("\nVocê não teve sorte, recebeu mais dano!")
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

            #Defendendo do segundo
            print("Tentando se defender do Goblin Nº2...\n")

            ataqueInimigo = goblin2_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
            meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)

            print(f"O ataque do inimigo foi de: {ataqueInimigo}")
            input("Jogue os dados...🎲")
            print(f"O seu ataque foi de: {meuAtaque}\n")

            #Evitando o dano
            if meuAtaque > ataqueInimigo :
                print("Você conseguiu se defender, não tomou dano!")

            #Tomando dano
            else :
                print("Quer testar sua sorte para receber menos dano?")
                testarSorte = input().lower()

                if testarSorte == "sim" :
                    if sorte > 0 :
                        input("Jogue os dados para testar sua sorte...\n")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                        if teste_da_sorte <= sorte :
                            print("\nVocê teve sorte! Recebeu menos dano!")
                            energia -= 1
                            sorte -= 1
                            print(f"Sua energia atual é {energia}")
                            print(f"Sua sorte agora é {sorte}")

                        else :
                            print("\nVocê não teve sorte, recebeu mais dano!")
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
    
        #Batendo no 2º Goblin
        elif resposta == 2 :
            print("Briga com o Goblin Nº2...\n")
            ataqueInimigo = goblin2_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                            goblin2_1["Energia"] -= 4
                            sorte -= 1
                            print("A energia atual do inimigo é: ", goblin2_1["Energia"])
                            print(f"Sua sorte agora é {sorte}")

                        else :
                            print("Você não teve sorte, causou menos dano!")
                            goblin2_1["Energia"] -= 1
                            sorte -= 1
                            print("A energia atual do inimigo é:", goblin2_1["Energia"])
                            print(f"Sua sorte agora é {sorte}")
                    
                    else :
                        print("Você infelizmente não tem mais sorte")
                        goblin2_1["Energia"] -= 2
                        print("\nA energia atual do inimigo é: ", goblin2_1["Energia"])

                else :
                    goblin2_1["Energia"] -= 2
                    print("\nA energia atual do inimigo é: ", goblin2_1["Energia"])

            #Tomando dano
            else :
                print("Quer testar sua sorte para receber menos dano?")
                testarSorte = input().lower()

                if testarSorte == "sim" :
                    if sorte > 0 :
                        input("Jogue os dados para testar sua sorte...\n")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                        if teste_da_sorte <= sorte :
                            print("\nVocê teve sorte! Recebeu menos dano!")
                            energia -= 1
                            sorte -= 1
                            print(f"Sua energia atual é {energia}")
                            print(f"Sua sorte agora é {sorte}")

                        else :
                            print("\nVocê não teve sorte, recebeu mais dano!")
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

            #Defendendo do primeiro
            print("Tentando se defender do Goblin Nº1...\n")

            ataqueInimigo = goblin1_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
            meuAtaque = habilidade + random.randint(1,6) + random.randint(1,6)

            print(f"O ataque do inimigo foi de: {ataqueInimigo}")
            input("Jogue os dados...🎲")
            print(f"O seu ataque foi de: {meuAtaque}\n")

            #Evitando o dano
            if meuAtaque > ataqueInimigo :
                print("Você conseguiu se defender, não tomou dano!")

            #Tomando dano
            else :
                print("Quer testar sua sorte para receber menos dano?")
                testarSorte = input().lower()

                if testarSorte == "sim" :
                    if sorte > 0 :
                        input("Jogue os dados para testar sua sorte...\n")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                        if teste_da_sorte <= sorte :
                            print("\nVocê teve sorte! Recebeu menos dano!")
                            energia -= 1
                            sorte -= 1
                            print(f"Sua energia atual é {energia}")
                            print(f"Sua sorte agora é {sorte}")

                        else :
                            print("\nVocê não teve sorte, recebeu mais dano!")
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
    
    print(textos.T81())
    escolha = int(input("Escolha: "))
    
    #Abrindo o armário
    if escolha == 1 :
        print(textos.T307())
        marreta_madeira += 1
        espigoes_ferro += 10
        respostaT307 = int(input("Escolha: "))
    
    #Abrindo a porta para o oeste
    elif escolha == 2 or respostaT307 == 1 :
        print(textos.T263())
        resposta = int(input("Escolha: "))

        #Abrindo a porta
        if resposta == 1 :
            print(textos.T153())
            escolha = int(input("Escolha: "))

            #Entrando no aposento e pegando o crânio
            if escolha == 1 :
                print(textos.T390())
                topazio += 2
                sorte -= 1
                resposta = int(input("Escolha: "))

                #Engatinhando para fora do aposento com o crânio
                if resposta == 1 :
                    print(textos.T15())
                    cranio += 1

                #Colocando o crânio de volta antes de sair do aposento
                elif resposta == 2 :
                    print(textos.T204())
                    input("\nTeste sua sorte...")
                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                    sorte -= 1

                    #Tendo sorte
                    if teste_da_sorte <= sorte :
                        print("\nVocê teve sorte!")
                        print(textos.T131())
                    
                    #Não tendo sorte
                    else :
                        print("\nVocê não teve sorte!")
                        print(textos.T199())
                        dardos = random.randint(1,6)
                        energia -= dardos * 2
                        sorte -= 1

            #Jogando a bola de madeira da porta no crânio
            elif escolha == 2 :
                print(textos.T371())
                input("Jogue os dados...🎲")
                teste_da_habilidade = random.randint(1,6) + random.randint(1,6)

                #Passando no teste de habilidade
                if teste_da_habilidade <= habilidade :
                    print(textos.T273())
                    topazio += 2
                    resposta = int(input("Escolha: "))

                    #Engatinhando para fora do aposento com o crânio
                    if resposta == 1 :
                        print(textos.T15())
                        cranio += 1

                    #Colocando o crânio de volta antes de sair do aposento
                    elif resposta == 2 :
                        print(textos.T204())
                        input("\nTeste sua sorte...")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                        sorte -= 1

                        #Tendo sorte
                        if teste_da_sorte <= sorte :
                            print("\nVocê teve sorte!")
                            print(textos.T131())
                        
                        #Não tendo sorte
                        else :
                            print("\nVocê não teve sorte!")
                            print(textos.T199())
                            dardos = random.randint(1,6)
                            energia -= dardos * 2
                            sorte -= 1
                    
                #Não passando no teste de habilidade
                else :
                    print(textos.T113()),
                    resposta = int(input("Escolha: "))

                    #Testando novamente depois de uma falha
                    if resposta == 1 :
                        print(textos.T371())
                        input("Jogue os dados...🎲")
                        teste_da_habilidade = random.randint(1,6) + random.randint(1,6)

                        #Passando no teste de habilidade
                        if teste_da_habilidade <= habilidade :
                            print(textos.T273())
                            topazio += 2
                            resposta = int(input("Escolha: "))

                            #Engatinhando para fora do aposento com o crânio
                            if resposta == 1 :
                                print(textos.T15())
                                cranio += 1

                            #Colocando o crânio de volta antes de sair do aposento
                            elif resposta == 2 :
                                print(textos.T204())
                                input("\nTeste sua sorte...")
                                teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                                sorte -= 1

                                #Tendo sorte
                                if teste_da_sorte <= sorte :
                                    print("\nVocê teve sorte!")
                                    print(textos.T131())
                                
                                #Não tendo sorte
                                else :
                                    print("\nVocê não teve sorte!")
                                    print(textos.T199())
                                    dardos = random.randint(1,6)
                                    energia -= dardos * 2
                                    sorte -= 1

                        #Não passando no teste novamente 
                        else :
                            print(textos.T113_2())

            #Pegando as bolas de madeira e indo embora
            elif escolha == 3 :
                bola_madeira += 2
        
        #PARA CIMA ESTÁ TUDO COMPLETO, ESTAREI ALTERANDO SÓ ABAIXO AGORA ================================================================================
        #Continuando oeste
        #Tendo o anel dos desejos
        if anel_de_ouro > 0 :
            print(textos.T74())
            resposta = int(input("Escolha: "))
            
            #Fazendo um desejo utilizando o anel
            if resposta == 1 :
                print(textos.T265())
                anel_de_ouro -= 1
            
            #Quebrando o espelho
            elif resposta == 2 :
                print(textos.T300())
                escolha = int(input("Escolha: "))
                
                #Tentando quebrar o espelho de novo
                if escolha == 1 :
                    print(textos.T141())
                    input("Jogue os dados...🎲")
                    teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                    
                    #Passando no teste de habilidade
                    if teste_da_habilidade <= habilidade :
                        print(textos.T72())
                        habilidade -= 2
                    
                    #Não passando no teste de habilidade > MORTE
                    else :
                        print(textos.T96())
                        energia = 0
                
                #Atacando o demônio com a espada
                elif escolha == 2 :
                    print(textos.T327())
                    
                    #Inicializando as variáveis de ataque para o looping funcionar
                    ataqueInimigo = 0
                    meuAtaque = 0
                    
                    while ataqueInimigo < meuAtaque :
                        #Inicializando as variáveis para a batalha
                        guerreiro_esqueleto_1 = inimigos.inimigos["guerreiro_esqueleto"]

                        #Matando o Guerreiro Esqueleto
                        print("Briga com o Guerreiro Esqueleto...\n")

                        while guerreiro_esqueleto_1["Energia"] > 0 :
                            ataqueInimigo = guerreiro_esqueleto_1["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                            print("\nVocê teve sorte! Causou o dobro de dano")
                                            guerreiro_esqueleto_1["Energia"] -= 4
                                            sorte -= 1
                                            print("A energia atual do inimigo é: ", guerreiro_esqueleto_1["Energia"])
                                            print(f"Sua sorte agora é {sorte}")

                                        else :
                                            print("\nVocê não teve sorte, causou menos dano!")
                                            guerreiro_esqueleto_1["Energia"] -= 1
                                            sorte -= 1
                                            print("A energia atual do inimigo é:", guerreiro_esqueleto_1["Energia"])
                                            print(f"Sua sorte agora é {sorte}")
                                            
                                    else :
                                        print("Você infelizmente não tem mais sorte")
                                        guerreiro_esqueleto_1["Energia"] -= 2
                                        print("\nA energia atual do inimigo é: ", guerreiro_esqueleto_1["Energia"])

                                else :
                                    guerreiro_esqueleto_1["Energia"] -= 2
                                    print("\nA energia atual do inimigo é: ", guerreiro_esqueleto_1["Energia"])

                            #Tomando dano
                            else :
                                print("Quer testar sua sorte para receber menos dano?")
                                testarSorte = input().lower()

                                if testarSorte == "sim" :
                                    if sorte > 0 :
                                        input("Jogue os dados para testar sua sorte...\n")
                                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                        if teste_da_sorte <= sorte :
                                            print("\nVocê teve sorte! Recebeu menos dano!")
                                            energia -= 1
                                            sorte -= 1
                                            print(f"Sua energia atual é {energia}")
                                            print(f"Sua sorte agora é {sorte}")

                                        else :
                                            print("\nVocê não teve sorte, recebeu mais dano!")
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
            
            #Atacando o demônio com a espada > NÃO TA FEITOOO, FAZER ESSA BOSTA DESSA BATALHA QUANDO VOLTAR PARA CASA
            elif resposta == 3 :
                print(textos.T327())
        
        #Não tendo o anel dos desejos
        else :
            print(textos.T74_2())
            resposta = int(input("Escolha: "))
            
            #Quebrando o espelho
            if resposta == 1 :
                print(textos.T300())
            
            #Atacando o demônio com a espada > NÃO TA FEITOOO, FAZER ESSA BOSTA DESSA BATALHA QUANDO VOLTAR PARA CASA
            elif resposta == 2 :
                print(textos.T327())
        
        #Depois de desejar que o demônio vá embora ou de vencer a luta
        print(textos.T122())
        resposta = int(input("Escolha: "))
        
        #Subindo lance da esquerda
        if resposta == 1 :
            print(textos.T176())
            print(textos.T277())
            print(textos.T338())
            escolha = int(input("Escolha: "))
            
            #Pegando o colar
            if escolha == 1 :
                print(textos.T123())
                habilidade += 1
                energia += 1
            
            #Não pegando o colocar/continuando viagem
            print(textos.T282())
            resposta = int(input("Escolha: "))
            
            #Aceitando a oferta e viajando com o bárbaro para o oeste
            if resposta == 1 :
                print(textos.T22())
                escolha = int(input("Escolha: "))
                
                #Aceitando a oferta e descendo a corda
                if escolha == 1 :
                    print(textos.T63())
                    print(textos.T194())
                    resposta = int(input("Escolha: "))
                    
                    #Abrindo o livro vermelho
                    if resposta == 1 :
                        print(textos.T52())
                        escolha = int(input("Escolha: "))
                        
                        #Abrindo o livro preto
                        if escolha == 1 :
                            print(textos.T138_2())
                            resposta = int(input("Escolha: "))
                            
                            #Bebendo o líquido
                            if resposta == 1 :
                                print(textos.T397())
                                sorte += 2
                                detectar_armadilhas = True
                            
                            #Passando o líquido nos ferimentos
                            elif resposta == 2 :
                                print(textos.T75_2())
                    
                    #Abrindo o livro preto
                    elif resposta == 2 :
                        print(textos.T138())
                        escolha = int(input("Escolha: "))
                        
                        #Bebendo o líquido
                        if escolha == 1 :
                            print(textos.T397())
                            sorte += 2
                            detectar_armadilhas = True
                            resposta = int(input("Escolha: "))
                            
                            #Abrindo o livro vermelho depois de beber
                            if resposta == 1 :
                                print(textos.T52_3())
                        
                        #Passando o líquido nos ferimentos
                        elif escolha == 2 :
                            print(textos.T75())
                            resposta = int(input("Escolha: "))
                            
                            #Abrindo o livro vermelho depois de espalhar o líquido em seus ferimentos
                            if resposta == 1 :
                                print(textos.T52_3())
                        
                        #Abrindo o livro vemelho
                        elif escolha == 3 :
                            print(textos.T52_2())
                            resposta = int(input("Escolha: "))
                            
                            #Bebendo o líquido
                            if resposta == 1 :
                                print(textos.T397_2())
                                sorte += 2
                                detectar_armadilhas = True
                            
                            #Passando nos ferimentos
                            elif resposta == 2 :
                                print(textos.T75_2())
                    
                    #Continuando pelo norte
                    print(textos.T369())
                    
                    #Inicializando as variáveis para a batalha
                    troll_caverna = inimigos.inimigos["troll_caverna"]

                    #Matando o Guerreiro Esqueleto
                    print("Briga com o Guerreiro Esqueleto...\n")

                    while troll_caverna["Energia"] > 0 :
                        ataqueInimigo = troll_caverna["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                                        print("\nVocê teve sorte! Causou o dobro de dano")
                                        troll_caverna["Energia"] -= 4
                                        sorte -= 1
                                        print("A energia atual do inimigo é: ", troll_caverna["Energia"])
                                        print(f"Sua sorte agora é {sorte}")

                                    else :
                                        print("\nVocê não teve sorte, causou menos dano!")
                                        troll_caverna["Energia"] -= 1
                                        sorte -= 1
                                        print("A energia atual do inimigo é:", troll_caverna["Energia"])
                                        print(f"Sua sorte agora é {sorte}")
                                        
                                else :
                                    print("Você infelizmente não tem mais sorte")
                                    troll_caverna["Energia"] -= 2
                                    print("\nA energia atual do inimigo é: ", troll_caverna["Energia"])

                            else :
                                troll_caverna["Energia"] -= 2
                                print("\nA energia atual do inimigo é: ", troll_caverna["Energia"])

                        #Tomando dano
                        else :
                            print("Quer testar sua sorte para receber menos dano?")
                            testarSorte = input().lower()

                            if testarSorte == "sim" :
                                if sorte > 0 :
                                    input("Jogue os dados para testar sua sorte...\n")
                                    teste_da_sorte = random.randint(1,6) + random.randint(1,6)

                                    if teste_da_sorte <= sorte :
                                        print("\nVocê teve sorte! Recebeu menos dano!")
                                        energia -= 1
                                        sorte -= 1
                                        print(f"Sua energia atual é {energia}")
                                        print(f"Sua sorte agora é {sorte}")

                                    else :
                                        print("\nVocê não teve sorte, recebeu mais dano!")
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
                    
                    print(textos.T288())
                    resposta = int(input("Escolha: "))
                    
                    #Colocando o anel
                    if resposta == 1 :
                        print(textos.T64())
                        input("Jogue os dados...🎲")
                        teste_da_habilidade = random.randint(1,6) + random.randint(1,6)
                        
                        #Passando no teste
                        if teste_da_habilidade <= habilidade :
                            print(textos.T115())
                            energia += 3
                        
                        #Não passando no teste
                        else :
                            print(textos.T190())
                            energia -= 3
                            print(textos.T50())
                    
                    #Continuando sem ou anel ou depois de colocar o anel
                    print(textos.T221())
                    resposta = int(input("Escolha: "))
                    
                    #Examinando a caverna
                    if resposta == 1 :
                        print(textos.T374())
                        input("\nTeste sua sorte...")
                        teste_da_sorte = random.randint(1,6) + random.randint(1,6)
                        
                        #Tendo sorte
                        if teste_da_sorte <= sorte :
                            print(textos.T118())
                        
                        #Não tendo sorte
                        else :
                            print(textos.T295())
                            energia -= 5
                            print(textos.T206())
                            provisoes -= 1
                            energia += 4
                    
                    #Continuando depois de explorar a caverna ou não explorando
                
                #Oferece ajudar com a descida dele
                elif escolha == 2 :
                    print(textos.T184())
                
                #Fala para os dois pularem
                elif escolha == 3 :
                    print(textos.T311())
            
            #Não aceitando a oferta e indo para o leste sozinho
            elif resposta == 2 :
                print(textos.T388())
        
        #Subindo lance da direita
        elif resposta == 2 :
            print(textos.T384())
    
    #Abrindo a porta para o norte
    elif escolha == 3 or respostaT307 == 2 :
        print(textos.T136())
    


    #MAIS PARA FRENTE TUDO VAI ACABAR NO 282
    #print(textos.T282())
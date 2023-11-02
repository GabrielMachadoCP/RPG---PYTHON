import inimigos
import random

demonio = inimigos.inimigos["demonio_espelho"]

sorte = 15
habilidade = 4
energia = 19

while energia != 0 :
    #Inicializando as variáveis para a batalha
    demonio = inimigos.inimigos["demonio_espelho"]

    #Matando o Guerreiro Esqueleto
    print("Briga com o Guerreiro Esqueleto...\n")

    while demonio["Energia"] > 0 or energia > 0 :
        ataqueInimigo = demonio["Habilidade"] + random.randint(1,6) + random.randint(1,6)
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
                        demonio["Energia"] -= 4
                        sorte -= 1
                        print("A energia atual do inimigo é: ", demonio["Energia"])
                        print(f"Sua sorte agora é {sorte}")

                    else :
                        print("\nVocê não teve sorte, causou menos dano!")
                        demonio["Energia"] -= 1
                        sorte -= 1
                        print("A energia atual do inimigo é:", demonio["Energia"])
                        print(f"Sua sorte agora é {sorte}")
                        
                else :
                    print("Você infelizmente não tem mais sorte")
                    demonio["Energia"] -= 2
                    print("\nA energia atual do inimigo é: ", demonio["Energia"])

            else :
                demonio["Energia"] -= 2
                print("\nA energia atual do inimigo é: ", demonio["Energia"])

        #Tomando dano
        else :
            print("Você morreu")
            energia = 0
            print(energia)
    
    print("KAKAKAKAKAKA")
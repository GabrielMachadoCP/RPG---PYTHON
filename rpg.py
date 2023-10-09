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

    "hobgoblin" : {
        "Nome" : "Hobgoblin",
        "Habilidade" : 6,
        "Energia" : 5
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

#Apresentação
print("Bem-vindo ao Calabouço da Morte")

#Mostrando a ficha
print("=" * 50)
print("SUA FICHA\n")

habilidade, energia, sorte = ficha.fichaValores()

ficha = {
        "Habilidade" : habilidade,
        "Energia" : energia,
        "Sorte" : sorte,
        "Provisões" : 10
        }

print("=" * 50)

#Começando a condição de looping
# while energia != 0 or energia > 0 :

#Condição inicial:
#Quer abrir a caixa? Sim(270) e Não (66)

#66
#Quer ir para Oeste ou Leste? Leste(119) e Oeste (293)
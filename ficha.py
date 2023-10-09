# Ana zerlin       rm 98065
# Bianca Dancs     rm 551645
# Gabriel Pimentel rm 99880
# Hellen Assis     rm 98284

import random

def fichaValores() :
        habilidade = random.randint(1,6) + 6
        energia = random.randint(1,6) + random.randint(1,6) + 12
        sorte = random.randint(1,6) + 6

        ficha = {
                "Habilidade" : habilidade,
                "Energia" : energia,
                "Sorte" : sorte,
                "Provisões" : 10
                }

        return ficha
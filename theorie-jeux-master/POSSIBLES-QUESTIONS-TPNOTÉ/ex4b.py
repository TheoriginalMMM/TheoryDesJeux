import numpy as np
from Classe.Joueur import *
from Classe.Troll import *
from Classe.Jeux import *
from src.Strategy import  *


if __name__ == "__main__":

    taille_jeux = 5
    nbr_pierre = 20
    joueur1_gagnant = 0
    joueur2_gagnant = 0
    match_null = 0
    cache = None

    for i in range(400):
        prudent_strat = Strategie_prudente(taille_jeux)
        random_strat = Strategie_random_Ndiv3(taille_jeux)
        joueur1 = Joueur(nbr_pierre, prudent_strat, 1)
        joueur2 = Joueur(nbr_pierre, random_strat, 2)
        
        if not cache is None:
            # joueur1.strategy.cache = cache
            joueur1.strategy.cache = cache

        troll = Troll()
        stage = Stage([joueur1, joueur2], troll, taille_jeux)
        jeux = Jeux(stage)
        joueur1.setGame(jeux)
        joueur2.setGame(jeux)
        gagnant = jeux.lancement()

        # print(prudent_strat.last_pu)

        if cache is None:
            cache = joueur1.strategie.cache

        if gagnant == 1: joueur1_gagnant += 1
        elif gagnant == 2: joueur2_gagnant += 1
        else: match_null += 1

    print("joueur 1: Stratégie prudente |  joueur 2: Stratégie random ndiv3")
    print("joueur 1 gagnant : ", joueur1_gagnant, " joueur 2 gagnant ", joueur2_gagnant, " match null : ", match_null)

from Strategies import *
from Jeux import *
#from Classe.Troll import *

#Fonction qui va constuire un jeux
#Retourne jeux, joueur_1, joueur_2, plateau, nbr_pierre
def constructeur_jeux(strat1 = Strategie_random, strat2 = Strategie_prudente, taille_jeux = 7, nbr_pierre = 8):

    #Définit les deux stratégies des joueurs : random et prudente
    random_strat = strat1(taille_jeux)
    prudent_strat = strat2(taille_jeux)

    #Construit 2 joueur qui ont un :
    # --nbr_pierre : nombre de pierre du joueur
    # --random_strat/prudent_strat : stratégie du joueur
    # -- un entier qui est l'id du joueur (pour les différencier)
    joueur_1 = Joueur(nbr_pierre, random_strat, 1)
    joueur_2 = Joueur(nbr_pierre, prudent_strat, 2)

    #Construit un Troll
    troll = Troll()

    #Construit un plateau de jeux qui va comporter :
    # -- 2 joueurs
    # -- 1 troll
    # -- qui a une certaine taille
    plateau = Plateau([joueur_1, joueur_2], troll, taille_jeux)

    #Construit le jeux à partir du plateau construit
    jeux = Jeux(plateau)

    #Ajoute les jouers dans le jeux
    joueur_1.setGame(jeux)
    joueur_2.setGame(jeux)

    return jeux, joueur_1, joueur_2, plateau, nbr_pierre
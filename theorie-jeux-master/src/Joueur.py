from Entite import *
from Strategies import  *
import random

#CLass joueur implente entité
class Joueur(Entite):

    def __init__(self, total_pierre, strat, id):

        self.total_pierre = total_pierre # nombre total de pierre du joueur
        self.strategie = strat # stratégie du joueur
        self.id = id # id du joueur (1 ou 2)
        self.strategie.setJoueuerID(self.id)

    def setGame(self, jeux):
        self.jeux = jeux


    def choix_pierre(self, dernier_choix=0) -> int:

        #Si le joueur n'a plus de pierre
        if self.total_pierre < 1:
            return 0

        taille_jeux = self.jeux.plateau.taille
        joueur1 = self.jeux.plateau.joueur1
        joueur2 = self.jeux.plateau.joueur2
        troll_pos = self.jeux.plateau.troll.position

        milieu = (taille_jeux // 2) + 1
        if troll_pos < milieu:
            tp = troll_pos - milieu
        elif troll_pos > milieu:
            tp = milieu - troll_pos
        else:
            tp = 0

        autre_joueur = self.jeux.plateau.joueur2

        if self.id == 2:
            tp = tp * -1
            autre_joueur = self.jeux.plateau.joueur1

        pierre_autre_joueur = autre_joueur.total_pierre + dernier_choix
        #print('tp:', tp, 'troll_pos:', troll_pos, 'player', self.id, ' nbr_pierre: ', self.total_pierre, ' player', autre_joueur.id, ' nbr_pierre', pierre_autre_joueur)
        choix_pierre = self.strategie.apply(self.total_pierre, pierre_autre_joueur, tp)
        #self.strategie.print_last_step()    

        self.total_pierre -= choix_pierre
        if(self.total_pierre<0):
            print("PROBLEMME @@@@@@@@@@@@@@@@@@@@")
        return choix_pierre

    def update(self, dernier_choix=0):
        self.jet_actuel = self.choix_pierre(dernier_choix)
        return self.jet_actuel
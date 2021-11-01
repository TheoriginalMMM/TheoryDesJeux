from Joueur import *
from Plateau import *
import sys
from Strategies import *
from typing import List
import random
class Jeux:

    def __init__(self, stage):
        self.plateau = stage

    def update(self):
        #print("joueur va choisir",self.plateau.joueur1.id)
        dernier_choix = self.plateau.joueur1.update() #Le joueur 1 tire un nombre de pierre
        self.plateau.joueur2.update(dernier_choix)
        direction = self.plateau.joueur1.jet_actuel - self.plateau.joueur2.jet_actuel
        self.plateau.troll.update(direction)

    def lancement(self):

        while self.plateau.extreme_gauche < self.plateau.troll.position < self.plateau.extreme_droite:

            self.update()

            if self.plateau.joueur1.total_pierre == 0:
                self.plateau.troll.position -= self.plateau.joueur2.total_pierre
                break

            if self.plateau.joueur2.total_pierre == 0:
                self.plateau.troll.position += self.plateau.joueur1.total_pierre
                break

            if self.plateau.joueur1.total_pierre + self.plateau.joueur2.total_pierre == 0:
                break

        milieu = (self.plateau.taille // 2) + 1
        troll_pos = self.plateau.troll.position

        if troll_pos < milieu:
            # print("joueur 2 gagnant the game")
            return 2
        elif troll_pos > milieu:
            # print("joueur 1 gagnant the game")
            return 1
        else:
            # print("drow match")
            return 0
    def run(self): 

        while self.plateau.extreme_gauche < self.plateau.troll.position < self.plateau.extreme_droite:

            self.update()

            if self.plateau.joueur1.total_pierre == 0:
                self.plateau.troll.position -= self.plateau.joueur2.total_pierre
                break

            if self.plateau.joueur2.total_pierre == 0:
                self.plateau.troll.position += self.plateau.joueur1.total_pierre
                break

            if self.plateau.joueur1.total_pierre + self.plateau.joueur2.total_pierre == 0:
                break

        middle = (self.plateau.taille // 2) + 1
        troll_pos = self.plateau.troll.position

        if troll_pos < middle: 
            # print("player 2 won the game")
            return 2
        elif troll_pos > middle: 
            # print("player 1 won the game")
            return 1
        else: 
            # print("drow match")
            return 0
from Troll import *
from Joueur import *
import sys
from Strategies import *
from typing import List
import random

class Plateau:

    def __init__(self, joueurs: List[Joueur], troll: Troll, taille: int):

        if taille < 1:
            raise ValueError('La taille doit être superieur à 0')

        if taille % 2 == 0:
            raise ValueError('La taille doit être un nombre impair')

        self.extreme_gauche = 1
        self.extreme_droite = taille
        self.taille = taille
        self.joueur1 = joueurs[0]
        self.joueur2 = joueurs[1]
        self.troll = troll
        self.troll.setPlateau(self, position=(taille // 2 + 1)) # Manque un self ? ( a revoir)
        self.joueur1.setPlateau( joueurs[0],self.extreme_gauche)
        self.joueur2.setPlateau(joueurs[1], self.extreme_gauche)


import numpy as np
from Joueur import *
from Troll import *
from Jeux import *
from Strategies import  *
from Plateau  import *
from Builders import *
def Affronter(NBParties,Strategi1,Strategi2,taille,NBPierres,Strategi1UseCash=False,Strategi2UseCash=False):
    if(Strategi1UseCash):
        cache1=None
    if(Strategi2UseCash):
        cache2=None
    joueur1_gagnant=0
    joueur2_gagnant=0
    match_null=0

    for i in range(NBParties):
        #Choisir les strateies de chaque joueur 
        joueur1 = Joueur(NBPierres, Strategi1, 1)
        joueur2 = Joueur(NBPierres, Strategi2, 2)
        #A decommenter aprés (ou a géneraliser )
        if(Strategi1UseCash):
            if not cache1 is None:
                joueur1.strategie.cache = cache1
        if(Strategi2UseCash):
            if not cache2 is None:
                joueur2.strategie.cache = cache2

        #initialisation du troll
        troll = Troll()
        stage = Plateau([joueur1, joueur2], troll, taille)
        jeux = Jeux(stage)
        joueur1.setGame(jeux)
        joueur2.setGame(jeux)
        gagnant = jeux.run()

        #Pour accelere les prochaines executions
        if(Strategi1UseCash):
            if cache1 is None:
                cache1 = joueur1.strategie.cache
        if(Strategi2UseCash):
            if cache2 is None:
                cache2=  joueur2.strategie.cache
        
        if gagnant == 1: joueur1_gagnant += 1
        elif gagnant == 2: joueur2_gagnant += 1
        else: match_null += 1
    
    tauxJ1 = joueur1_gagnant/NBParties
    tauxJ2 = joueur2_gagnant/NBParties
    tauxMatchNull = match_null/NBParties
    print("------------------------------------------------------------------------------------------------------------")
    print("TAILLE :",taille , "Nombre de pierre :",NBPierres)
    print("joueur 1:",Strategi1.getName(),"|  joueur 2: ",Strategi2.getName())
    print("joueur 1 gagnant : ", joueur1_gagnant, " joueur 2 gagnant ", joueur2_gagnant, " match null : ", match_null)
    print("joueur 1 gagne à  : ", tauxJ1, " joueur 2 gagne a  ", tauxJ2, " match null : ", tauxMatchNull)
    print("------------------------------------------------------------------------------------------------------------")

    
           
    




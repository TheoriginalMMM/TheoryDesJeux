import random
import numpy as np
import pulp as pu

#Class abstraite des strategies
class Strategie:
    def __init__(self, taille):
        self.taille = taille

    def apply(self, nb_p1, nb_p2, tpos):
        pass
    
    def setJoueuerID(self,id):
        self.joueurID=id

#Strategie aléatoire : on tire un nombre aléatloire parmi les pierres qui nous reste
class Strategie_random(Strategie):
    def apply(self, nb_p1, nb_p2 , tpos ):
        return random.randint(1, nb_p1)
    
    def getName(self):
        return "Strategie random"

#Strategie prudente, on utilise le simplex (pulp pour trouver la distribution des probabilité)
class Strategie_prudente(Strategie):
    def __init__(self, taille):
        super().__init__(taille=taille)
        self.cache = {}
        self.derniere_etape = None
        self.dernier_pu = None
    

    def apply(self, nb_p1, nb_p2, tpos):
        if(self.joueurID==1):
            return res_lineaire(self, nb_p1, nb_p2, tpos, get_meilleur_choix)[1]
        else:
            return res_lineaire(self, nb_p1, nb_p2, -tpos, get_meilleur_choix)[1]

    #fonction pour afficher les probabilités trouvé avant de lancer une pierre
    def print_last_step(self):
        for i in range(len(self.derniere_etape)):
            print(i+1, 'proba:', self.derniere_etape[i].varValue, end=' ')

    def getName(self):
        return "Strategie prudente"

#Strategie prudente inversse, elle prende le mauvais choix a chaque fois : (on utilise les même probabilité
# retourner par le simplex de la strategie prudent mais on prend le choix avec la plus petit valeurs)
class Strategie_prudente_inverse(Strategie):
    def __init__(self, taille):
        super().__init__(taille=taille)
        self.cache = {}
        self.derniere_etape = None

    def apply(self, nb_p1, nb_p2, tpos):
        return res_lineaire(self, nb_p1, nb_p2//2, tpos, get_pire_choix)[1]


    def getName(self):
        return "Strategie prudente invers"

#choisir le nombre de pierre a jouer avec la console
class Strategie_Humaine(Strategie):
    def __init__(self, taille):
        super().__init__(taille=taille)
    
    def apply(self, nb_p1, nb_p2, tpos):
        print("Il vous reste :",nb_p1, "Position du trolle",tpos,"\n")
        print("Entrer un nombre de pierre a joueur dans l'intervalle [1 ,",nb_p1,"] :\n")
        nbChoisie=int(input())
        while(nbChoisie<1 or nb_p1<nbChoisie):
            print("ouups ! c'est pas possible ca")
            nbChoisie=int(input())
        return nbChoisie


    def getName(self):
        return "Strategie Humaine"

#Genere une clé à utilisé pour stokcer les gains déja calculé(pour acceler le programme et eviter de recalculer des gains déja calculé)
def gen_cle(nb_p1, nb_p2, troll_pos):
    return '{}-{}-{}'.format(nb_p1, nb_p2, troll_pos)

#Calculé le gain d'une configuration
def gain(start, nb_p1, nb_p2, troll_pos, get_choix):
    #On check les cas triviaux 
    if troll_pos == (start.taille - 1) / 2:
        return 1 
    
    if troll_pos == -((start.taille -1) / 2):
        return -1 
    if nb_p1 == 0:
        if(troll_pos<0):
            return -1
        if nb_p2 > troll_pos:
            return -1 
        if nb_p2 < troll_pos:
            return 1 
        return 0

    if nb_p2 == 0:
        if nb_p1 + troll_pos > 0:
            return 1 
        if nb_p1 + troll_pos < 0: 
            return -1 
        return 0

    #Sinon on regarde si on a déja calculé ce gain avant
    cle = gen_cle(nb_p1, nb_p2,troll_pos)
    if not cle in start.cache.keys():
        #On calcule le gain avec le simplexe une seul fois et on le stocke dans le cash
        start.cache[cle] = res_lineaire(start, nb_p1, nb_p2, troll_pos, get_choix)[0]

    return start.cache[cle]

#Choisir un nombre de pierre a jeter selon une distribution de probabilité retourné par le simplex
#Le nombre de pierre avec une probabilité elvé il sera choisie dans la plupart du temps
#C'est un choix probabiliste(r) , REF : ROULET WHEEL 
def get_meilleur_choix(strat, variable_contrainte):
    strat.derniere_etape = variable_contrainte
    r = random.randint(1, 100)
    s = 0
    dernier_i = None
    for i in  range(0, len(variable_contrainte)-1):                                       
        prob = variable_contrainte[i].varValue
        s += prob
        dernier_i = i 
        if s * 100 >= r: 
            return i + 1
    return dernier_i + 1

#Choisir un nombre de pierre a jeter selon une distribution de probabilité retourné par le simplex
#Le nombre de pierre avec la plus petite probabilité il sera choisie dans la plupart du temps
#C'est un choix probabiliste  (r ), REF : ROULET WHEEL  
def get_pire_choix(strat, variable_contrainte):
    strat.derniere_etape = variable_contrainte
    r = random.randint(1, 100)
    s = 0
    for i in  range(0, len(variable_contrainte)-1):
        prob = variable_contrainte[i].varValue
        s += prob
        if s * 100 <= r:
            return i + 1
        dernier_i = i
    
    return dernier_i + 1

#Fonction pour afficher la matrice des gains 
def print_MatriceGain(matrice):
    resultats="MATRICES GAINS: \n"
    for row in matrice:
        lignes="["
        for i in range (len(row)):
            lignes+=str(row[i][5])+" "
        lignes+="]"
        resultats+=lignes
    return resultats

#La résolutions d'un system linéaire pour trouver le meilleur gain et la distribution de
def res_lineaire(strat, nb_p1, nb_p2, tpos, get_choix):
    dimensions=(nb_p1, nb_p2)
    lignes=nb_p1
    colonnes=nb_p2
    #On creer la matrice de tous les possibles configurations selon le nb_p1 , nb_p2 et la tpos
    matrice =np.empty(dimensions, dtype=object)
    for i in range(lignes):
        for j in range(colonnes):
            l = lignes-1-i
            w = colonnes-1-j
            #On calcule la postion la nouvelle position du trol selon le nombre de pierre jetter par p1 et p2
            troll_pos = calcul_troll_pos(strat,nb_p1,nb_p2,tpos, l,w)
            #On calcule le gain de cette configuration et on le stocke dans la matrice
            gain_joueur = gain(strat, l, w, troll_pos, get_choix)
            matrice[i,j]= (nb_p1,nb_p2,l,w,troll_pos, gain_joueur)

    #On initialise le problme linéaire
    mon_lp_probleme = pu.LpProblem("MonLPProbleme", pu.LpMaximize)
    char = "a_"
    variable_contrainte = []
    #Declaration des probabilités (ai, anbp1)
    for i in range(len(matrice)):
        variable_contrainte.append(pu.LpVariable(char+str(i), lowBound=0, cat='Continuous'))
    #On declare la variable de  G*
    variable_contrainte.append(pu.LpVariable("G", lowBound=-10000, cat='Continuous'))
    mon_lp_probleme += variable_contrainte[-1], 'G'

    #Une contrainte par collone (on utilise la matrice transpose()) (CF : rapport) 
    for row in matrice.transpose():
        constraint = None
        for i in range(len(row)):
            gainp = row[i][5]
            constraint += gainp * variable_contrainte[i]
        mon_lp_probleme += constraint - variable_contrainte[-1] >= 0

    constraint = None
    
    for i in  range(len(variable_contrainte) -1):
        constraint += variable_contrainte[i]
    #Contrainte sur la somme des probas = 1
    mon_lp_probleme += constraint == 1
    #Resolution du probleme linéaire
    mon_lp_probleme.solve()
    #On stocke la valeur de G*
    strat.last_pu = pu.value(mon_lp_probleme.objective)
    
    #On retoure le gain et le nombre de pierre a tirer selon la distribution de proba (variable_contrainte)
    return strat.last_pu, get_choix(strat, variable_contrainte)


#Calculer la nouvelle position du trolle (regles de jeux )
def calcul_troll_pos(strat, p1_init, p2_init,t_prec, p1, p2):
    #On calcule combien de pierre chaque joueur a jetter
    jeux_p1 = p1_init - p1
    jeux_p2 = p2_init - p2

    if (jeux_p1 == jeux_p2):
        return t_prec
    if (jeux_p1 > jeux_p2):
        return t_prec +1
    else:
        return t_prec -1

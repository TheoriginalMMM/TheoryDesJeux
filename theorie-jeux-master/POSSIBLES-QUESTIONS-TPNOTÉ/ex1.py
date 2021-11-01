from src.Builders import *
from src.Strategy import *

if __name__ == "__main__":
    cache = None

    for i in range(23, 1, -1):

        ps = Strategie_prudente(5)
        
        if not cache is None:
            ps.cache = cache

        # for i in range(100):
        nbr_pierre = ps.apply(23, i, -1)

        if cache is None:
            cache = ps.cache

        contrainte = ps.derniere_etape
        # ps.print_last_step() # ici pour savoir Comment joue-t-il sur la configuration
        print(i, 'gain:', ps.dernier_pu)





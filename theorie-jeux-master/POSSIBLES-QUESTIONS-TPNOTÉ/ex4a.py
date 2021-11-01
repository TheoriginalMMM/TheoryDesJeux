from src.Builders import *
from src.Strategy import *

if __name__ == "__main__":
    cache = None

    ps = Strategie_prudente(5)
    
    if not cache is None:
        ps.cache = cache

    # for i in range(100):
    nbr_pierre = ps.apply(20, 20, 0)

    if cache is None:
        cache = ps.cache

    contrainte = ps.derniere_etape
    ps.print_derniere_etape() # ici pour savoir Comment joue-t-il sur la configuration
    print('gain:', ps.dernier_pu)





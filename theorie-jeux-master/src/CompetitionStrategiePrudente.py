from UtilePourCompetition import *

if __name__ == "__main__":

    taillesdeJeux=[7,7,15,15]
    Nombres_Pierres=[15,30,30,50]
    for i in range(len(taillesdeJeux)):

        StrategiePrincipale=Strategie_prudente(taillesdeJeux[i])
        OtherStrategies=[]
        OtherStrategies.append(Strategie_prudente(taillesdeJeux[i]))
        OtherStrategies.append(Strategie_prudente_inverse(taillesdeJeux[i]))
        OtherStrategies.append(Strategie_random(taillesdeJeux[i]))

        for j in range(len(OtherStrategies)):
            
            if(OtherStrategies[j].getName()=="Strategie random"):
                Affronter(1000,StrategiePrincipale,OtherStrategies[j],taillesdeJeux[i],Nombres_Pierres[i],Strategi1UseCash=True,Strategi2UseCash=False)
            else:
                Affronter(1000,StrategiePrincipale,OtherStrategies[j],taillesdeJeux[i],Nombres_Pierres[i],Strategi1UseCash=True,Strategi2UseCash=True)   
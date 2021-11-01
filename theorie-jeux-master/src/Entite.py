class Stage:
    pass

#CLasse abstraite pour toutes les entités de notre jeu (troll et les deux joueures)
class Entite:
    def setPlateau(self, stage: Stage, position: int):
        self.position = position



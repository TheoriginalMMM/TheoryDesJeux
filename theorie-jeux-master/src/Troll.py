
from Entite import *
#Troll implemente entite
class Troll(Entite):
    def update(self, direction):

        if direction < 0:
            # print("direction: -1")
            # avance vers j1
            self.position = self.position - 1
        elif direction > 0:
            # avance vers j2
            # print("direction: +1")

            # avatage j2
            # if direction > 2:
            #     self.position = self.position + 2
            # else:
            self.position = self.position + 1

        else:
            pass
            # print("direction: 0")

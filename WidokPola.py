class WidokPola:
    pole = None
    zwierzetaNaPolu = None

    def __init__(self, pole, zwierzetaNaPolu):
        self.pole = pole
        self.zwierzetaNaPolu = zwierzetaNaPolu

    def __str__(self):
        return "Pole: " + str(self.pole.x) + ", " + str(self.pole.y) + ":\n" +\
               str(self.zwierzetaNaPolu)
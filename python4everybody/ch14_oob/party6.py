from party import PartyAnimal

class CricketFan(PartyAnimal):
    """docstring for CricketFan"""
    points = 0
    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, 'points', self.points)

x = PartyAnimal('Xi')
x.party()
j = CricketFan('Jiang')
j.six()
print(dir(j))

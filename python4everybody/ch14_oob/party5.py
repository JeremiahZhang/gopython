class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

x = PartyAnimal('Xi')
j = PartyAnimal('Jiang')

x.party()
j.party()
PartyAnimal.party(x)

# many instance

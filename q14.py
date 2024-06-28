class Athlete:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

    def train(self):
        print(f"{self.name} is training for {self.sport}")


class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def perform(self):
        print(f"{self.name} is performing on {self.instrument}")


class Performer(Athlete, Musician):  # Multiple inheritance
    def __init__(self, name, sport, instrument):
        Athlete.__init__(self, name, sport)
        Musician.__init__(self, name, instrument)


performer = Performer("Iqra", "Basketball", "violin")
performer.train()
performer.perform()

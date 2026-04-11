class Artist:
    def __init__(self, name):
        self.name = name


class Musician(Artist):
    def __init__(self, name, instrument):
        super().__init__(name)
        self.instrument = instrument


if __name__ == "__main__":
    john = Musician("John Lennon", "Guitar")
    print(john.name)
    print(john.instrument)

# parent class
class Organism:

    # dunder method, allows passing of arguments upon object instantiation
    def __init__(self, name, species, origin):
        self.name = name
        self.species = species
        self.origin = origin

    def method(self):
        msg = "\nThis is placeholder text"
        return msg

# New object - inherits methods from parent
class diffOrganism(Organism):
    trait = "Tall"
    scent = "Unknown"

    # Polymorphism, changes the same-named method from parent
    def method(self):
        msg = "\nThis is DIFFERENT placeholder text"
        return msg


class anotherOrganism(Organism):
    genus = "Unknown"
    latinName = "Squalus Fuscata"

    def method(self):
        msg = "\nThis is ANOTHER placeholder text"
        return msg    


if __name__ == "__main__":
    org1 = Organism("Jack", "Human", "Earth")
    org2 = diffOrganism("John", "Martian", "Mars")
    org3 = anotherOrganism("Jimbo", "Venusian", "Venus")

    print(org1.name)
    print(org2.trait)
    print(org3.latinName)

    print(org1.method())
    print(org2.method())
    print(org3.method())


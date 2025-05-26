class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner or None")
        self.owner = owner

        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Must add an instance of Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


o = Owner("Alice")
p1 = Pet("Fido", "dog")
p2 = Pet("Whiskers", "cat")

o.add_pet(p1)
o.add_pet(p2)

print(o.pets())           # [<Pet object at ...>, <Pet object at ...>]
print(o.get_sorted_pets())  # Sorted by pet name

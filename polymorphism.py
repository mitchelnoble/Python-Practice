class Bird:
    def fly(self):
        return "Birds can fly."
    
class Penguin:
    def fly(self):
        return "Penguins cannot fly"
    
def get_flight_ability(bird):
    print(bird.fly())

sparrow = Bird()
penguin = Penguin()

get_flight_ability(sparrow) #Output: Birds can fly.
get_flight_ability(penguin) #Output: Penguins cannot fly.


"""
Pokemon OOP game
"""
# Create a Pokemon
class Pokemon:
    
    def __init__(self, name, primary_type, max_hp = 20):
        self.name = name 
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp

    def __str__(self):
        return (f'name: {self.name.capitalize()}, primary type: {self.primary_type.capitalize()}, HP: {self.hp}/{self.max_hp}')

    def feed(self):
        if self.hp<self.max_hp:
            self.hp += 1
            print(f'{self.name} is now {self.hp}/{self.max_hp} HP.')
        else:
            print(f'{self.name} is full!')

    # pokemons battle eachother
    def battle(self, oponent):
        try:
            print('Battle:', self.name, 'VS', oponent.name)
            result = self.typewheel(self.primary_type, oponent.primary_type)
            print(f'{self.name.capitalize()} has', result)
            # depends on the result, effects
            if result=='lost':
                self.hp-=10
                print(self.name, 'has lost 10hp, current hp:', self.hp)
            else:
                self.hp-=5
                print(self.name, 'has lost 5hp, current hp:', self.hp)

        except:
            print("This isn't valid target for pokemon!")
        

    @staticmethod
    def typewheel(type1, type2):
        result = {0: 'lost', 1: 'won', -1:'tied'}
        # mapping between types and result conditions
        game_map = {'Water': 0, 'Fire': 1, 'Grass': 2}
        # implement win-lose matrix
        wl_matrix = [
            [-1, 1, 0],
            [0, -1, 1],
            [1, 0, -1]
        ]
        # declare a winner
        result_str = wl_matrix[game_map[type1]][game_map[type2]]
        return result[result_str]

# Take a look at it
b=(Pokemon('bulbasaur', 'Grass'))
c=(Pokemon('charmander', 'Fire'))

b.battle(c)

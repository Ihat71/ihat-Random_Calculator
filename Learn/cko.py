weight_classes = ['Feather weight', 'Lightweight', 'Cruiser weight', 'Middle weight', 'Light heavy weight', 'Heavy weight']

class Character:
    def __init__(self, name, height, age, stats):
        self.name = name
        self.height = height
        self.age = age
        self.stats = stats
        self.level = 0
    def stat_boost(self, boost):
        if boost == 'Big':
            for i in self.stats:
                self.stats[i] += 5
        if boost == 'Mid':
            for i in self.stats:
                self.stats[i] += 3
        if boost == 'Small':
            for i in self.stats:
                self.stats[i] += 1

    def level_up(self):
        x = input("You have leveled up! What stat do you want to upgrade? ")
        if x in self.stats:
            if x != 'weight':
                self.stats[x] += 1
                print(f'you have upgraded your {x} by 1!')
            else:
                print('You have to bulk or cut! ')
        else:
            print('Not a stat!')

    def bulk_cut(self):
        gym = input('Do you want to bulk or cut? ')
        if gym == 'bulk':
            x = weight_classes.index(self.stats['weight'])
            x += 1
            self.stats['weight'] = weight_classes[x]
            print('grats, you got bigger! ')
        if gym == 'cut':
            y = weight_classes.index(self.stats['weight'])
            y -= 1
            self.stats['weight'] = weight_classes[y]
            print('Wow, you got leaner! ')
    def __add__(self, other):
        return self.levels() + other.levels()
    
    def levels(self):
        total_sum = 0
        for i in self.stats:
            if i == 'weight':
                continue
            total_sum += self.stats[i]
        return total_sum
    def __repr__(self):
        return f"Character('{self.name}', {self.age}, {self.height}, {self.stats})"
    def __str__(self):
        return "A strong character"


ch1_stats = {
    'strength':80,
    'int':90,
    'speed':70,
    'agility':50,
    'craftiness':60,
    'dexterity':60,
    'weight':'Middle weight'

}
ch2_stats = {
    'strength':80,
    'int':90,
    'speed':70,
    'agility':50,
    'craftiness':60,
    'dexterity':60,
    'weight':'Middle weight'

}

char_1 = Character('Ahmad', 181, 19, ch1_stats)
char_2 = Character('Muhammad', 183, 20, ch2_stats)
print(char_1.stats)
print(str(char_1))
print(repr(char_1))

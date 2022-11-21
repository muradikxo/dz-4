import random


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f"{self.__name} health: {self.__health} damage: {self.__damage}"


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage

    def __str__(self):
        return "BOSS " + super().__str__() + f" defence: {self.__defence}"


class Heroes(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super(Heroes, self).__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        if boss.health > 0 and self.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Heroes):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, "CRITICAL_DAMAGE")

    def apply_super_power(self, boss, heroes):
        coef = random.randint(1, 5)
        boss.health -= self.damage * coef
        print(f"CRITICAL_DAMAGE {self.damage * coef}")


class Magic(Heroes):
    def __init__(self, name, health, damage):
        super(Magic, self).__init__(name, health, damage, "BOOST")

    def apply_super_power(self, boss, heroes):
        boost_point = random.randint(5, 11)
        print(f"BOOST POINT {boost_point}")
        for hero in heroes:
            if hero != self and hero.health > 0:
                hero.damage += boost_point


class Medic(Heroes):
    def __init__(self, name, health, damage):
        super(Medic, self).__init__(name, health, damage, "HEAL")

    def apply_super_power(self, boss, heroes):
        heal_point = random.randint(5, 11)
        print(f"HEAL POINT {heal_point}")
        for hero in heroes:
            if hero != self and hero.health > 0:
                hero.health += heal_point


class Berserk(Heroes):
    def __init__(self, name, health, damage):
        super(Berserk, self).__init__(name, health, damage, "FURY")

    def apply_super_power(self, boss, heroes):
        angry = random.randint(1, 5)
        boss.health -= self.damage * boss.damage // angry
        print(f"BARSEY ANGRY {self.damage * angry}")


class Thor(Heroes):
    def __init__(self, name, health, damage):
        super(Thor, self).__init__(name, health, damage, "LIGHTNING")
        
    def apply_super_power(self, boss, heroes):
            for hero in heroes:
                sun = random.randint(5, 11)
                if hero != self and hero.health > 0 and sun ==7:
                    hero.health += 50
                    print(" I am THOR ")


class Golem(Heroes):
    def __init__(self, name, health, damage):
        super(Golem, self).__init__(name, health, damage, "LIFE")
    
    def apply_super_power(self, boss, heroes):
        hit__boss = boss.damage // 5
        self.health - hit__boss
        for hero in heroes:
            if hero != self and hero.health > 0:
                hero.health += hit__boss
        


        

class Witcher(Heroes):
    def __init__(self, name, health, damage):
        super(Witcher, self).__init__(name, health, damage, "SAVE")
        self.__save = None

    @property
    def save(self):
        return self.__save

    @save.setter
    def name(self, value):
        self.__save = value

    def apply_super_power(self, heroes, boss):
        for hero in heroes:
            if hero != self and hero.health == 0:
                hero.health += self.health and self.health == 0
                print(f"герой {hero} оживлен")




class Druid(Heroes):
    def __init__(self, name, health, damage):
        super(Druid, self).__init__(name, health, damage, "SAVE")

    def apply_super_power(self, heroes, boss):
        animal = random.randint(0,1)
        heal_point2 = random.randint(5, 11)
        if animal == 0:
            for hero in heroes:
                if hero != self:
                    hero.health - 55
                    print("CROW IS RETURNED")
        elif animal == 1:
            for hero in heroes:
                if hero != self and hero.health > 0:
                    hero.health += heal_point2        
                    print(f"ANGEL HEAL POINT {heal_point2}")
            

class AntMan(Heroes):
    def __init__(self, name, health, damage):
        super(AntMan, self).__init__(name, health, damage, "SAVE")
    def apply_super_power(self, heroes, boss):
        choise = random.randint(0,1)
        ant = random.randint(2,10)
        man = random.randint(2,10)
        if choise == 0:
            self.damage - ant and self.health - ant
            print("Oh shit") 
        elif choise == 1:
            self.damage + man and self.health + man
            print("I AM BIG!")




            




round_counter = 0


def print_statistic(boss, heroes):
    print(f'_____________ ROUND {round_counter} _____________')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_counter
    round_counter += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)

    for hero in heroes:
        hero.hit(boss)
        hero.apply_super_power(boss, heroes)

    print_statistic(boss, heroes)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!")
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print("Boss won!")

    return all_heroes_dead


def start_game():
    boss = Boss("mura", 17500, 55)

    warrior = Warrior("aska", 270, 10)
    magic = Magic("simik", 280, 20)
    medic = Medic("Эра", 220, 5)
    berserk = Berserk("Barsey", 250, 15)
    thor = Thor("Kris", 300, 30)
    golem = Golem("neymar", 400, 2)
    witcher = Witcher("Geralt", 250, 0)
    druid = Druid("Grut", 290, 0)
    antman = AntMan("Skot", 250, 7)


    heroes = [warrior, magic, medic, berserk, thor, golem,antman]

    print_statistic(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()
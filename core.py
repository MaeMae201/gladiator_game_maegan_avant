from random import randint


class Gladiator:
    def __init__(self, health, rage, damage_low, damage_high, name):
        """ (Gladiator) -> str
        Gladiators health is 100 and rage is 15 after attack
        """
        self.health = 100
        self.rage = 0
        self.damage_low = damage_low
        self.damage_high = 20
        self.name = name

    def __str__(self):
        return '{}: {} Health || {}  Rage'.format(self.name, self.health,
                                                  self.rage)

    def attack(self, other):
        """ dict, dict -> None 
        Modifies the existing dictionaries for the attacker and defender

        -Each attack can hit normal or critical
        -Critical chance is the same as the attacker's rage
        (50 rage == 50% crit chance)
        - Damage dealt is a random integer between the attacker's
        damage\low and damage\_high
        -Critting doubles damage dealt
        -If gladiator crits, their rage is reset to 0
        -If gladiator hits normally, their rage is +15
        """
        hit = randint(self.damage_low, self.damage_high)
        if self.rage > randint(1, 100):
            other.health = max(0, other.health - (2 * hit))
            self.rage = 0
        else:
            other.health = max(0, other.health - hit)
            self.rage = min(100, self.rage + 15)

    # def super_sting(self, other):
    #     """(dict), dict -> (Nonetype)
    #     big hit
    #     """
    #     punch = (self.damage_high)
    #     if self.rage > randint(25, 100):
    #         other.health = max(0, other.health - (3 * punch))
    #     else:
    #         other.health = max(0, other.health - punch)
    #         self.rage = min(100, self.rage + 25)

    def heal(self):
        """
        -Spends 10 rage to heal 5 health
        -Cannot heal above max health of 100
        """
        if self.rage >= 10:
            self.rage -= 10
            self.health = min(100, self.health + 5)

    def is_dead(self):
        """
        Returns True iff gladiator has no health.
        """
        return self.health <= 0
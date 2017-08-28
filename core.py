from random import randint


class Gladiator:
    def __init__(self, health, rage, damage_low, damage_high):
        """ (Gladiator) -> str
        Gladiators health is 100 and rage is 15 after attack
        """
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def __str__(self):
        """(Gladiator) -> str
       Returns the string of the health status
       """
        return (
            '{}: Health || {}   Rage || {} \n{}: Health || {}   Rage || {}'.
            format(gladiator_1['Name'], gladiator_1['Health'],
                   gladiator_1['Rage'], gladiator_2['Name'],
                   gladiator_2['Health'], gladiator_2['Rage']))

    def attack(self, defender):
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
        hit = randint(self.Damage_Low, self.Damage_High)
        if self.Rage > randint(1, 100):
            defender['Health'] = max(0, defender['Health'] - (2 * hit))
            self.Rage = 0
        else:
            defender['Health'] = max(0, defender['Health'] - hit)
            self.Rage = min(100, self.Rage + 15)

    # def super_punch():
    #     """ if rage == 35 then you can use
    #     super punch
    #     """
    #     if self.rage >= 35:
    #         self.rage -= 20

    def heal(self):
        """
        -Spends 10 rage to heal 5 health
        -Cannot heal above max health of 100
        """
        if self.Rage >= 10:
            self.Rage -= 10
            self.Health = min(100, self.Health + 5)

    def is_dead(self):
        """
        Returns True iff gladiator has no health.
        """
        return self.Health <= 0
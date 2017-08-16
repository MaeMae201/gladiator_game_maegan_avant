import random
from random import randint


def new_gladiator(name, health, rage, damage_low, damage_high):
    """
    -Health = an int. between (0, 100)
    -Rage = an int. between (0, 100)
    -damage_low = int
    -damage_high = int
    Returns dictionary representing the gladiator with the
    provided values.
    """
    gladiator = {
        'Name': name,
        'Health': health,
        'Rage': rage,
        'Damage Low': damage_low,
        'Damage High': damage_high
    }

    return gladiator


def attack(gladiator):
    """
    -Each attack can hit normal or critical
    -Critical chance is the same as the attacker's rage
    (50 rage == 50% crit chance)
    - Damage dealt is a random integer between the attacker's
    damage\low and damage\_high
    -Critting doubles damage dealt
    -If gladiator crits, their rage is reset to 0
    -If gladiator hits normally, their rage is +15
    """
    normal = randint(gladiator['Damage Low'], gladiator['Damage High'])
    crit = normal * 2
    attack = random.choice([normal, crit])
    if attack == normal:
        gladiator['Health'] -= normal
        gladiator['Rage'] += 15
    elif attack == crit:
        gladiator['Health'] -= crit
        gladiator['Rage'] = 0


def heal(gladiator):
    """
    -Spends 10 rage to heal 5 health
    -Cannot heal above max health of 100
    """
    if gladiator['Rage'] >= 10:
        gladiator['Rage'] -= 10
        gladiator['Health'] += 5
        gladiator['Health'] <= 100
    return gladiator


def is_dead(gladiator):
    """
    Returns True iff gladiator has no health.
    """
    if gladiator['Health'] == 0:
        return True
    else:
        return False

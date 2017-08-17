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
        'Damage_Low': damage_low,
        'Damage_High': damage_high
    }

    return gladiator


def attack(attacker, defender):
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
    hit = randint(attacker['Damage_Low'], attacker['Damage_High'])
    if attacker['Rage'] > randint(1, 100):
        defender['Health'] = max(0, defender['Health'] - (2 * hit))
        attacker['Rage'] = 0
    else:
        defender['Health'] = max(0, defender['Health'] - hit)
        attacker['Rage'] = min(100, attacker['Rage'] + 15)


def heal(gladiator):
    """
    -Spends 10 rage to heal 5 health
    -Cannot heal above max health of 100
    """
    if gladiator['Rage'] >= 10:
        gladiator['Rage'] -= 10
        gladiator['Health'] = min(100, gladiator['Health'] + 5)


def is_dead(gladiator):
    """
    Returns True iff gladiator has no health.
    """
    return gladiator['Health'] <= 0

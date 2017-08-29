import core, shell


#these tests ran without using class but now they dont !!!!
def test_new_gladiator():
    health = 100
    rage = 0
    damage_low = 10
    damage_high = 20
    gladiator = core.new_gladiator('name', health, rage, damage_low,
                                   damage_high)
    assert gladiator['Health'] == 100
    assert gladiator['Rage'] == 0
    assert gladiator['Damage_High'] >= gladiator['Damage_Low']
    assert gladiator['Damage_High'] <= 20
    assert gladiator['Damage_Low'] >= 10


def test_attack():
    attacker = {'Health': 100, 'Rage': 0, 'Damage_Low': 15, 'Damage_High': 15}
    defender = {'Health': 100, 'Rage': 0, 'Damage_Low': 10, 'Damage_High': 20}
    core.attack(attacker, defender)
    assert attacker['Rage'] == 15
    assert defender['Health'] == 85


def test_heal():
    gladiator = {'Health': 100, 'Rage': 0}
    core.heal(gladiator)
    assert gladiator['Rage'] >= 0
    assert gladiator['Health'] == 100


def test_is_dead():
    gladiator = {'Health': 0}
    core.is_dead(gladiator)
    assert gladiator['Health'] <= 0
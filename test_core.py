import core, shell


def test_new_gladiator(gladiator):
    health = 100
    rage = 0
    damage_low = 10
    damage_high = 20
    gladiator == {
        'Health': health,
        'Rage': rage,
        'Damage_Low': damage_low,
        'Damage_High': damage_high
    }
    assert gladiator
    True


def test_attack(attacker, defender):
    attacker == {'health': 100, 'rage': 0, 'Damage_Low': 10, 'Damage_High': 20}
    assert attacker['Rage'] > randint(1, 100)
    True
    assert attacker['Rage'] == min(100, attacker['Rage'] + 15)
    True


# def test_heal():


def test_is_dead():
    assert attacker['Health'] == -1
    False
    assert attacker['Health'] == 0
    True
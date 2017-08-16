import core
import time, sys
from random import randint


def main():

    typing_speed = 10

    def slow_type(t):
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(typing_speed / 970.0)
        return input()

    print('\nGet Ready To Fight...\n\n')
    time.sleep(1)

    health = 100
    rage = 50
    damage_low = 20
    damage_high = 30

    # values = core.new_gladiator(health, rage, damage_low, damage_high)
    # for key, value in values.items():
    #     print('*', key, '-----', value)
    # attacker = values
    # defender = values

    print('Gladiator_1 its your turn to begin')

    # gladiator = core.attack(attacker, defender)
    # print(gladiator)

    choice = '\n Whats your move fighter?\n -attack\n -heal\n'
    attacker = core.new_gladiator(health, rage, damage_low, damage_high)
    for key, value in attacker.items():
        print('*', key, '-----', value, '\n')
    defender = core.new_gladiator(health, rage, damage_low, damage_high)
    print('Gladiator_2')
    for key, value in defender.items():
        print('*', key, '-----', value, '\n')

    decision = input(choice)
    if decision == 'attack':
        decision = core.attack(attacker, defender)
        print(decision)

    if decision == 'heal':
        decision = core.heal(gladiator)
        print(choice)


if __name__ == '__main__':
    main()
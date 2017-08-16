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
    time.sleep(1.5)

    health = 100
    rage = 0
    damage_low = 10
    damage_high = 20

    while True:
        gladiator_1 = core.new_gladiator('Player 1', health, rage, damage_low,
                                         damage_high)
        gladiator_2 = core.new_gladiator('Player 2', health, rage, damage_low,
                                         damage_high)

        print('*************************************************************')
        print('{}: Health:{}, Rage:{}, || {}: Health:{}, Rage:{} '.format(
            gladiator_1['Name'], gladiator_1['Health'], gladiator_1['Rage'],
            gladiator_2['Name'], gladiator_2['Health'], gladiator_2['Rage']))
        print('_____________________________________________________________')
        time.sleep(1.3)

        print('\n\nPlayer 1 is Up!\n\n')
        time.sleep(1)
        decision = slow_type(
            '\n\n Whats your move fighter?\n\n\n -Attack\n -Heal\n\n')

        if decision == 'attack'.lower():
            core.attack(gladiator_1)

        elif decision == 'heal'.lower():
            core.heal(gladiator_1)

        elif health == 0:
            core.is_dead(gladiator_1)
            print('Game Over', '{}', 'wins!')
            break

######################################PLAYER 2##################################
        while True:
            print(
                '*************************************************************'
            )
            print('{}: Health:{}, Rage:{}, || {}: Health:{}, Rage:{} '.format(
                gladiator_1['Name'], gladiator_1['Health'], gladiator_1[
                    'Rage'], gladiator_2['Name'], gladiator_2['Health'],
                gladiator_2['Rage']))
            print(
                '_____________________________________________________________'
            )
            time.sleep(1.3)

            print('\n\nPlayer 2 is Up!\n\n')
            time.sleep(1)
            decision = slow_type(
                '\n\n Whats your move fighter?\n\n\n -Attack\n -Heal\n\n')

            if decision == 'attack'.lower():
                core.attack(gladiator_2)

            elif decision == 'heal'.lower():
                core.heal(gladiator_2)

            elif health == 0:
                core.is_dead(gladiator_2)
                print('Game Over', '{}', 'wins!')
                break

if __name__ == '__main__':
    main()
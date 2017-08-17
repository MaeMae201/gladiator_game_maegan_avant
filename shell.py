import core, time, sys
from random import randint


def slow_type(t):
    typing_speed = 10
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()


def get_move():
    ''' gets the user decision for which move to do '''
    while True:
        decision = slow_type(
            '\n Whats your move fighter?\n -Attack\n -Heal\n').strip().lower()
        if decision in ['attack', 'heal\n']:
            return decision
        print('Invalid choice!')


def main():
    print('\nGet Ready To Fight...\n')
    time.sleep(1.5)

    health = 100
    rage = 0
    damage_low = 10
    damage_high = 20
    gladiator_1 = core.new_gladiator('Player 1', health, rage, damage_low,
                                     damage_high)
    gladiator_2 = core.new_gladiator('Player 2', health, rage, damage_low,
                                     damage_high)
    while True:
        print(
            '\n*************************************************************')
        print('{}: Health:{}, Rage:{}, \n{}: Health:{}, Rage:{}'.format(
            gladiator_1['Name'], gladiator_1['Health'], gladiator_1['Rage'],
            gladiator_2['Name'], gladiator_2['Health'], gladiator_2['Rage']))
        print('_____________________________________________________________')
        time.sleep(.5)

        print('\nPlayer 1 is Up!\n')
        time.sleep(1)
        decision = get_move()

        if decision == 'attack':
            core.attack(gladiator_1, gladiator_2)
        elif decision == 'heal':
            core.heal(gladiator_1)

        if core.is_dead(gladiator_2):
            print('\nGame Over -_- Gladiator 1 wins!')
            exit()

######################################PLAYER 2##################################
        print(
            '\n*************************************************************')
        print('{}: Health:{}, Rage:{}, \n{}: Health:{}, Rage:{}'.format(
            gladiator_1['Name'], gladiator_1['Health'], gladiator_1['Rage'],
            gladiator_2['Name'], gladiator_2['Health'], gladiator_2['Rage']))
        print('_____________________________________________________________')
        time.sleep(.5)

        print('\nPlayer 2 is Up!\n')
        time.sleep(1)
        decision = get_move()

        if decision == 'attack':
            core.attack(gladiator_2, gladiator_1)
        elif decision == 'heal':
            core.heal(gladiator_2)

        if core.is_dead(gladiator_1):
            print('\nGame Over ~_~ Gladiator 2 wins!')
            exit()

if __name__ == '__main__':
    main()
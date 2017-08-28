import core, time, sys
from random import randint


def slow_type(t):
    typing_speed = 10
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()


def get_move(Gladiator):
    ''' gets the user decision for which move to do '''
    while True:
        decision = slow_type(
            '\n              -Attack \n              -Heal\n >>>').strip(
            ).lower()
        if decision in ['attack', 'heal']:
            return decision
        print('~~~~~~~~~~~~~~~Invalid choice!~~~~~~~~~~~~~~~')


def main():
    print('\n        ...Get Ready To Fight...\n')
    time.sleep(1.5)

    gladiator_1 = core.Gladiator('Gladiator 1', health, rage, damage_low,
                                 damage_high)
    gladiator_2 = core.Gladiator('Gladiator 2', health, rage, damage_low,
                                 damage_high)
    while True:
        print('\n***********************************************')
        print('{}: Health || {}  Rage || {} \n{}: Health || {}  Rage || {}'.
              format(gladiator_1['Name'], gladiator_1['Health'], gladiator_1[
                  'Rage'], gladiator_2['Name'], gladiator_2['Health'],
                     gladiator_2['Rage']))
        print('_______________________________________________')
        time.sleep(.5)

        print('\n              Gladiator 1:')
        time.sleep(1)
        decision = get_move(Gladiator)

        if decision == 'attack':
            gladiator_1.attack(gladiator_2)
        elif decision == 'heal':
            gladiator_1.heal()
        if gladiator_2.is_dead():
            print('\nGame Over -_- Gladiator 1 wins!')
            exit()

######################################PLAYER 2##################################
        print('\n***********************************************')
        print('{}: Health || {}   Rage || {} \n{}: Health || {}   Rage || {}'.
              format(gladiator_1['Name'], gladiator_1['Health'], gladiator_1[
                  'Rage'], gladiator_2['Name'], gladiator_2['Health'],
                     gladiator_2['Rage']))
        print('_______________________________________________')
        time.sleep(.5)

        print('\n             Gladiator 2:')
        time.sleep(1)
        decision = get_move(Gladiator)

        if decision == 'attack':
            gladiator_2.attack(gladiator_1)
        elif decision == 'heal':
            gladiator_2.heal()

        if gladiator_1.is_dead():
            print('\nGame Over ~_~ Gladiator 2 wins!')
            exit()

if __name__ == '__main__':
    main()
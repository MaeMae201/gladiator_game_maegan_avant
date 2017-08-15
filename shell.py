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

    health = randint(0, 100)
    rage = randint(0, 100)
    damage_low = randint(0, 25)
    damage_high = randint(25, 50)

    values = core.new_gladiator(health, rage, damage_low, damage_high)
    for key, value in values.items():
        print('*', key, '-----', value)


if __name__ == '__main__':
    main()
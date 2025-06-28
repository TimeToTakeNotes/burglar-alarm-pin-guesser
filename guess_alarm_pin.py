from typing import List
from itertools import product # Generates all possible combos.

class GuessAlarmPin:
    def guess_pins(self, total_digits: int = 4) -> List[str]:
        digits = ['5', '7']
        pins = []

        # Generates all PIN combos: 
        for p in product(digits, repeat=total_digits): # Iterates through all possible digits
                pin = ''.join(p)
                
                if pin not in {'5555', '7777'}: # Exclude pins in set
                    pins.append(pin) # Joins digits into 1 str and adds to an array of pins

        return pins

# Script entry point
if __name__ == '__main__':
    guesser = GuessAlarmPin()
    possible_pins = guesser.guess_pins()

    print("Possible Pins:")
    for pin in possible_pins:
        print(pin)

    print(f'Total Number of Guesses: {len(possible_pins)}')
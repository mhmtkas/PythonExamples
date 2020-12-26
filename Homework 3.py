import random

word_list = ['wares', 'soup', 'mount', 'extend', 'brown', 'expert', 'tired', 'humidity', 'backpack', 'escalate',
             'mutter', 'desert', 'memento', 'kayak', 'homeless', 'medley',
             'packet', 'tickle', 'coming', 'leave', 'swing', 'thicket', 'reserve', 'murder', 'costly', 'corduroy',
             'bump', 'oncology', 'swatch', 'rundown', 'steal', 'teller',
             'cable', 'oily', 'official', 'abyss', 'schism', 'while', 'jaguar', 'seminary', 'command', 'cassette',
             'draw', 'anchovy', 'scream', 'blush', 'organic', 'applause',
             'parallel', 'trolley', 'pathos', 'origin', 'hang', 'pungent', 'angular', 'stubble', 'painted', 'forward',
             'saddle', 'muddy', 'orchid', 'prudence', 'disprove',
             'yiddish', 'lobbying', 'neuron', 'tumor', 'haitian', 'swift', 'mantel', 'wardrobe', 'consist', 'storied',
             'extreme', 'payback', 'control', 'dummy', 'influx', 'realtor',
             'detach', 'flake', 'consign', 'adjunct', 'stylized', 'weep', 'prepare', 'pioneer', 'tail', 'platoon',
             'exercise', 'dummy', 'clap', 'actor', 'spark', 'dope', 'phrase',
             'welsh', 'wall', 'whine', 'fickle', 'wrong', 'stamina', 'dazed', 'cramp', 'filet', 'foresee', 'seller',
             'award', 'mare', 'uncover', 'drowning', 'ease', 'buttery', 'luxury',
             'bigotry', 'muddy', 'photon', 'snow', 'oppress', 'blessed', 'call', 'stain', 'amber', 'rental', 'nominee',
             'township', 'adhesive', 'lengthy', 'swarm', 'court', 'baguette',
             'leper', 'vital', 'push', 'digger', 'setback', 'accused', 'taker', 'genie', 'reverse', 'fake', 'widowed',
             'renewe']


def random_word():
    random_word = random.choice(word_list).upper()
    return random_word


def display_hangman(tries):
    steps = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,

        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,

        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,

        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,

        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,

        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,

        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return steps[tries]


def play(word):
    tries = 6
    print(display_hangman(tries))
    words_char = word.upper()
    len_word = len(words_char)
    empty = list(len_word * "_")
    print(empty)
    charList = []
    while 1:
        char = input("\nPlease make guess a word or character:  ").upper()

        if charList.count(char) > 0:
            print(f"You tried '{char}' before.")
            continue
        else:
            charList.append(char)
        if len(char) > 1:
            if char == words_char:
                print(f"Congrats. You found '{words_char}'")
                break
            else:
                print("Wrong Guess\n")
                tries = tries - 1
                print(display_hangman(tries))
                if tries == 0:
                    print("You lost the game.")
                    break
        elif len(char) == 1:
            detect = -1
            for i, char1 in enumerate(words_char):
                if char1 == char:
                    detect = i
                    empty[i] = char1
            if detect == -1:
                tries = tries - 1
                print(display_hangman(tries))
                if tries == 0:
                    print("You lost the game.")
                    break

            print("\n"+ str(empty))
            if empty==list(words_char):
                print(f"Congrats. You found '{words_char}'")
                break
        else:
            print("Try again")

    print(f"The word was '{words_char}'")


if __name__ == '__main__':
    user_name = input("Enter The Player Name: ")
    print(f"\nWelcome {user_name}")
    play(random_word())
    while 1:
        decision = input("\n\nWant to play again?(Y/N)")
        if decision == 'y':
            play(random_word())
        elif decision == 'n':
            print("End Game.")
            break
        else:
            print("Invalid Input")

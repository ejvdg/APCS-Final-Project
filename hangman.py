class Hangman(object):

    def __init__(self):
        self.correct = False
        self.f = open("hangman_word.txt", 'r')
        self.letter_list = []
        self.already_guesses = []
        self.guesses = 5
        for word in self.f:
            for letters in word:
                letters = letters.lower()
                if letters == '!' or letters == '.' or letters == ',' or letters == '\'' or letters == '-' or letters == '?' or letters == " ":
                    pass
                else:
                    self.letter_list.append(letters)

    def showing(self):
        og_word = None
        f = open("hangman_word.txt", 'r')
        for word in f:
            og_word = word
            og_word = og_word.lower()
            word = word.lower()
            for letters in word:
                if letters not in self.already_guesses:
                    if letters == '!' or letters == '.' or letters == ',' or letters == '\'' or letters == '-' or letters == " ":
                        pass
                    else:
                        og_word = og_word.replace(f'{letters}','_')

        print(og_word)

    def already_guessed(self,ans) -> bool:
        if ans in self.already_guesses:
            return True
        return False

    def add_to_guessed(self,ans):
        self.already_guesses.append(ans)

    def is_guess_correct(self, ans) -> bool:
        if ans in self.letter_list:
            self.already_guesses.append(f'{ans}')
            return True
        return False

    def all_letters_right(self):
        for letters in self.letter_list:
            if letters in self.already_guesses:
                continue
            else:
                return False
        return True

    def get_guesses(self):
        return self.guesses

    def minus_a_try(self):
        self.guesses -= 1

    def did_user_lose(self) -> bool:
        if self.guesses <= 0:
            words = None
            for word in self.f:
                words = word
            print(f'The word was {words}')
        return self.guesses <= 0





hangman = Hangman()
while(True):
    # Use this break statement if running tests
    break
    hangman.showing()
    ans = input('What is your guess? ')
    ans = ans.lower()
    if(hangman.already_guessed(ans)):
        print("You already guessed this letter.")
    else:
        if(hangman.is_guess_correct(ans)):
            hangman.add_to_guessed(ans)
            print("You got the letter correct!")
            if hangman.all_letters_right():
                print('YOU WON!')
                break
        else:
            hangman.add_to_guessed(ans)
            hangman.minus_a_try()
            print("You got the letter wrong!")
            if hangman.did_user_lose():
                print("You lost!")
                break

import random

class Random_password:
    def __init__(self):
        self.letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}',
                   '|']
        self.letter_input = 3
        self.numbers_input = 3
        self.symbols_input = 3
        self.a = []
        self.b = []
        self.c = []
    def rand_pass(self):
        self.a.clear()
        for i in range(1, self.letter_input + 1):
            self.random_letters_formula = random.randint(0, 25)
            self.random_letters = self.letters[self.random_letters_formula]
            self.a.append(self.random_letters)
        self.b.clear()
        for j in range(1, self.numbers_input + 1):
            self.random_numbers_formula = random.randint(0, 9)
            self.random_numbers = self.numbers[self.random_numbers_formula]
            self.b.append(str(self.random_numbers))

        self.c.clear()
        for k in range(1, self.symbols_input + 1):
            self.random_symbols_formula = random.randint(0, 9)
            self.random_symbols = self.symbols[self.random_symbols_formula]
            self.c.append(self.random_symbols)

        self.abc = self.a + self.b + self.c
        random.shuffle(self.abc)
        self.password = ''.join(self.abc)
        return self.password





'''Generate a random password based on user input for the number of letters, numbers, and symbols.
This program prompts the user to input how many letters, numbers, and symbols they want in their password.
It then randomly selects characters, numbers, and symbols from predefined lists and combines them into a shuffled password.'''

import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|']
letter_input=int(input("How many letters you want:"))
numbers_input=int(input("How many numbers you want:"))                 
symbols_input=int(input("How many symbols you want:"))
a=[]
b=[]
c=[]
for i in range(1,letter_input+1):
    random_letters_formula=random.randint(0,25)
    random_letters=letters[random_letters_formula]
    a.append(random_letters)
for j in range(1,numbers_input+1):
    random_numbers_formula=random.randint(0,9)
    random_numbers=numbers[random_numbers_formula]
    b.append(str(random_numbers))
for k in range(1,symbols_input+1):
    random_symbols_formula=random.randint(0,9)
    random_symbols=symbols[random_symbols_formula]
    c.append(random_symbols)
abc=a+b+c
random.shuffle(abc)
password = ''.join(abc)
print(password)




    

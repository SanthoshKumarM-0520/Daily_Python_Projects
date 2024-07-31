import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")

word_code={row.letter:row.code for (index,row) in data.iterrows()}

user_inpt=input("Enter your word:").upper()
final=[word_code[letter] for letter in user_inpt]
print(final)


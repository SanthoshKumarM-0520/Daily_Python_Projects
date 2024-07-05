"""Caesar Cipher Implementation
This Python code encrypts or decrypts messages using a Caesar cipher with a specified shift value,
handling both encoding and decoding based on user input"""

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(message,shift,action):
    end_letter=""
    if action=="decode":
        shift*=-1
    for i in message:
        if i in letters:
            position=letters.index(i)
            new_position=position+shift
            end_letter+=letters[new_position]
        else:
            end_letter+=i
    print(end_letter)    
condition=True
while condition==True:
    
    action_input=input("type 'encode' to encrypt,type 'decode' to decrypt:\n ")
    message_input=input("Enter the message:\n").lower()
    shift_input=int(input("Enter the shift number:\n"))
    new_shift=shift_input%26
    caesar(action=action_input,shift=new_shift,message=message_input)
    again=input("Continue or not:\n")
    if again=="not":
        condition=False
        print("ok bye")



        

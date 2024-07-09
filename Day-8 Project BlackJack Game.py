def random_number_calc(turn):
    import random
    a={
        "ace":[1,11],
        "normal_numbers":[1,2,3,4,5,6,7,8,9],
        "kqj":["K","Q","J"]
    }

    keys=[]
    for i in a:
        keys.append(i)
    random_key=random.choice(keys)

    if turn=="user":
        if random_key=="ace":
            ace_input=int(input("You have drawn an ACE. Choose 11 or 1: "))
            return ace_input
        elif random_key=="kqj":
            random_kqj=random.choice(a[random_key])
            return random_kqj
            
        else:
            random_number=random.choice(a[random_key])
            return random_number

    elif turn=="computer":
        computer_sum=0
        computer_list=[]
        condition=1
        while condition==1:
            if random_key=="ace":
                adding=computer_sum+11
                if adding>21:
                    computer_list.append(1)
                    computer_sum+=1
                else:
                    computer_list.append(11)
                    computer_sum+=11
            elif random_key=="kqj":
                random_kqj=random.choice(a[random_key])
                if random_kqj=="K" or random_kqj=="Q" or random_kqj=="J":
                    computer_list.append(10)
                    computer_sum+=10                    
            else:                
                random_number=random.choice(a[random_key])
                computer_list.append(random_number)
                computer_sum+=random_number
            if computer_sum>=17:
                condition=0
        return computer_list            

print("Welcome to Blackjack...")
print("Ace is your choice; you can choose 11 or 1.")
print("Normal cards count as their number.")
print("King (K), Queen (Q), and Jack (J) all count as 10.")
enter_input=input("Type 'Enter' to start the game: ").lower()
if enter_input=="enter":
    
    first_user_cards=(random_number_calc(turn="user"),random_number_calc(turn="user"))
    change_list_first_user_cards=list(first_user_cards)    
    duplicate=change_list_first_user_cards.copy()
    len_change=len(duplicate)
    for s in range (len_change) :
        if duplicate[s]=="K" or duplicate[s]=="Q" or duplicate[s]=="J":
            duplicate[s]=10
    user_first_cards_adding=sum(duplicate)
    print(f"Your Cards: {change_list_first_user_cards} / Score: {user_first_cards_adding}")
    a=(random_number_calc(turn="computer"))
    computer_first_cards_adding=sum(a)
    print(f"Computer's Cards: {a[0]} X")    
    print("Do you want another card?")
    user_second_card_input=input("Type 'Yes' for another card or 'No' to challenge: ").lower()
    if user_second_card_input=="no":
        if user_first_cards_adding>21 and computer_first_cards_adding<=21:
            print("YOU LOSE")
            print(f"Computer's Cards: {a} / Score: {computer_first_cards_adding}")
            print(f"Your Cards: {change_list_first_user_cards} / Score: {user_first_cards_adding}")        
        elif user_first_cards_adding<computer_first_cards_adding:
            print("YOU LOSE")
            print(f"Computer's Cards: {a} / Score: {computer_first_cards_adding}")
            print(f"Your Cards: {change_list_first_user_cards} / Score: {user_first_cards_adding}")
        elif user_first_cards_adding>computer_first_cards_adding:
            print("YOU WIN")
            print(f"Computer's Cards: {a} / Score: {computer_first_cards_adding}")
            print(f"Your Cards: {change_list_first_user_cards} / Score: {user_first_cards_adding}")    
        elif user_first_cards_adding==computer_first_cards_adding:
            print("MATCH DRAW")
            print(f"Computer's Cards: {a} / Score: {computer_first_cards_adding}")
            print(f"Your Cards: {change_list_first_user_cards} / Score: {user_first_cards_adding}")
    elif user_second_card_input=="yes":
        b=random_number_calc(turn="user")
        change_list_first_user_cards.append(b)
        duplicate2=change_list_first_user_cards.copy()
        len_change1=len(duplicate2)        
        for u in range (len_change1):
            if duplicate2[u]=="K" or duplicate2[u]=="Q" or duplicate2[u]=="J": 
                duplicate2[u]=10 
        user_third_cards_adding=sum(duplicate2)
        if user_third_cards_adding>21 and computer_first_cards_adding<=21:
            print("YOU LOSE")
            print(f"Computer's Cards: {a} / Score: {computer_first_cards_adding}")
            print(f"Your Cards: {change_list_first_user_cards} / Score: {user_third_cards_adding}")                
        elif user_third_cards_adding<computer_first_cards_adding:
            print("YOU LOSE")
            print(f"Computer's Cards: {a} / Score: {computer_first_cards_adding}")
            print(f"Your Cards: {change_list_first_user_cards} / Score: {user_third_cards_adding}")
        elif user_third_cards_adding>computer_first_cards_adding:
            print("YOU WIN")
            print(f"Computer's Cards: {a} / Score: {computer_first_cards_adding}")
            print(f"Your Cards: {change_list_first_user_cards} / Score: {user_third_cards_adding}")    
        elif user_third_cards_adding==computer_first_cards_adding:
            print("MATCH DRAW")
            print(f"Computer's Cards: {a} / Score: {computer_first_cards_adding}")
            print(f"Your Cards: {change_list_first_user_cards} / Score: {user_third_cards_adding}")
else:
    print("Invalid command Re-start the game...")

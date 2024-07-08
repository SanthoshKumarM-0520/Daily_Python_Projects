"""This program allows users to participate in a secret auction by entering their names and bid amounts.
It then determines and prints the winner with the highest bid amount."""


def bidding_data_calc(bidding_data):
    bidding_value = 0
    winner_name = ""
    for name, bid_amount in bidding_data.items():
        if bid_amount > bidding_value:
            bidding_value = bid_amount
            winner_name = name
    print(f"The winner is {winner_name} with a bidding amount of ₹ {bidding_value}")        

print("Welcome to the Secret Auction Program")
bidding_data = {}
condition = True
while condition:
    name_input = input("Please enter your name: ")
    bid_input = int(input("Please enter your bid amount in ₹: "))
    bidding_data[name_input] = bid_input
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == "yes":
        condition = True
    elif more_bidders == "no":
        condition = False
    else:
        while more_bidders not in ["yes", "no"]:
            print("Please enter a valid command.")
            more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

bidding_data_calc(bidding_data)

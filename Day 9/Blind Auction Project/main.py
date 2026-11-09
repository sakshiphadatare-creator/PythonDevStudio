import art
print(art.logo)
# TODO-4: Compare bids in dictionary
def find_highest_bid(set_dict):
    highest_bid = 0
    winner = ""
    for bidder in set_dict:
        if highest_bid < set_dict[bidder]:
            highest_bid = set_dict[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# TODO-1: Ask the user for input
save_data = {}
person_add = True
while person_add:
    # TODO-1: Ask the user for input
    name = input("What's your name?: ")
    price = float(input("What's your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    save_data[name] = price
    new_person = input("Are there any other bidders? Type 'yes or 'no'.").lower()

    #TODO-3: Whether if new bids need to be added
    if new_person == "no":
        person_add =  False
        find_highest_bid(set_dict=save_data)
    else:
        person_add = True
        print("\n" * 20)



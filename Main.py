from Card import Card
from Teller import Teller

# region create cards
card_map: dict[int, Card] = {}

file = open("mock_credit.csv", "r")

# for each line in file
for x in file.readlines()[1:5]:

    # create card out of values
    card_info = x.split(",")

    card = Card(
        int(card_info[0]),
        card_info[1],
        card_info[2],
        card_info[3],
        card_info[4],
        card_info[5],
        float(card_info[6][1:-1]),
    )

    # add card to dict
    card_map[card.get_id()] = card

file.close()

# endregion

# instantiate teller
teller: Teller = Teller()

# select card to insert
test_num = 1
test_card = card_map[test_num]

# test_card = Card(-1, "John Doe", "1234567890123456", "2023-04", "084", "visa", 200)

# insert card
teller.receive_card(test_card)

# check balance
teller.check_balance()

# deposit $100
teller.deposit(100)

# withdraw $100
teller.withdraw(100)

# eject card
teller.eject_card()

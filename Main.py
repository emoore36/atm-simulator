from Card import Card
from Teller import Teller

# region create cards
card_map: dict[int, Card] = {}

file = open("mock_credit.csv", "r")

# for each line in file
for x in file.readlines()[1:]:

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

input_str: str = ""

while input_str.lower() != any(["quit", "q"]):
    input_str = input("What would you like to do? ")
    input_str.lower().strip()

    if (
        input_str == "quit"
        or input_str == "q"
        or input_str == "exit"
        or input_str == "e"
    ):

        # persist changes to csv
        file = open("mock_credit.csv", "w")
        file.write("id,name,number,expiration,cvv,brand,balance\n")
        for x in card_map:
            card: Card = card_map[x]
            card_str: str = str.format(
                "{},{},{},{},{},{},{}\n",
                str(card.get_id()),
                card.get_name(),
                card.get_number(),
                card.get_expiration(),
                card.get_cvv(),
                card.get_brand(),
                card.get_balance(),
            )
            file.write(card_str)

        break

    if input_str == "insert" or input_str == "insert card":
        card_id: int = int(input("Enter card ID: "))

        card: Card = card_map.get(card_id)

        if card is None:
            print("Card not found. Please try again.")
            continue

        else:
            teller.receive_card(card)

            while input_str != "eject":

                input_str = input(
                    "Would you like to deposit, withdraw, check balance, or eject? "
                )
                input_str.lower().strip()

                if input_str == "dep" or input_str == "deposit" or input_str == "d":
                    dep_amt = float(input("Enter amount to deposit: "))
                    teller.deposit(dep_amt)
                    continue

                if (
                    input_str == input_str == "with"
                    or input_str == "withdraw"
                    or input_str == "w"
                ):
                    with_amt = float(input("Enter amount to withdraw: "))
                    teller.withdraw(with_amt)
                    continue

                if (
                    input_str == "check"
                    or input_str == "check balance"
                    or input_str == "bal"
                    or input_str == "balance"
                    or input_str == "check bal"
                    or input_str == "chkbal"
                ):
                    teller.check_balance()
                    continue

                if input_str == "eject":
                    teller.eject_card()
                    break

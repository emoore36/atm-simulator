from Card import Card
from datetime import date


class Teller:
    def __init__(self) -> None:
        """Initializes the teller object."""
        self._inserted_card: Card = None

    def receive_card(self, card: Card) -> bool:
        """Inserts card into teller for card data manipulation.

        Args:
            card (Card): The card to insert

        Returns:
            bool: if card insertion is successful
        """
        # Check if card exists
        if self._card_exists():
            return False

        # associate card with teller
        self._inserted_card = card

        # check if card is expired
        if self._card_expired():
            print("Card is expired. Cannot operate.")
            self._inserted_card = None
            return self.eject_card()

        # greet the user :D
        print(str.format("Welcome, {}.", self._inserted_card.get_name()))
        return True

    def eject_card(self) -> Card:
        """Ejects the inserted card from the teller, if one exists.

        Returns:
            Card: the card to eject
        """
        card: Card = None

        # check if card exists
        if self._card_exists():

            # dissociate card with teller and return card
            card = self._inserted_card
            self._inserted_card = None

        print(str.format("Card ejected. Have a nice day.", card))
        return card

    def check_balance(self) -> None:
        """Prints the balance of the inserted card."""
        # check if card is inserted
        if self._card_exists():
            print(str.format("Current balance: {}", self._inserted_card.get_balance()))

    def deposit(self, amt: float) -> bool:
        """Adds the given amount to the inserted card, if the amount is valid.

        Args:
            amt (float): the amount to deposit

        Returns:
            bool: if deposit was successful
        """
        # check if card is inserted
        if self._card_exists():

            # check if amount is negative
            if amt < 0:
                print("Cannot deposit negative amount.")
                return False

            # process deposit
            self._inserted_card.add(amt)
            print(
                str.format(
                    "Successfully deposited ${}. Current balance is now {}.",
                    amt,
                    self._inserted_card.get_balance(),
                )
            )
            return True

        return False

    def withdraw(self, amt: float) -> float:
        """Removes the given amount from the inserted card, if doing so does not leave a negative balance.

        Args:
            amt (float): the amount to withdraw

        Returns:
            float: the withdrawn amount
        """
        # check if card is inserted
        if self._card_exists():
            # check if amount is negative
            if amt < 0:
                print("Cannot withdraw negative amount.")
                return 0

            # check if subtracting amount will result in overdraft
            if float(self._inserted_card.get_balance()[1:]) - amt < 0:
                print("Not enough in account balance for withraw.")
                return 0

            # subtract amount
            self._inserted_card.subtract(amt)
            print(
                str.format(
                    "Successfully withdrew ${}. Current balance is now {}.",
                    amt,
                    self._inserted_card.get_balance(),
                )
            )
            return amt
        return 0

    def _card_exists(self) -> bool:
        """Checks if a card is inserted in this teller

        Returns:
            bool: if a card exists in this teller
        """
        return self._inserted_card is not None

    def _card_expired(self) -> bool:
        """Checks if inserted card is expired

        Returns:
            bool: if inserted card is expired
        """
        return self._inserted_card._expiration < str(date.today())

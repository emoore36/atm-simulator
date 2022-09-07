class Card:
    def __init__(
        self,
        id: int,
        name: str,
        number: str,
        expiration: str,
        cvv: str,
        brand: str,
        balance: float,
    ) -> None:
        """Initializes card with fine-grained attributes.

        Args:
            id (int): the card ID
            name (str): the name on the card
            number (str): the card number
            expiration (str): the expiration date of the card
            cvv (str): the Card Verification Value
            brand (str): the brand of the card
            balance (float): the amount of money associated with the card
        """
        self._id: int = id
        self._name: str = name
        self._number: str = number
        self._expiration: str = expiration
        self._cvv: str = cvv
        self._brand: str = brand
        self._balance: float = balance

    def __str__(self) -> str:
        """ToString representation of the card

        Returns:
            str: String representation of the card
        """
        return str.format(
            "{}_{}", self._name.replace(" ", ""), self.get_number_encoded()
        )

    def get_full_data(self) -> str:
        """Returns a string of all data associated with this card.

        Returns:
            str: all data associated with this card.
        """
        return str.format(
            "[id={}, name={}, number={}, expiration={}, cvv={}, brand={}, balance=${}]",
            self._id,
            self._name,
            self._number,
            self._expiration,
            self._cvv,
            self._brand,
            self._balance,
        )

    def get_id(self) -> int:
        """Returns the card id

        Returns:
            int: the card id
        """
        return self._id

    def get_name(self) -> str:
        """Returns the name on the card

        Returns:
            str: the name on the card
        """
        return self._name

    def get_number(self) -> str:
        """Returns the card number

        Returns:
            str: the card number
        """
        return self._number

    def get_number_encoded(self) -> str:
        """Returns an encoded format of the card number (for security)

        Returns:
            str: the card number in encoded form
        """
        return "xxxxxxxxxxxx" + self._number[-4:]

    def get_balance(self) -> str:
        """Returns the current balance on the card

        Returns:
            str: the current balance on the card
        """
        return str.format("${}", self._balance)

    def get_expiration(self) -> str:
        """Returns the expiration date of the card.

        Returns:
            str: the expiration date
        """
        return self._expiration

    def add(self, amt: float) -> None:
        """Adds the given amount to the current balance

        Args:
            amt (float): The amount to add
        """
        self._balance += amt

    def subtract(self, amt: float) -> None:
        """Subtracts the given amount from the current balance

        Args:
            amt (float): _description_
        """
        self._balance -= amt

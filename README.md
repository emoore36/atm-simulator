# atm-simulator

A small, personal project I built for fun in Python. Works with a CSV of fake credit cards generated with the help of [Mockaroo](https://www.mockaroo.com/) to simulate the functionality of an Automatic Teller Machine (ATM).

## Installation
This app should work with any installation of Python3.
- For Windows, download Python3 [here](https://www.python.org/downloads/windows/).
- For Mac, download Python3 [here](https://www.python.org/downloads/macos/).
- For Linux, download Python3 [here](https://www.python.org/downloads/source/), or run `sudo apt-get install python3` in a terminal window.

## Running
To run this app, simply open a command terminal inside the repo and type the following command: 
- Windows: `py Main.py`.
- Mac: `python Main.py`.
- Linux: `python3 Main.py`.

## Instructions for use
The first prompt will read, "What would you like to do?". The options for input are
- inserting a card ("insert", "insert card")
- quitting the program ("quit", "q", "exit", "e")

The "machine" will ask to input the ID of the card to affect. For now, this is any integer between 1 and 1000, as listed in the `mock_credit.csv` file.

Once the card is inserted, the options are as follows:
- Make a deposit ("dep", "deposit", "d").
  - It will ask for the amount (float) to add to the account.
  - It will reprimand negative values and ignore non-float-compliant values.
- Make a withdraw ("with", "withdraw", "w").
  - It will ask for the amount (float) to withdraw from the account
  - It will reprimand negative values and values greater than the current balance, and ignore non-float-compliant values.
- Check the card's account balance ("check", "check balance", "bal", "balance", "check bal", "chkbal").
- Eject the card ("eject").


## Notes
- Running this app will generate a `/__pycache__/` directory in the local repo. This is automatically ignored by the .gitignore file.

## Issues
- ~~A number of functional requirements in-scope demand user interaction in the command line. This is not yet implemented. Coming soon.~~
~~- One non-functional requirement in-scope demands that changes to a `Card` object are persisted to the .csv for saving. This is not yet implemented. Coming soon.~~
- One non-function requirement out-of-scope would demand a third-party database server (likely SQL-based). I may implement this in the future, but it is unlikely.

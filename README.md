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

## Notes
- Running this app will generate a /__pycache__/ directory in the local repo. This is automatically ignored by the .gitignore file.

## Issues
- A number of functional requirements in-scope demand user interaction in the command line. This is not yet implemented. Coming soon.
- One non-functional requirement in-scope demands that changes to a `Card` object are persisted to the .csv for saving. This is not yet implemented. Coming soon.
- One non-function requirement out-of-scope would demand a third-party database server (likely SQL-based). I may implement this in the future, but it is unlikely.

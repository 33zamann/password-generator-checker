# Password Generator and Checker

A simple Python CLI tool to test password strength against common security rules and generate randomized passwords.

## Features

- **Password Tester**: Checks a given password for length, uppercase letters, lowercase letters, numbers, and special characters.
- **Password Generator**: Creates a secure random password of any requested length (minimum 8 characters).

## Prerequisites

- Python 3.x installed on your system.

## How to Run

1. Clone or download this repository.
2. Open your terminal or command prompt in the project folder.
3. Run the script:

```bash
python Passwords.py



How the Code Works

The program is structured around three main functions inside Passwords.py:
1. main()

Handles the user interface loop:

    Prompts you to pick a mode (1 for testing, 2 for generating).

    If you choose Mode 1, it runs test_pass().

    If you choose Mode 2, it asks for your desired length (defaults to 12 if left blank) and runs gen_pass(length).

    Re-prompts the user if an invalid menu option is entered.

2. test_pass()

Evaluates password strength using regular expressions (re module):

    Prompts for a password input.

    Initializes an empty errors list.

    Checks against five criteria:

        Minimum 8 characters long (len()).

        Contains an uppercase letter ([A-Z]).

        Contains a lowercase letter ([a-z]).

        Contains at least one digit (\d).

        Contains at least one special character ([\W]).

    If any check fails, it appends a message to errors and prints all failing rules.

    If no checks fail, it outputs "Password is Strong".

3. gen_pass(length)

Generates a random password using random and string modules:

    Enforces a minimum length of 8 characters.

    Ensures rule compliance by picking at least one uppercase letter, lowercase letter, digit, and special character first.

    Fills the rest of the requested length with a random selection from all combined character sets.

    Shuffles the character array using random.shuffle() so the guaranteed characters aren't always at the beginning.

    Joins the characters into a string and prints it out.
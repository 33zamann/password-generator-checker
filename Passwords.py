import re
import random
import string


def main():
    while True:
        try:
            choice = (input("\nModes:\n1. Test a Password,\n2. Generate One\nEnter Mode: "))
            if choice in ["1", "test a password", "test password"]:
                test_pass()
                break
            elif choice in ["2", "generate One", "generate"]:
                length = int(input("Enter desired length of password: ")or 12)
                gen_pass(length)
                break
            else:
                print("NO Such Mode!!")
        except ValueError:
            print("Value Error!")
            pass

def test_pass():
    password = input("Enter Password to Check: ")
    errors = []
    if len(password) < 8:
        errors.append("Password is too small!!")
    if not re.search(r"[A-Z]", password):
        errors.append("Must include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        errors.append("Must include at least one lowercase letter.")
    if not re.search(r"\d", password):
        errors.append("Must include at least one digit.")
    if not re.search(r"[\W]", password):
        errors.append("Must include at least one special character.")

    if errors:
        print("\n".join(errors))
    elif len(errors) == 0:
        print("Password is Strong")


def gen_pass(length=12):
    if (length) < 8:
        raise ValueError("Length is too Small")
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    specials = "!@#$%^&*()_+=-[]{}:;|<>,.?"

    password_char = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(specials),
    ]

    all_char = uppercase + lowercase + digits + specials
    for _ in range(length - 4):
        password_char.append(random.choice(all_char))

    random.shuffle(password_char)
    generated_str = "".join(password_char)

    print(generated_str)

main()
import random
import string
from utils import append_data, read_data, write_data, init


def generate_password(
    length,
    use_special_chars=True,
    use_numbers=True,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_punctuation=True,
    use_symbols=True,
):
    if length < 4:
        print("Length must be at least 4 characters.")
        return 0
    else:
        characters = ""
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        if use_special_chars:
            characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
        if use_numbers:
            characters += string.digits
        if use_punctuation:
            characters += string.punctuation

        if not characters:
            print("At least one character type must be selected.")
            return ""

        password = "".join(random.choices(characters, k=length))
        append_data(password)
        return password


def generate_multiple_passwords(
    count,
    length,
    use_special_chars=True,
    use_numbers=True,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_punctuation=True,
    use_symbols=True,
):
    passwords = []
    for _ in range(count):
        password = generate_password(
            length,
            use_special_chars,
            use_numbers,
            use_uppercase,
            use_lowercase,
            use_digits,
            use_punctuation,
            use_symbols,
        )
        passwords.append(password)
    return passwords

from genrator import generate_password, generate_multiple_passwords
from utils import init, read_data, append_data


def main():
    while True:
        print(
            """
  ========== MENU ==========
  1. Generate Password 
  2. Generate Multiple Passwords
  3. Show All Passwords
  4. Exit
  ==========================
            """
        )
        try:
            choice = int(input("Please select an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

        if choice == 1:
            length = int(input("Enter password length (minimum 4): "))
            password = generate_password(length)
            if password and len(password) >= 4:
                print("Password generated successfully.", f"Your password: {password}")
            else:
                print("Password generation failed. Please enter a valid length.")
        elif choice == 2:
            length = int(input("Enter password length (minimum 4): "))
            count = int(input("Enter number of passwords to generate: "))
            if length < 4 or count < 1:
                print(
                    "Invalid input. Length must be at least 4 and count must be at least 1."
                )
            else:
                passwords = generate_multiple_passwords(count, length)
                print("Multiple passwords generated successfully.")
        elif choice == 3:
            print("All generated passwords:")
            passwords = read_data()
            for i in passwords:
                print(f" - {i}")
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    character_set = ''
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("The length must be a positive integer.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
            continue

        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        try:
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
            print(f"Generated password: {password}")
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

        another = input("Generate another password? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()

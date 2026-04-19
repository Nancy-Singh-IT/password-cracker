target_password = input("Enter password to crack: ")

with open("passwords.txt", "r") as file:
    for line in file:
        word = line.strip()

        print(f"Trying: {word}")

        if word == target_password:
            print(f"\nPassword found: {word}")
            break
    else:
        print("\nPassword not found in list")

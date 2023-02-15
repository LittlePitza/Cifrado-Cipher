# Cesar encriptation and decriptation

def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result


def decrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)

        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)

    return result


def main():

    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter choice(1/2): ")

        if choice == '1':
            text = input("Enter text: ")
            shift = int(input("Enter shift number: "))
            print("Encrypted text: " + encrypt(text, shift))

        elif choice == '2':
            text = input("Enter text: ")
            shift = int(input("Enter shift number: "))
            print("Decrypted text: " + decrypt(text, shift))

        elif choice == '3':
            exit(0)

        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()

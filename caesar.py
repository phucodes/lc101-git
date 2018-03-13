from helpers import alphabet_position, rotate_character

def encrypt(text, rot):

    alphabet_position(text)
    encrypted_message = rotate_character(text, rot)

    return encrypted_message

def main():
    text = input("Enter your code here: ")
    rot = input("Enter the key here (Must be a number): ")
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()
from helpers import alphabet_position, rotate_character

def encription_key(text, rot):

    counter = 0

    enc_key_phrase = ""

    enc_key_list = []

    counter = ((len(text)//len(rot))+1)

    enc_key_phrase += rot * counter

    enc_key_list = list(enc_key_phrase)

    return enc_key_list

def encrypt(text, rot):

    encryp_key = (encription_key(text, rot))

    encr_list = list(encryp_key)

    final_message = []

    hold_key = ""

    key_val = 0

    for char in text:

        if char.isalpha():

            hold_key = encr_list[key_val]

            encr_let = alphabet_position(hold_key)

            final_message.append(rotate_character(char, encr_let))

            key_val = int(key_val) + 1 

        else:

            final_message.append(char)

            key_val = key_val

    return "".join(final_message)

def main():

    text = input("Enter a message for cypher: ")

    rot = input("Cypher key (must not be nonalpha): ")

    print(encrypt(text, rot))

if __name__ == '__main__':

    main()
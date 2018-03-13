def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_up = alphabet.upper()
    char_position = ''

    for chars in text:
        if chars.isalpha():
            if chars.isupper():
                char_position =+ alphabet_up.find(chars)
            else:
                char_position =+ alphabet.find(chars)
        else:
            char_position += chars
        return char_position #this is an int

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_up = alphabet.upper()
    rotated = ''

    for chars in char:
        if chars.isalpha():
            char_pos = alphabet_position(chars) + int(rot)
            if chars.isupper():
                if char_pos < 26:
                    rotated = rotated + alphabet_up[char_pos]
                else:
                    rotated = rotated + alphabet_up[char_pos % 26]
            else:
                if char_pos < 26:
                    rotated = rotated + alphabet[char_pos]
                else:
                    rotated = rotated + alphabet[char_pos % 26]                
        else:
            rotated = rotated + chars
    return rotated

def encryption(text, rot):

    alphabet_position(text)
    encrypted_message = rotate_character(text, rot)

    return encrypted_message
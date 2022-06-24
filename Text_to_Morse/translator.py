from morse_code_alphabet import MORSE_CODE_DICT







def encrypt(user_input):
    cipher = ""
    for char in user_input:
        if char not in MORSE_CODE_DICT:
            cipher = cipher + char + ' '
        else:
            cipher = cipher + MORSE_CODE_DICT[char] + ' '
    return cipher

def decrypt(cipher):
    cipher += ' '
    citext = ''
    decipher = ''
    for letter in cipher:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext =  ''
    return decipher

def again(to_continue):
    again = input("Would you like to continue? Type 'y' to continue or 'n' to stop")
    if again == 'y':
        to_continue = True
    elif again == 'n':
        to_continue = False

to_continue = True
while to_continue:
    choice = input('Would you like to encrypt a message to morse or decrypt a message to english? Type encode to encode or decode to decode.').lower()
    if choice == 'encode':
        user_input = input("Provide a word that you would like to be translated into morse code.\n").upper()
        print(encrypt(user_input))
        agains = again()
        if not again:
            to_continue = False
    elif choice == 'decode':
        user_input = input("Provide morse code to decipher. \n")
        print(decrypt(cipher=user_input))
        agains = again()
        if not again:
            to_continue = False
    else:
        agains = again()
        if not again:
            to_continue = False



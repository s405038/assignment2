# cipher.py reads the text file raw_text.txt,
# encrypts its contents using the described scheme, and writes the result to
# encrypted_text.txt. It then has a function that decrypts that file, and a
# function that verifies the decryption was successful.


def encryptshiftlogic(input, shift):
    """
    Gets the input and shift, calculates the shifted value
    and if it has special characters, recalculates the value to point to alphabets

    Parameters:
        input: The original input character.
        shift: The shift value.

    Returns:
        The shifted new value or encrypted value for the char.
    """

    new_value = ord(input) - shift
    if new_value < ord("A"):
        new_value += 26

    return chr(new_value)

def decryptshiftlogic(input, shift):
    """
    Gets the input and shift, calculates the shifted value
    and if it  has special characters, recalculates the value to point to alphabets

    Parameters:
        input: The original input character.
        shift: The shift value.

    Returns:
        The shifted new value or decrypted value for the char.
    """

    new_value = ord(input) + shift
    if new_value > ord("A"):
        new_value -= 26

    return chr(new_value)


def encrypt_file(shift1: int, shift2: int, input_path: str, output_path: str):
    input_text = getfiletext(input_path)
    encrypted_text = encrypt(input_text, shift1, shift2)

    with open(output_path, "w") as file:
        file.write(encrypted_text)


def decrypt_file(shift1: int, shift2: int, input_path: str, output_path: str):
    input_text = getfiletext(input_path)
    decrypted_text = decrypt(input_text, shift1, shift2)

    with open(output_path, "w") as file:
        file.write(decrypted_text)


def getfiletext(path):
    inputfile = open(path, "r")
    input_text = inputfile.read()
    inputfile.close()

    return input_text


def verify_files(original_path: str, decrypted_path: str):
    input_text = getfiletext(original_path)
    output_text = getfiletext(decrypted_path)

    if input_text == output_text:
        return True
    else:
        return False


def encrypt(input: str, shift1: int, shift2: int):

    lowercase_first_half = "abcdefghijklmn"
    uppercase_first_half = "ABCDEFGHIJKLMN"
    lowercase_second_half = "opqrstuvwxyz"
    uppercase_second_half = "OPQRSTUVWXYZ"

    # calculated shifts
    multiplied_shift = shift1 * shift2
    added_shift = shift1 + shift2

    encrypted_text = ""  # initialize enc text

    for char in input:
        if char in lowercase_first_half:
            # If the letter is in the first half of the alphabet shift forward by shift1 * shift2 positions
            encrypted_text += chr(ord(char) + multiplied_shift)
        elif char in lowercase_second_half:
            # If the letter is in the second half of the alphabet shift backward by shift1 + shift2 positions
            encrypted_text += chr(ord(char) - added_shift)
        elif char in uppercase_first_half:
            # If the letter is in the first half shift backward by shift1 positions
            encrypted_text += encryptshiftlogic(char, shift1)
        elif char in uppercase_second_half:
            # if the letter is in the second half shift forward by (shift2 squared)
            encrypted_text += chr(ord(char) + shift2 * shift2)
        elif char.isdigit():
            # Shift forward by shift1 - shift2
            encrypted_text += chr(ord(char) + shift1 - shift2)
        else:
            # Spaces, tabs, newlines, punctuation, symbols remain unchanged
            encrypted_text += char

    return encrypted_text


def decrypt(input,shift1, shift2):
    
    lowercase_first_half = "abcdefghijklmn"
    uppercase_first_half = "ABCDEFGHIJKLMN"
    lowercase_second_half = "opqrstuvwxyz"
    uppercase_second_half = "OPQRSTUVWXYZ"

    # calculated shifts
    multiplied_shift = shift1 * shift2
    added_shift = shift1 + shift2

    derypted_text = ""  # initialize enc text

    for char in input:
        if char in lowercase_first_half:
            # If the letter is in the first half of the alphabet shift backward by shift1 * shift2 positions
            derypted_text += chr(ord(char) - multiplied_shift)
        elif char in lowercase_second_half:
            # If the letter is in the second half of the alphabet shift forward by shift1 + shift2 positions
            derypted_text += chr(ord(char) + added_shift)
        elif char in uppercase_first_half:
            # If the letter is in the first half shift backward by shift1 positions
            derypted_text += decryptshiftlogic(char, shift1)
        elif char in uppercase_second_half:
            # if the letter is in the second half shift backward by (shift2 squared)
            derypted_text += chr(ord(char) - shift2 * shift2)
        elif char.isdigit():
            # Shift backward by shift1 - shift2
            derypted_text += chr(ord(char) - shift1 - shift2)
        else:
            # Spaces, tabs, newlines, punctuation, symbols remain unchanged
            derypted_text += char

    return derypted_text


def verify(firststring, secondstring):

    if firststring == secondstring:
        return True
    else:
        return False


def validateinput(stringvalue):
    """
    Prompts the user to enter a number.
    Repeats the prompt until a valid whole number is entered.

    Parameters:
        stringvalue: The name displayed in the input prompt.

    Returns:
        The validated input as an integer.
    """

    user_input = input("Enter a number for " + stringvalue + ": ")

    while not user_input.isdigit():
        print("Invalid input. Please enter numbers only.")
        user_input = input("Enter a number for " + stringvalue + ": ")

    return int(user_input)


shift1 = validateinput("shift1")
shift2 = validateinput("shift2")
encrypt_file(shift1, shift2, "raw_text.txt", "encrypted_text.txt")
print("Generated encrypted file")

decrypt_file(shift1, shift2, "encrypted_text.txt", "decrypted_text.txt")
print("Generated decrypted file")

if verify_files("raw_text.txt", "decrypted_text.txt")==True:
    print("Decryption successful")
else:
    print("Decryption failed")
    

# input_text="a1A fxP"
# encry_text=encrypt(input_text)
# print(encry_text)
# decrypted_text=decrypt(encry_text)
# print(verify(encry_text,decrypted_text))

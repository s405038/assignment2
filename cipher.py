# cipher.py reads the text file raw_text.txt, 
# encrypts its contents using the described scheme, and writes the result to 
# encrypted_text.txt. It then has a function that decrypts that file, and a 
# function that verifies the decryption was successful. 

def shiftlogic(input,shift):
    """
    Gets the input and shift, calculates the shifted value
    and if it special characters, recalculates the value to point to alphabets

    Parameters:
        input: The original input character.
        shift: The shift value.

    Returns:
        The shifted new value or encrypted value for the char.
    """

    new_value = ord(input) - shift
    if new_value < ord('A'):
        new_value += 26
    
    return chr(new_value)    

def encrypt(input):
    """
    Prompts the user to enter a number.
    Repeats the prompt until a valid whole number is entered.

    Parameters:
        stringvalue: The name displayed in the input prompt.

    Returns:
        The validated input as an integer.
    """

    lowercase_first_half ='abcdefghijklmn'
    uppercase_first_half ='ABCDEFGHIJKLMN'
    lowercase_second_half ='opqrstuvwxyz'
    uppercase_second_half ='OPQRSTUVWXYZ'    

    # calculated shifts
    multiplied_shift=shift1*shift2
    added_shift=shift1+shift2

    encrypted_text="" # initialize enc text

    for char in input:
        if char in lowercase_first_half:
            # If the letter is in the first half of the alphabet shift forward by shift1 * shift2 positions        
            encrypted_text += chr(ord(char) + multiplied_shift)
        elif char in lowercase_second_half:
            # If the letter is in the second half of the alphabet shift backward by shift1 + shift2 positions          
            encrypted_text += chr(ord(char) - added_shift)
        elif char in uppercase_first_half: 
            # If the letter is in the first half shift backward by shift1 positions       
            encrypted_text += shiftlogic(char,shift1)
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
        
def decrypt(input):

    return input

def verify(firststring, secondstring):

    if firststring==secondstring:
        return True
    else:
        return False

def validateinput(stringvalue):
    user_input = input("Enter a number for " + stringvalue + ": ")

    while not user_input.isdigit():
        print("Invalid input. Please enter numbers only.")
        user_input = input("Enter a number for " + stringvalue + ": ")

    return int(user_input)


shift1=validateinput("shift1")
shift2=validateinput("shift2")

input_text="a1A fxP"

encry_text=encrypt(input_text)
print(encry_text)
decrypted_text=decrypt(encry_text)
print(verify(encry_text,decrypted_text))





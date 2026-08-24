"""
cipher.py reads the text file raw_text.txt,
encrypts its contents using the described scheme, and writes the result to
encrypted_text.txt. It then has a function that decrypts that file, and a
function that verifies the decryption was successful.

Encryption logic - 
• For lowercase letters: 
o If the letter is in the first half of the alphabets shift forward  by shift1 * shift2 positions 
o If the letter is in the second half of the alphabets shift backward  by shift1 + shift2 positions 

• For uppercase letters: 
o If the letter is in the first half shift backward by shift1 positions 
o If the letter is in the second half shift forward by shift2 squared positions 

• For digits Shift forward by shift1 - shift2 positions  

• Other characters: 
o Spaces, tabs, newlines, punctuation, symbols remain unchanged 
""" 

def shift_forward(char, characters, shift):
    """
    Calculates the forward shift by using modulus operator so that the char is within the dataset
    This helps in ensuring encrypt works properly and subsequent decrypt will work fine too
    """

    position = characters.index(char) # find position in character set
    new_position = (position + shift) % len(characters) # ensure shift is within character set
    return characters[new_position]  # return new character within set

def shift_backward(char, characters, shift):
    """
    Calculates the backward shift by using modulus operator so that the char is within the dataset
    This helps in ensuring decrypt logic works properly
    """

    position = characters.index(char) # find position in character set
    new_position = (position - shift) % len(characters) # ensure shift is within character set
    return characters[new_position] # return new character within set

def encrypt_file(shift1: int, shift2: int, input_path: str, output_path: str):
    """
    Writes encrypted file content to hard-disk based on provided file path as well
    as caclulating shift based on shift1 and shift2 values
    """
     
    input_text = get_file_text(input_path) # get file text from path
    encrypted_text = encrypt_or_decrypt_logic(input_text,shift1, shift2,"enc") # encrypt the text

    with open(output_path, "w") as file:
        file.write(encrypted_text) # write the contents to the encrypted file


def decrypt_file(shift1: int, shift2: int, input_path: str, output_path: str):
    """
    Writes decrypted file content to hard-disk based on provided file path as well
    as reversing the encrypt logic calculated using shift based on shift1 and shift2 values
    """
    input_text = get_file_text(input_path) # get file text from path
    decrypted_text = encrypt_or_decrypt_logic(input_text,shift1, shift2,"dec") # decrypt the text

    with open(output_path, "w") as file:
        file.write(decrypted_text) # write the decrypted contents to the file


def get_file_text(path):
    """
    Returns file content based on provided file path
    """
    input_file = open(path, "r") # open file in read only format
    input_text = input_file.read() # read contents of file and assign to a variable
    input_file.close() # close the file

    return input_text # return file contents or text

def verify_files(original_path: str, decrypted_path: str):
    """
    Gets two file paths and compares their conent to return a boolean value
    """
    input_text = get_file_text(original_path)
    output_text = get_file_text(decrypted_path)

    if input_text == output_text:
        return True
    else:
        return False

def encrypt_or_decrypt_logic(input,shift1, shift2,type):
    """
    Encrypts or decrypts the input text using the supplied shift values.

    Different shifting rules are applied using shift1 and shift2 numeric values to lowercase letters, uppercase
    letters, and digits. Decryption reverses the shifts used during encryption.
    Spaces, punctuation, and other special characters remain unchanged.

    Also, accepts "enc" or "dec" as type to do encryption or subsequent decryption
    """

    # different character sets
    lowercase_first_half = "abcdefghijklmn"
    uppercase_first_half = "ABCDEFGHIJKLMN"
    lowercase_second_half = "opqrstuvwxyz"
    uppercase_second_half = "OPQRSTUVWXYZ"
    digit_list="0123456789"    

    output_text="" # initialize the var that will hold the text

    match type:
        case "enc":
            for char in input:
                    if char in lowercase_first_half:
                        # If the letter is in the first half of the alphabet shift forward within boundaries
                        #  by shift1 * shift2 positions
                        multiplied_shift = shift1 * shift2
                        output_text += shift_forward(char,lowercase_first_half,multiplied_shift)
                    elif char in lowercase_second_half:
                        # If the letter is in the second half of the alphabet shift backward by shift1 + shift2 positions
                        added_shift = shift1 + shift2
                        output_text += shift_backward(char,lowercase_second_half,added_shift)
                    elif char in uppercase_first_half:
                        # If the letter is in the first half shift backward by shift1 positions
                        output_text += shift_backward(char,uppercase_first_half,shift1)
                    elif char in uppercase_second_half:
                        # if the letter is in the second half shift forward by (shift2 squared)
                        squared_shift=shift2 * shift2
                        output_text += shift_forward(char,uppercase_second_half,squared_shift)
                    elif char.isdigit():
                        # Shift forward by shift1 - shift2
                        subtracted_shift=shift1 - shift2
                        output_text += shift_forward(char,digit_list,subtracted_shift)
                    else:
                        # Spaces, tabs, newlines, punctuation, symbols remain unchanged
                        output_text += char
        case "dec":
            for char in input:
                    if char in lowercase_first_half:
                        # If the letter is in the first half of the alphabet shift backward by shift1 * shift2 positions
                        multiplied_shift = shift1 * shift2
                        output_text += shift_backward(char,lowercase_first_half,multiplied_shift)
                    elif char in lowercase_second_half:
                        # If the letter is in the second half of the alphabet shift backward by shift1 + shift2 positions
                        added_shift = shift1 + shift2
                        output_text += shift_forward(char,lowercase_second_half,added_shift)
                    elif char in uppercase_first_half:
                        # If the letter is in the first half shift backward by shift1 positions
                        output_text += shift_forward(char,uppercase_first_half,shift1)
                    elif char in uppercase_second_half:
                        # if the letter is in the second half shift forward by (shift2 squared)
                        squared_shift=shift2 * shift2
                        output_text += shift_backward(char,uppercase_second_half,squared_shift)
                    elif char.isdigit():
                        # Shift forward by shift1 - shift2
                        subtracted_shift=shift1 - shift2
                        output_text += shift_backward(char,digit_list,subtracted_shift)
                    else:
                        # Spaces, tabs, newlines, punctuation, symbols remain unchanged
                        output_text += char

    return output_text

def validate_input(string_value):
    """
    Prompts the user to enter a number.
    Repeats the prompt until a valid whole number is entered.

    Parameters:
        string_value: The name displayed in the input prompt.

    Returns:
        The validated input as a positive integer.
    """

    user_input = input("Enter a non-negative number for " + string_value + ": ")

    while not user_input.isdigit():
        print("Invalid input. Please enter non-negative numbers only.")
        user_input = input("Enter a non-negative number for " + string_value + ": ")

    return int(user_input)

print("\n*****************************************")
print("\nQuestion 1: Encryption/Decryption logic")
print("\n*****************************************\n")

shift1 = validate_input("shift1")
shift2 = validate_input("shift2")
encrypt_file(shift1, shift2, "raw_text.txt", "encrypted_text.txt")
print("\n- Generated encrypted file successfully")

decrypt_file(shift1, shift2, "encrypted_text.txt", "decrypted_text.txt")
print("- Generated decrypted file successfully")

print("\n*****************************************")
print("\nEnd-result: ")
print("\n-----------------------------------------\n")

if verify_files("raw_text.txt", "decrypted_text.txt")==True:
    print("\033[92mDecryption verification successful\033[0m")
else:
    print("\033[91mDecryption verification failed\033[0m") 

print("\n-----------------------------------------\n")   


# cipher.py reads the text file raw_text.txt, 
# encrypts its contents using the described scheme, and writes the result to 
# encrypted_text.txt. It then has a function that decrypts that file, and a 
# function that verifies the decryption was successful. 

def shiftlogic(input,shift1):
    new_value = ord(input) - shift1
    if new_value < ord('A'):
        new_value += 26
    
    return chr(new_value)    

def encrypt(input):
    lowercase_first_half ='abcdefghijklmn'
    uppercase_first_half ='ABCDEFGHIJKLMN'
    lowercase_second_half ='opqrstuvwxyz'
    uppercase_second_half ='OPQRSTUVWXYZ'    

    multiplied_shift=shift1*shift2
    added_shift=shift1+shift2
    encrypted_text=""

    for char in input:
        if char in lowercase_first_half:            
            encrypted_text += chr(ord(char) + multiplied_shift)
        elif char in lowercase_second_half:            
            encrypted_text += chr(ord(char) - added_shift)
        elif char in uppercase_first_half:            
            encrypted_text += shiftlogic(char,shift1)
        elif char in uppercase_second_half:            
            encrypted_text += chr(ord(char) + shift2 * shift2)
        elif char.isdigit():            
            encrypted_text += chr(ord(char) + shift1 - shift2)
        elif char==' ':
            encrypted_text += ' '

    return encrypted_text
        
def decrypt(input):
    return input

def verify(firststring, secondstring):

    if firststring==secondstring:
        return True
    else:
        return False

shift1=int(input("Input shift1 = "))
shift2=int(input("Input shift2 = "))

input_text="a1A fxP"

encry_text=encrypt(input_text)
print(encry_text)
decrypted_text=decrypt(encry_text)
print(verify(encry_text,decrypted_text))





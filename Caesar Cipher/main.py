alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(text, shift, direction):
  if direction == "encode".lower():
    encoded_pw = []
    for letter in text:        
      encoded_pw += alphabet[alphabet.index(letter) + shift]
    encoded_text = "".join(encoded_pw)
    print(f"The encoded text is {encoded_text}.")

  else:
    decoded_pw = []
    for letter in text:        
      decoded_pw += alphabet[alphabet.index(letter) - shift]
    decoded_text = "".join(decoded_pw)
    print(f"The decoded text is {decoded_text}.")
    
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)
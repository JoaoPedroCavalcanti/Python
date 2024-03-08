alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_and_decrypt(message, shift):
    final_text = ''
    encrypted_lettler_index = []
  
    for lettler in message:
        encrypted_lettler_index.append(alphabet.index(lettler) + shift)

    for index in encrypted_lettler_index:
        final_text += alphabet[index]
        
    return final_text


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
  encrypted_text = encrypt_and_decrypt(message, shift)
  print(f"Your encoded message is: {encrypted_text}")


elif direction == 'decode':
  shift = shift * (-1)
  decrypted_text = encrypt_and_decrypt(message, shift)
  print(f"Your decoded message is: {decrypted_text}")


  

  

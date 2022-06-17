alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cieaser(chosen_text, chosen_shift, direction_chosen):
    cipher_text = ""
    if direction == "decode":
        chosen_shift *= -1
    for char in chosen_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + chosen_shift
            new_char = alphabet[new_position]
            cipher_text += new_char
        else:
            cipher_text += char

    print(f"Here is the {direction_chosen} text {cipher_text}")


end = True
while end == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cieaser(chosen_text=text, chosen_shift=shift, direction_chosen=direction)
    ask = input("do you want to restart the program :")
    if ask == "no":
        end = False
    else:
        end = True
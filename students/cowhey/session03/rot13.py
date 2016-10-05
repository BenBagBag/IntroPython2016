def rot13(encrypted_str):
    translation_table = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    decoded_chars = []
    for char in encrypted_str:
        if char.isalpha():
            decoded_chars.append(char.translate(translation_table))
        else:
            decoded_chars.append(char)
    return ''.join(decoded_chars)


if __name__ == '__main__':
    assert(rot13("Zntargvp sebz bhgfvqr arne pbeare") == "Magnetic from outside near corner")
    assert(rot13("Gb trg gb gur bgure fvqr!") == "To get to the other side!")
    assert(rot13("V'z nffregvat gung gur EBG13 genafyngbe jbexf!") == "I'm asserting that the ROT13 translator works!")

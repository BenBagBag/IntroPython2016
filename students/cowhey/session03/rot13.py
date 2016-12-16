def rot13(encrypted_str):
    '''Return an unencrypted string that was encrypted with ROT13.
    Uses the str.maketrans() method'''
    translation_table = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    decoded_chars = []
    for char in encrypted_str:
        if char.isalpha():
            decoded_chars.append(char.translate(translation_table))
        else:
            decoded_chars.append(char)
    return ''.join(decoded_chars)


def shift_letter(letter):
    '''return unencrypted letter that has been encrypted with ROT13'''
    orig_ord = ord(letter)
    new_ord = orig_ord + 13
    if not letter.isalpha():
        return letter
    # range for upper case: 65 - 90 (inclusive)
    # range for lower case: 97 - 122 (inclusive)
    elif (65 <= new_ord <= 90 and letter.isupper()) or (97 <= new_ord <= 122 and letter.islower()):
        return chr(new_ord)
    else:
        return chr(new_ord - 26)


def rot13_from_scratch(encrypted_str):
    '''Return an unencrypted string that was encrypted with ROT13.
    Does not use the str.maketrans() method'''
    decoded_chars = []
    for char in encrypted_str:
        decoded_chars.append(shift_letter(char))
    return ''.join(decoded_chars)


if __name__ == '__main__':
    assert(rot13("Zntargvp sebz bhgfvqr arne pbeare") == "Magnetic from outside near corner")
    assert(rot13("Gb trg gb gur bgure fvqr!") == "To get to the other side!")
    assert(rot13("V'z nffregvat gung gur EBG13 genafyngbe jbexf!") == "I'm asserting that the ROT13 translator works!")
    assert(rot13_from_scratch("Zntargvp sebz bhgfvqr arne pbeare") == "Magnetic from outside near corner")
    assert(rot13_from_scratch("Gb trg gb gur bgure fvqr!") == "To get to the other side!")
    assert(rot13_from_scratch("V'z nffregvat gung gur EBG13 genafyngbe jbexf!") == "I'm asserting that the ROT13 translator works!")

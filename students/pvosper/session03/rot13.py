#!/usr/bin/env python3

print("Caesar Cypher")

alphabet = ("abcdefghijklmnopqrstuvwxyz")

def reconcile(index):
    while index not in range(len(alphabet)):
        if index < 0:
            index += len(alphabet)
        else:
            index -= len(alphabet)
    return index

def rotate_word(str, rot = 13):
    turned = ""
    for i in range(len(str)):
        if str[i].isalpha():
            if str[i].islower():
                index = reconcile(alphabet.find(str[i]) + rot)
                turned = turned + alphabet[index]
            else:
                index = reconcile(alphabet.find(str[i].lower()) + rot)
                turned = turned + alphabet[index].upper()
        else:
            turned = turned + str[i]
    return turned

def test():

    print("\nExample #1:\n")

    print("Zntargvp sebz bhgfvqr arne pbeare")
    print("-----")
    print(rotate_word("Zntargvp sebz bhgfvqr arne pbeare", 13))

    print("\nExample #2:\n")

    fortune_cookie = '''N PBQR BS RGUVPNY ORUNIVBE SBE CNGVRAGF:
    1. QB ABG RKCRPG LBHE QBPGBE GB FUNER LBHE QVFPBZSBEG.
    Vaibyirzrag jvgu gur cngvrag’f fhssrevat zvtug pnhfr uvz gb ybfr inyhnoyr fpvragvsvp bowrpgvivgl.
    2. OR PURRESHY NG NYY GVZRF.
    Lbhe qbpgbe yrnqf n ohfl naq gelvat yvsr naq erdhverf nyy gur tragyrarff naq ernffhenapr ur pna trg.
    3. GEL GB FHSSRE SEBZ GUR QVFRNFR SBE JUVPU LBH NER ORVAT GERNGRQ.
    Erzrzore gung lbhe qbpgbe unf n cebsrffvbany erchgngvba gb hcubyq.'''

    print(fortune_cookie)
    print("-----")
    print(rotate_word(fortune_cookie, 13))

if __name__ == "__main__":
    test()

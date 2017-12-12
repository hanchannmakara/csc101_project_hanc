from dictionary import*
from encryption import*
from decryption import *
from hanc_combined_codes import*

def testit(did_pass):
    """  Prints the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
def Hancsecurity_test_suit():
    #Test encryption
    print("\nThis is testing encryption algorithm.")
    hanc1 = HancSecurity()
    hanc1.key = 20
    hanc1.user_input = "Chann Makara Han"
    hanc1.crypt_type = "encrypt"
    testit(hanc1.crypting() == "LJBQQ KBFBIB JBQ")

    hanc2 = HancSecurity()
    hanc2.key = 40
    hanc2.user_input = "When people are sad, they cry."
    hanc2.crypt_type = "encrypt"
    testit(hanc2.crypting() == "VJGU AGWASG BRG CBF, XJGD MRD.")

    hanc3 = HancSecurity()
    hanc3.key = 10
    hanc3.user_input = "Today is a good day."
    hanc3.crypt_type = "encrypt"
    testit(hanc3.crypting() == "JKCHX ZP H WKKC CHX.")

    hanc4 = HancSecurity()
    hanc4.key = 75
    hanc4.user_input = "The world is changing faster than ever before."
    hanc4.crypt_type = "encrypt"
    testit(hanc4.crypting() == "RCB VKNMQ EO DCFLSELS JFORBN RCFL BIBN HBJKNB.")

    a = 55
    h = "What are you doing?"
    testit(encrypt(a, h) == "UQFA FOD ZEK BETXJ?")

    b = 88
    j = "When will you graduate from college?"
    testit(encrypt(b, j) == "VOJC VLWW IXR EKDGRDPJ SKXM QXWWJEJ?")

    c = 49
    k = "I am so hungry mother, is there any food leftover?"
    testit(encrypt(c, k) == "X BF GM WTEDAU FMRWLA, XG RWLAL BEU QMMK ZLQRMOLA?")

    d = 66
    l = "What is your name dude?"
    testit(encrypt(d, l) == "OAFU SR YXDM WFTJ CDCJ?")

    print("\nThis is testing decryption algorithm.")
    hanc5 = HancSecurity()
    hanc5.key = 17
    hanc5.user_input = "CHCH, W VJP IJR PCWN PWLS!"
    hanc5.crypt_type = "decrypt"
    testit(hanc5.crypting() == "HAHA, I GOT YOU THIS TIME!")

    hanc6 = HancSecurity()
    hanc6.key = 39
    hanc6.user_input = "ZSOY BOABWO FCO KFL, PSOI MCI."
    hanc6.crypt_type = "decrypt"
    testit(hanc6.crypting() == "WHEN PEOPLE ARE SAD, THEY CRY.")

    hanc7 = HancSecurity()
    hanc7.key = 71
    hanc7.user_input = "OKLHN TI H BKKL LHN."
    hanc7.crypt_type = "decrypt"
    testit(hanc7.crypting() == "TODAY IS A GOOD DAY.")

    hanc8 = HancSecurity()
    hanc8.key = 75
    hanc8.user_input = "RCB VKNMQ EO DCFLSELS JFORBN RCFL BIBN HBJKNB."
    hanc8.crypt_type = "decrypt"
    testit(hanc8.crypting() == "THE WORLD IS CHANGING FASTER THAN EVER BEFORE.")

    e = 33
    m = "ZMFO FNE ACU QCTKI?"
    testit(decrypt(e, m) == "WHAT ARE YOU DOING?")

    f = 11
    n = "SNCT SKQQ YUM JVHIMHAC GVUR FUQQCJC?"
    testit(decrypt(f, n) == "WHEN WILL YOU GRADUATE FROM COLLEGE?")

    g = 82
    o = "J FS TX EYWIBU SXREMB, JT REMBM FWU GXXD CMGRXOMB?"
    testit(decrypt(g, o) == "I AM SO HUNGRY MOTHER, IS THERE ANY FOOD LEFTOVER?")

    x = 69
    y = "BSFI LE VKTR YFXC QTQC?"
    testit(decrypt(x, y) == "WHAT IS YOUR NAME DUDE?")


    print("\nThis is testing Dictionary Class")
    tt = "Hello, I am  cool."
    k = Dictionary(3, tt)
    testit(k.dict2 == {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K',
                       12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U',
                       22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'})
    testit(k.dict1 == {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
                       'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
                       'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26})
    testit(k.key_functions()[0] == {21: 'A', 1: 'B', 2: 'C', 12: 'D', 17: 'E', 3: 'F', 13: 'G', 7: 'H', 4: 'I',
                                    6: 'J', 5: 'K', 8: 'L', 9: 'M', 10: 'N', 14: 'O', 22: 'P', 11: 'Q', 15: 'R',
                                    19: 'S', 16: 'T', 18: 'U', 20: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'})
    testit(k.key_functions()[1] == {'A': 21, 'B': 1, 'C': 2, 'D': 12, 'E': 17, 'F': 3, 'G': 13, 'H': 7, 'I': 4,
                                    'J': 6, 'K': 5, 'L': 8, 'M': 9, 'N': 10, 'O': 14, 'P': 22, 'Q': 11, 'R': 15,
                                    'S': 19, 'T': 16, 'U': 18, 'V': 20, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26})


    tt1 = "Will you  get mad if I yell at you?"
    kk = Dictionary(3, tt1)
    testit(kk.dict1 == {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
                        'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
                        'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26})
    testit(kk.dict2 == {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K',
                        12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U',
                        22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'})
    testit(kk.key_functions()[0] == {11: 'A', 1: 'B', 2: 'C', 12: 'D', 17: 'E', 3: 'F', 23: 'G', 7: 'H', 20: 'I',
                                     8: 'J', 21: 'K', 19: 'L', 4: 'M', 24: 'N', 5: 'O', 6: 'P', 9: 'Q', 13: 'R',
                                     10: 'S', 16: 'T', 18: 'U', 22: 'V', 14: 'W', 15: 'X', 25: 'Y', 26: 'Z'})
    testit(kk.key_functions()[1] == {'A': 11, 'B': 1, 'C': 2, 'D': 12, 'E': 17, 'F': 3, 'G': 23, 'H': 7, 'I': 20,
                                     'J': 8, 'K': 21, 'L': 19, 'M': 4, 'N': 24, 'O': 5, 'P': 6, 'Q': 9, 'R': 13,
                                     'S': 10, 'T': 16, 'U': 18, 'V': 22, 'W': 14, 'X': 15, 'Y': 25, 'Z': 26})

Hancsecurity_test_suit()

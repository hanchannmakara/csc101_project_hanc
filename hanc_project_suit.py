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


Hancsecurity_test_suit()

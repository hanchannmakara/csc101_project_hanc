from dictionary import*

global alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt(a, h):
    k = Dictionary(a, h)
    cipher = ""
    for i in h:
        if i.upper() in alphabet:
            v = k.dict1[i.upper()]
            u = k.key_functions()[0][v]
            cipher += u
        else:
            cipher += i
    return cipher
def main():
    i = ""
    while i!= "quit":
        user_input = "This is crazy. i have been working with this for whole time and nothing works." #Key 3
        result = "OQIM IM CJAZX. I QATG BGGR YPJSIRH YIOQ OQIM LPJ YQPDG OING ARF RPOQIRH YPJSM."
        h = input("Please enter you message: ")
        a = int(input("Please enter your translation key: "))
        test1 = encrypt(a, h)
        print(test1)
        i = input("Type quit to stop the program. ")
        if i == "quit":
            break

if __name__ == "__main__":
    main()

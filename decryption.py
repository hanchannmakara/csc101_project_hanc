from dictionary import*

global alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def decrypt(a, h):
    t = Dictionary(a, h)
    decipher = ""
    conv_list = []
    for i in h:
        if i in alphabet:
            m = t.key_functions()[1][i]
            conv_list.append(m)
        else:
            conv_list.append(i)
    for i in range(len(conv_list)):
        if type(conv_list[i]) is int:
            decipher += t.dict2[conv_list[i]]
        else:
            decipher += str(conv_list[i])
    return decipher

def main():
    result = "This is crazy. i have been working with this for whole time and nothing works." #Key 3
    user_input = "OQIM IM CJAZX. I QATG BGGR YPJSIRH YIOQ OQIM LPJ YQPDG OING ARF RPOQIRH YPJSM."
    h = input("Please enter you message: ")
    a = int(input("Please enter your translation key: "))
    test2 = decrypt(a, h)
    print(test2)

if __name__ == "__main__":
    main()

import math
import sys

class Dictionary():

    def __init__(self, key = 0, input_file = "Please input your mesaage"):
        """

        :param key: user input key
        :param file_input: msg to translate
        """
        self.tk = key
        self.input_file = input_file
        self.dict1 = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
                    "I": 9, "J": 10, "K": 11, "L": 12, "M":13, "N":14, "O": 15, "P": 16,
                    "Q": 17, "R": 18, "S": 19, "T":20, "U": 21, "V": 22, "W":23, "X":24,
                    "Y": 25, "Z": 26}
        self.dict2 = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J",
                    11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S",
                    20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z"}
        self.key_functions()


    def key_functions(self):
        wrd_count = len(self.input_file)
        a = self.tk
        x_value = list(self.dict1.values())

        func_key_list = [0]

        f1 = int((x_value[0]*a + wrd_count) % 27)
        l1 = 0
        while f1 in func_key_list:
            f1 = (f1 + 1) % 27
            l1 += 1
        else:
            func_key_list.append(f1)

        f2 = int(math.pow((a/math.e), (x_value[1]))%27)
        l2 = 0
        while f2 in func_key_list:
            f2 = (f2 + 1) % 27
            l2 += 1
        else:
            func_key_list.append(f2)

        f3 = int(a*math.log10(x_value[2])%27)
        l3 = 0
        while f3 in func_key_list:
            f3 = (f3 + 1) % 27
            l3 += 1
        else:
            func_key_list.append(f3)

        f4 = int((x_value[3]*a)%27)
        l4 = 0
        while f4 in func_key_list:
            f4 = (f4 + 1) % 27
            l4 += 1
        else:
            func_key_list.append(f4)

        f5 = int(math.pow(x_value[4],a)%27)
        l5 = 0
        while f5 in func_key_list:
            f5 = (f5 + 1) % 27
            l5 += 1
        else:
            func_key_list.append(f5)

        f6 = int(math.pow(a,x_value[6])%27)
        l6 = 0
        while f6 in func_key_list:
            f6 = (f6 + 1) % 27
            l6 += 1
        else:
            func_key_list.append(f6)

        f7 = int((a + wrd_count)*(x_value[6])%27)
        l7 = 0
        while f7 in func_key_list:
            f7 = (f7 + 1) % 27
            l7 +=1
        else:
            func_key_list.append(f7)

        f8 = int(math.pow(math.pow(x_value[7],3),(1/a))%27)
        l8 = 0
        while f8 in func_key_list:
            f8 = (f8 + 1) % 27
            l8 += 1
        else:
            func_key_list.append(f8)

        f9 = int((wrd_count+(x_value[8]+a))%27)
        l9 = 0
        while f9 in func_key_list:
            f9 = (f9 + 1) % 27
            l9 += 1
        else:
            func_key_list.append(f9)

        f10 = int((wrd_count*x_value[9]/a)%27)
        l10 = 0
        while f10 in func_key_list:
            f10 = (f10 + 1) % 27
            l10 += 1
        else:
            func_key_list.append(f10)

        f11 = int((wrd_count*a*x_value[10])%27)
        l11 = 0
        while f11 in func_key_list:
            f11 = (f11 + 1) % 27
            l11 += 1
        else:
            func_key_list.append(f11)

        f12 = int(math.pow((wrd_count+ a), x_value[11])%27)
        l12 = 0
        while f12 in func_key_list:
            f12 = (f12 + 1) % 27
            l12 += 1
        else:
            func_key_list.append(f12)

        f13 = int(math.pow(wrd_count,(a/x_value[12]))%27)
        l13 = 0
        while f13 in func_key_list:
            f13 = (f13 + 1) % 27
            l13 += 1
        else:
            func_key_list.append(f13)

        f14 = int(math.pow((a*wrd_count),x_value[13])%27)
        l14 = 0
        while f14 in func_key_list:
            f14 = (f14 + 1) % 27
            l14 += 1
        else:
            func_key_list.append(f14)

        f15 = int((wrd_count- (x_value[14]/a))%27)
        l15 = 0
        while f15 in func_key_list:
            f15 = (f15 + 1) % 27
            l15 += 1
        else:
            func_key_list.append(f15)

        f16 = int((wrd_count/a + x_value[15])%27)
        l16 = 0
        while f16 in func_key_list:
            f16 = (f16 + 1) % 27
            l16 += 1
        else:
            func_key_list.append(f16)

        f17 = int(math.pow(math.pow(wrd_count,x_value[16]), (1/a))%27)
        l17 = 0
        while f17 in func_key_list:
            f17 = (f17 + 1) % 27
            l17 += 1
        else:
            func_key_list.append(f17)

        f18 = int(math.sqrt(wrd_count) + math.sqrt(a) + math.sqrt(x_value[17])%27)
        l18 = 0
        while f18 in func_key_list:
            f18 = (f18 + 1) % 27
            l18 += 1
        else:
            func_key_list.append(f18)

        f19 = int((math.pow(wrd_count,2) + math.pow(a,2) + math.pow(x_value[18],2))%27)
        l19 = 0
        while f19 in func_key_list:
            f19 = (f19 + 1) % 27
            l19 += 1
        else:
            func_key_list.append(f19)

        f20 = int(math.pow(wrd_count+a+x_value[19],2)%27)
        l20 = 0
        while f20 in func_key_list:
            f20 = (f20 + 1) % 27
            l20 += 1
        else:
            func_key_list.append(f20)

        f21 = int((wrd_count*a*x_value[20])%27)
        l21 = 0
        while f21 in func_key_list:
            f21 = (f21 + 1) % 27
            l21 += 1
        else:
            func_key_list.append(f21)

        f22 = int((math.pow(wrd_count, 1/a)*x_value[21])%27)
        l22 = 0
        while f22 in func_key_list:
            f22 = (f22 + 1) % 27
            l22 += 1
        else:
            func_key_list.append(f22)

        f23 = int((math.pow(x_value[22],1/a)/wrd_count)%27)
        l23 = 0
        while f23 in func_key_list:
            f23 = (f23 + 1) % 27
            l23 += 1
        else:
            func_key_list.append(f23)

        f24 = int(math.pow(wrd_count/a,x_value[23])%27)
        l24 = 0
        while f24 in func_key_list:
            f24 = (f24 + 1)%27
            l24 += 1
        else:
            func_key_list.append(f24)

        f25 = int(((math.e *a)/x_value[24])%27)
        l25 = 0
        while f25 in func_key_list:
            f25 = (f25 + 1)%27
            l25 += 1
        else:
            func_key_list.append(f25)

        f26 = int(math.sqrt(wrd_count+a+x_value[25])%27)
        l26 = 0
        while f26 in func_key_list:
            f26 = (f26 + 1)%27
            l26 += 1
        else:
            func_key_list.append(f26)

        dict3 = {f1:"A", f2:"B", f3:"C", f4:"D", f5:"E", f6:"F", f7:"G", f8:"H",
                  f9:"I", f10:"J", f11:"K", f12:"L", f13:"M", f14:"N", f15:"O", f16:"P",
                  f17:"Q", f18:"R", f19:"S", f20:"T", f21:"U", f22:"V", f23:"W", f24:"X",
                  f25:"Y", f26:"Z"}

        dict4 = {"A": f1, "B": f2, "C": f3, "D": f4, "E": f5, "F": f6, "G": f7, "H": f8,
                  "I": f9, "J": f10, "K": f11, "L": f12, "M":f13, "N":f14, "O": f15, "P": f16,
                  "Q": f17, "R": f18, "S": f19, "T":f20, "U": f21, "V": f22, "W":f23, "X":f24,
                  "Y": f25, "Z": f26}
        key_plus_loop = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15,
                         l16, l17, l18, l19, l20, l21, l22, l23, l24, l25, l26]
        return dict3, dict4, key_plus_loop

def main():
    h = "This is crazy. i have been working with this for whole time and nothing works."
    k = Dictionary(4, h)
    t = Dictionary(3, h)
    print(t.key_functions()[0])
    print(t.key_functions()[1])
    print(t.dict1)
    print(t.dict2)

    print("\n")
    print(k.key_functions()[0])
    print(k.key_functions()[1])
    print(k.dict1)
    print(k.dict2)

if __name__ == "__main__":
    main()


from dictionary import*

class HancSecurity:
    #This part will be for encryption and decryption purpose
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self, input_file = "Input File", key = 0, crypt_type = "encrypt"):
        self.input_file = input_file
        self.key= key
        self.crypt_type = crypt_type
        self.cipher = ""
        self.message = ""
        self.import_file()

        self.t1 = Dictionary(self.key, self.input_file).dict1
        self.t2 = Dictionary(self.key, self.input_file).dict2
        self.t3 = Dictionary(self.key, self.input_file).key_functions()[0]
        self.t4 = Dictionary(self.key, self.input_file).key_functions()[1]

    def import_file(self):
        f = open(self.input_file, "r")
        if self.crypt_type == "encrypt":
            self.message = f.read()
        elif self.crypt_type == "decrypt":
            self.cipher = f.read()
        f.close()

    def export_file(self, text_to_export, filename):
        f = open(filename, "w")
        f.write(text_to_export)
        f.close()
        print("File exported to " + filename)

    def encrypt(self):
        output = ""
        for i in self.message:
            if i.upper() in self.alphabet:
                v = self.t1[i.upper()]
                u = self.t3[v]
                output += u
            else:
                output += i
        return output

    def decrypt(self):
        output = ""
        convert_list = []
        for i in self.cipher():
            if i in self.alphabet:
                m = self.t4[i]
                convert_list.append(m)
            else:
                convert_list.append(i)
        for i in range(len(convert_list)):
            if type(convert_list[i]) is int:
                output += self.t2[i]
            else:
                output += str(convert_list[i])
        return output

def main():
    #A sample encryption
    cipher0 = HancSecurity("message_input.txt", 3, "encrypt")
    cipher_text0 = cipher0.encrypt()
    cipher0.export_file(cipher_text0, "hanc_smp1.txt")

    cipher3 = HancSecurity("hanc_smp1.txt", 3, "decrypt")
    cipher_text3 = cipher3.decrypt()
    cipher3.export_file(cipher_text3, "hanc_samp1_decrypt.txt")




if __name__ == "__main__":
    main()


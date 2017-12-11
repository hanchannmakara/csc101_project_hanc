from dictionary import*

class HancSecurity:
    #This part will be for encryption and decryption purpose
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, input_file = "Input File", key = 0, crypt_type = "encrypt"):
        self.input_file = input_file
        self.key = key
        self.crypt_type = crypt_type
        self.cipher = ""
        self.message = ""
        #self.import_file()

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
        k = Dictionary(self.key, self.input_file)
        for i in self.message:
            if i.upper() in self.alphabet:
                v = k.dict1[i.upper()]
                u = k.key_functions()[0][v]
                output += u
            else:
                output += i
        print(output)
        return output

    def decrypt(self):
        decrypt_list = []
        k = Dictionary(self.key, self.input_file)
        for i in self.cipher:
            if i in self.alphabet:
                m = k.key_functions()[1][i]
                decrypt_list.append(m)
            else:
                decrypt_list.append(i)
        output = ""
        for i in range(len(decrypt_list)):
            if type(decrypt_list[i]) is int:
                output += k.dict2[decrypt_list[i]]
            else:
                output += str(decrypt_list[i])
        print(output)
        return output


def main():
    #A sample encryption
    cipher0 = HancSecurity("message_input.txt", 5, "encrypt")
    cipher_text0 = cipher0.encrypt()
    cipher0.export_file(cipher_text0, "hanc_smp1.txt")

    #cipher3 = HancSecurity(, 5, "decrypt")
    #cipher_text3 = cipher3.decrypt()
    #cipher3.export_file(cipher_text3, "hanc_samp1_decrypt.txt")



if __name__ == "__main__":
    main()


from dictionary import*
from encryption import*
from decryption import*

class HancSecurity:

    def __init__(self, key = 0, user_input = "User Message", crypt_type = "encrypt"):
        self.user_input = user_input
        self.key = key
        self.crypt_type = crypt_type
        self.message = ""
        self.cipher = ""
    def crypting(self):
        try0 = HancSecurity(self.key, self.user_input, self.crypt_type)
        if try0.crypt_type == "encrypt":
            output = encrypt(self.key, self.user_input)
        else:
            output = decrypt(self.key, self.user_input)
        return output

def main():
    key1  = int(input("Please enter your  key: "))
    use_mgs1 = input("Please enter your text: ")
    crypt1 = input("Please enter your encryption_type [encrypt/decrypt]: ")
    try0 = HancSecurity(key1, use_mgs1, crypt1)
    try1 = try0.crypting()
    print(try1)
if __name__== "__main__":
    main()

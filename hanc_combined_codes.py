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

def main():
    key1  = int(input("Please enter your  key: "))
    use_mgs1 = input("Please enter your text: ")
    crypt1 = input("Please enter your encryption_type [encrypt/decrypt]: ")
    try0 = HancSecurity(key1, use_mgs1, crypt1)
    try1 = try0.enct()
    print("Hi")
if __name__== " __main__":
    main()

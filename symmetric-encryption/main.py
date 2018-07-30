import sys

from cryptography.fernet import Fernet


def main(text):
   key = Fernet.generate_key()
   f = Fernet(key)
   token = f.encrypt(text)
   print("decrypted text: %s, key: %s" % (token, key))
   return token, key


if __name__ == '__main__':
    main(sys.argv[1])

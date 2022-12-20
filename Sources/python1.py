import sys
import argparse

class IDObfuscator:
    def __init__(self, key, length):
        self.key = key
        self.length = length
    
    def __init__(self, key):
        self.key = key
        self.length = 8
        
    def __init__(self):
        self.key = bytearray(b'9tphM8YYhE0fvmeN3KPNPFJ4cHftG4lMFHP9GAmj')
        self.length = 8
    
    def compressKey(self):
        key = bytearray(self.key)
        while len(key) > self.length:
            newKey = bytearray()
            for i in range(0, len(key) - 1, 2):
                newKey.append(key[i] ^ key[i + 1])
            key = newKey
        self.key = key
    
    def encrypt(self, id):
        id = int(id)
        key = self.key
        self.compressKey()
        key = self.key
        self.key = key
        encrypted = bytearray()
        for i in range(0, self.length):
            encrypted.append(id & 0xFF)
            id >>= 8
        for i in range(0, self.length):
            encrypted[i] ^= key[i]
        return int.from_bytes(encrypted, byteorder='little')
    
    def decrypt(self, id):
        id = int(id)
        key = self.key
        self.compressKey()
        key = self.key
        self.key = key
        decrypted = bytearray()
        for i in range(0, self.length):
            decrypted.append(id & 0xFF)
            id >>= 8
        for i in range(0, self.length):
            decrypted[i] ^= key[i]
        return int.from_bytes(decrypted, byteorder='little')
    
    def setKey(self, key):
        self.key = key
    
    def setLength(self, length):
        self.length = length
        
    def getKey(self):
        return self.key
    
    def getLength(self):
        return self.length
    
    def printInfo(self):
        print("Key: " + str(self.key))
        print("Length: " + str(self.length))
    
    def printUsage(self):
        print("Usage: " + sys.argv[0] + " [-h] [-e] [-d] [-k KEY] [-l LENGTH] ID")
        print("Encrypt or decrypt an ID using a key and length")
        print("  -h, --help            show this help message and exit")
        print("  -e, --encrypt         encrypt ID")
        print("  -d, --decrypt         decrypt ID")
        print("  -k KEY, --key KEY     set key")
        print("  -l LENGTH, --length LENGTH")
        print("                        set length")
        print("Example: " + sys.argv[0] + " -d -k 9tphM8" + " 1060271552")
        
    def printError(self):
        print("Error: " + sys.argv[0] + " [-h] [-e] [-d] [-k KEY] [-l LENGTH] ID")
        print("Try '" + sys.argv[0] + " -h' for more information.")
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encrypt", help="encrypt ID", action="store_true")
    parser.add_argument("-d", "--decrypt", help="decrypt ID", action="store_true")
    parser.add_argument("-k", "--key", help="set key")
    parser.add_argument("-l", "--length", help="set length", type=int)
    parser.add_argument("ID", help="ID to encrypt/decrypt")
    args = parser.parse_args()
    obfuscator = IDObfuscator()
    if args.key:
        obfuscator.setKey(args.key)
    if args.length:
        obfuscator.setLength(args.length)
    if args.encrypt:
        print(obfuscator.encrypt(args.ID))
    elif args.decrypt:
        print(obfuscator.decrypt(args.ID))
    else:
        obfuscator.printError()
        sys.exit(1)
    sys.exit(0)
    
if __name__ == "__main__":
    main()
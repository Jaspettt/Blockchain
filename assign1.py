import random


class Block:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class ChainOfBlocks:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_block = Block(data)
        if self.head is None:
            self.head = new_block
            return
 
        current_block = self.head
        while(current_block.next):
            current_block = current_block.next
 
        current_block.next = new_block

    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_block = self.head
            while(current_block):
                size = size+1
                current_block = current_block.next
            return size
        else:
            return 0
 
    def printLL(self):
        current_block = self.head
        while(current_block):
            print(current_block.data)
            current_block = current_block.next



def generate_keypair():
    p = generate_large_prime()
    q = generate_large_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = choose_public_exponent(phi)
    d = modular_inverse(e, phi)
    return ((n, e), (n, d))

def generate_large_prime(bits=1024):
    prime_candidate = random.getrandbits(bits)
    while not is_prime(prime_candidate):
        prime_candidate += 1
    return prime_candidate

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def choose_public_exponent(phi):
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    return e

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(message, public_key):
    n, e = public_key
    return pow(message, e, n)

def decrypt(ciphertext, private_key):
    n, d = private_key
    return pow(ciphertext, d, n)


def transactionOperation(chain):
    while (True):
        insertionReceiver = input("Who you want to transact money?: ")
        insertionAmount = int(input("How much you would like to send?: "))
        public_key, private_key = generate_keypair()
        cipheredData = encrypt(insertionAmount, public_key)
        insertionData = str(insertionReceiver) + " get " + str(cipheredData) + " AliCoins"
        signature = input("To complete transaction, we need your sign(private key word): ")
        print()
        if (decrypt(sign, turntonum(word)) == 212):
            chain.insert(insertionData)
            print("Transaction complete!")
        else:
            print("Wrong signature!")
        
        yesno = input("Transactions complete? (y/n): ")
        if (yesno == 'y'):
            break

def turntoword(privatekey):
    privkey1 = str(privatekey[0])
    privkey2 = str(privatekey[1])
    word1 = ""
    word2 = ""
    for i in privkey1:
        word1 += chr((int(i) + 10) * 5)
    for i in privkey2:
        word2 += chr((int(i) + 10) * 5)
    return word1 + " " + word2

def turntonum(word):
    privkey1 = word.split(' ')[0]
    privkey2 = word.split(' ')[1]
    num1 = ""
    num2 = ""
    for i in privkey1:
        num1 += str((int(ord(i) / 5) - 10))
    for i in privkey2:
        num2 += str((int(ord(i) / 5) - 10))
    return (int(num1), int(num2))

transactions = ChainOfBlocks()
xpub, ypriv = generate_keypair()
sign = encrypt(212, xpub)
word = turntoword(ypriv)

print("Your signature: " + word)

print("Welcome!")

while (True):
    commandMenu = int(input("What would you like?: \n 1. Transfer money \n 2. View transaction list \n 3. Close the app \n"))
    if (commandMenu == 1):
        transactionOperation(transactions)
    if (commandMenu == 2):
        transactions.printLL()
    if (commandMenu == 3):
        exit(1)

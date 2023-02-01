''' O algoritmo RSA é um algoritmo de criptografia de chave pública que é amplamente utilizado para criptografar e assinar dados. Ele funciona gerando dois números primos aleatórios, chamados de p e q, e calculando n = p * q. O algoritmo RSA em python pode ser implementado da seguinte maneira:

Copy code '''
import random 

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_e(phi):
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    return e

def find_d(e, phi):
    i = 1
    while True:
        if((i * e) % phi == 1):
            return i
        i += 1
    
def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = find_e(phi)
    d = find_d(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with private key ", private, " . . .")
    print("Your message is:")
    print(decrypt(private, encrypted_msg))
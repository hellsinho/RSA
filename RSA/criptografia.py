import random

# E, N == chave pública
# D, N == chaves privadas

class Criptografia():
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.phi_n = (p-1) * (q-1)
        self.n = self.p * self.q
        self.e = 0
        self.d = 0
        
    # gera as chaves públicas e privadas
    def getKeys(self):
        self.e = self.encontrar_e(self.phi_n)
        self.d = self.encontrar_d(self.e, self.phi_n)
        return ((self.e, self.n),(self.d, self.n)) # Retorna a chave pública e privada
    
      # Máximo divisor comum
    def mdc(self, a, b):
        while(b != 0):
            resto = a % b
            a = b
            b = resto
        return a
            
        # Encontrar um valor primo no intervalo de 1 < E < phi
    def encontrar_e(self, phi):
        self.e = random.randrange(1 , phi)
        maximo = self.mdc(self.e, phi)

        while(maximo != 1):
            e = random.randrange(1 , phi)
            maximo = self.mdc(e, phi)
        return e

        # Chave privada valor D
    def encontrar_d(self, e, phi):
        for i in range(1, phi):
            if((i * e) % phi == 1):
                return i
        return None
    
 
    def criptografar(self, chave_publica, n, texto):
        mensagem_cifrada = []
        for i in texto:
            letra_cifrada = ((ord(i) ** chave_publica) % n)
            mensagem_cifrada.append(letra_cifrada)
        return mensagem_cifrada

    def descriptografar(self, chave_privada, n, texto_cifrado):
        mensagem = []
        for i in texto_cifrado:
            letra = (i ** chave_privada) % n
            texto = chr(letra)
            mensagem.append((texto))
        return ''.join(mensagem)

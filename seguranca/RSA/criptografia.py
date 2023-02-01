import random

# E, N == chave pública
# D, N == chaves privadas

   
 # gera as chaves públicas e privadas
def gerar_chaves(p, q):
    n = p * q
    phi_n = (p-1) * (q-1)
    e = encontrar_e(phi_n)
    d = encontrar_d(e, phi_n)

    return ((e, n),(d, n)) # Retorna a chave pública e privada

# Máximo divisor comum
def mdc( a, b):
    while(b != 0):
        resto = a % b
        a = b
        b = resto
    return a
        
    # Encontrar um valor primo no intervalo de 1 < E < phi
def encontrar_e( phi):
    e = random.randrange(1 , phi)
    maximo = mdc(e, phi)

    while(maximo != 1):
        e = random.randrange(1 , phi)
        maximo = mdc(e, phi)
    return e

    # Chave privada valor D
def encontrar_d( e, phi):
    for i in range(1, phi):
        if((i * e) % phi == 1):
            return i
    return None

def criptografar(chave_publica, n, texto):
    mensagem_cifrada = []
    for i in texto:
        letra_cifrada = ((ord(i) ** chave_publica) % n)
        mensagem_cifrada.append(letra_cifrada)
    return mensagem_cifrada

def descriptografar(chave_privada, n, texto_cifrado):
    mensagem = []
    for i in texto_cifrado:
        letra = (chave_privada ** i) % n
        texto = chr(letra)
        mensagem.append((texto))
    return ''.join(mensagem)



((e, n),(d, n)) = gerar_chaves(3, 17)


print(n)
print(e)
print(d)
mensagem = str(input("Digite sua mesagem: "))

mensagem_cifrada = criptografar( e, n, mensagem)
print(mensagem_cifrada)

mensagem_decifrada = descriptografar( d, n, mensagem_cifrada)
print(mensagem_decifrada)
from RSA.criptografia  import Criptografia

cripto = Criptografia(13, 41)

((e, n),(d, n)) = cripto.getKeys()

print(n)
print(e)
print(d)
mensagem = str(input("Digite sua mesagem: "))

mensagem_cifrada = cripto.criptografar(e, n, mensagem)
print(mensagem_cifrada)

mensagem_decifrada = cripto.descriptografar( d, n, mensagem_cifrada)
print(mensagem_decifrada)
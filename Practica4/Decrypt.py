from cryptography.fernet import Fernet

def cargar_key():
    return open("clave.key.txt","rb").read()

key = cargar_key()

cipher_suite = Fernet(key)

#En "mensaje.txt" se pone el nombre del archivo donde se encuentra el mensaje encriptado
def cargar_mensaje():
    return open ("nombre_encrypt.txt","rb").read()

cipher_text = cargar_mensaje()

plain_text = cipher_suite.decrypt(cipher_text)

print(plain_text.decode())

import pyAesCrypt

password = input('Enter a password to encrypt the file: ')

# encrypt
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

# decrypt
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)

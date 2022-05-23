encrypt = input('cripta il testo: \n')

encrypt_text = ''

for c in encrypt:
    x = ord(c)
    x = x + 1
    c2 = chr(x)

    encrypt_text = encrypt_text + c2

print(encrypt_text)
print('\n')
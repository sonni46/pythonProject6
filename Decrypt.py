dencrypt = input('Decripta il testo: \n')

plain_text = ''

for c in dencrypt:
    x = ord(c)
    x =- 1
    c2 = chr(x)

    plain_text = plain_text + c2

print(plain_text)
print('\n')
try:
    import pyperclip
except ImportError:
    pass
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print('Caesar Cipher, by A. Sweigart')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number.')
print()

while True:
    print('Do you want to (e)ncrypt of (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d')


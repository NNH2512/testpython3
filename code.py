import pyperclip
message='this is my secret message'
key=13
mode='encrypt'
LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
transladed=''
message=message.upper()
for symbol in message:
    if symbol in LETTERS:
        num=LETTERS.find(symbol)
        if mode=='encrypt':
            num=num+key
        elif mode=='decrypt':
            num=num-key
        if num>=len(LETTERS):
            num=num-len(LETTERS)
        elif num<0:
            num=num+len(LETTERS)
        transladed=transladed+LETTERS[num]
    else:
        transladed=transladed+symbol
print(transladed)
pyperclip.copy(transladed)



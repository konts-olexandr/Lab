b = ''
v = b
ua = "абвгґдуєжзиіїйклмнопрстуфхцчшщьюяабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
UA = ua.upper()
ENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng = ENG.lower()
num = "12345678901234567890"


text=''
Dtext=""
key = 5

textt = ''
Dtextt=""
o_eng = ord("a")
o_ENG = ord("A")

for letter in text:

    new_num = num.find(letter) + key
    new_ua = ua.find(letter) + key
    new_UA = UA.find(letter) + key

    if letter in ua:
        textt = textt + ua[new_ua]

    elif letter in UA:
        textt = textt + UA[new_UA]

    elif letter in str(eng):
        textt += chr(((ord(letter) - o_eng + key) % 32) + o_eng)

    elif letter in str(ENG):
        textt += chr(((ord(letter) - o_ENG + key) % 32) + o_ENG)

    elif letter in str(num):
        textt = textt + num[new_num]

    else:
        textt = textt + letter


for letter in b:

        Dnew_num = num.find(letter) - key
        Dnew_ua = ua.find(letter) - key
        Dnew_UA = UA.find(letter) - key

        if letter in ua:
         Dtextt = Dtextt + ua[new_ua]

        elif letter in UA:
         Dtextt = Dtextt + UA[new_UA]

        elif letter in str(eng):
         Dtextt += chr(((ord(letter) - o_eng - key) % 32) + o_eng)

        elif letter in str(ENG):
         Dtextt += chr(((ord(letter) - o_ENG - key) % 32) + o_ENG)

        elif letter in str(num):
         Dtextt = Dtextt + num[new_num]

        else:
         Dtextt = Dtextt + letter


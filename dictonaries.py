import time

qiymat = int(input('''quyidagilardan birini tanlang:
1.Dictonaries
2.Time
3.Threading
'''))
lugat = {
    "Odam":{
        "ism": "Samir",
        "familiya": "Amirov",
        "otchestva": "Sanjar o'g'li",
        "yosh": 18
    },
    "Gul": {
        'nomi': 'Atirgul',
        'rangi': 'qizil'
    },       
}
qiymat1 = 0
if qiymat == 1:
    
    print("4 sekund kuting")

    while qiymat1 < 4:
        qiymat1 += 1
        time.sleep(0.2)
        print(qiymat1)
    print("Odam:")
    print(lugat["Odam"])
    print("Gul")
    print(lugat["Gul"])


elif qiymat == 2:
    print("4 sekund kuting")
    while qiymat1 < 4:
        qiymat1 += 1
        time.sleep(0.2)
        print(qiymat1)

    from dict import * 

elif qiymat ==3:
    print("4 sekun kuting")
    while qiymat1 < 4:
        qiymat1 += 1
        time.sleep(0.2)
        print(qiymat1)

    from threading1 import *
import time


ism = input("ismingizni kiriting: ")
familiya = input("familiyangizni kiriting: ")
parol = int(input("parol kiriting: "))
login = input("login kiriting: ")
a_b = 0


if parol == 1234 and login == "login1234":
    print("siz parol va loginni to'g'ri kiritdingiz")
elif parol != 1234 and login == "login1234":
    print("parol xato")

    print("4 sekund kuting!")

    while a_b < 4:
        a_b += 1
        time.sleep(0.2)
        print(a_b)
elif parol == 1234 and login != "login1234":
    print("login xato")

    print("4 sekund kuting!")


    while a_b < 4:
        a_b += 1
        time.sleep(0.4)
        print(a_b)
elif parol != 1234 and login != "login1234":
    print("siz parol va loginni xato kiritdingiz")

    print("6 sekund kuting!")

    while a_b < 6:
        a_b += 1
        time.sleep(0.2)
        print(a_b)
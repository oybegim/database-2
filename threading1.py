import threading
import time

def funksiya1():
    for x in range(0, 4):
        time.sleep(0.2)
        print("Oybegim")


def funksiya2():
    for x in range(0, 4):
        time.sleep(0.2)
        print("Sultonova")



def funksiya3():
    for x in range(0, 4):
        time.sleep(0.2)
        print("Safar qizi")

        
f1 = threading.Thread(target=funksiya1)
f2 = threading.Thread(target=funksiya2)
f3 = threading.Thread(target=funksiya3)


f1.start()
f2.start()
f3.start()
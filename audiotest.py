from threading import Thread


def print1():

    for x in range(1000):
        f = 3
    return "dASDASDASDASDASDASone"

def print2():

    while True:
        print ("ongoing")


test = Thread(target = print1).start()
#while test != "done":
#    Thread(target = print2).start()

print(test)

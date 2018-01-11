
import random

i = 0

temp_file = "/Users/autohome/test.txt"


def writeLmk(fileName, landmarks):

    fp = open(fileName, 'w+')
    for j in landmarks:
        fp.write(str(j))
        fp.write("\n")

    fp.close()

def for_shu(b):
    a = random.random()
    b = a * 100000000000
    if len(str(b)) < 11:
        a = random.random()
        b = a * 100000000000
    return int(b)
def main_read():
    b = 0
    c =[]
    while True:
        ten = input("请输入正整数x:")
        try:
            x = eval(ten)
            if x > 0:
                for i in range(x):
                    c.append(for_shu(b))
                    print(c)

        except:
            pass
        writeLmk(temp_file, c)
        break



main_read()


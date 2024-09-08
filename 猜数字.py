from random import randint

try:
    with open('leve.txt') as fj:
        leve = fj.readline()
        leve = int(leve)

except ValueError:
    with open('leve.txt', 'w') as fk:
        fk.write('1')
except FileNotFoundError:
    with open('leve.txt', 'w') as fk:
        fk.write('1')

sm = leve*20
cs = randint(0, sm)
print('关卡越高猜的数越大')
print('当前数值：' + '0' + '-' + str(sm))
print("猜数字无限版")
print('关卡：' + str(leve))
s = -1
while True:
    try:
        while True:
            s += 1
            print('当前试错次数：' + str(s))
            user = int(input('输入数字: '))

            if user > cs:
                print('你的数大了')

            elif user < cs:
                print('你数小了！')

            elif user == cs:
                print('当前试错次数：' + str(s))
                print('你猜对了')
                print('现在重置随机数')

                sm += leve*20

                cs = int(randint(0, sm))
                with open('leve.txt', 'w') as fj:
                    leve += 1
                    leve = str(leve)
                    fj.write(leve)
                    leve = int(leve)
                print('重置成功关卡：' + str(leve) + ' 难度加' + str(20))
                print('当前数值：' + '0' + '-' + str(sm))
                print('试错次数以重置！')
                s = -1
    except ValueError:
        print('你输入了错误的字符')

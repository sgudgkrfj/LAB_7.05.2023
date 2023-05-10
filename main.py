#1
def beebra(*args):
    ser=0
    for i in args:
        ser+=1
    print(sum(args)/ser)
beebra(1,2,3,4,5)


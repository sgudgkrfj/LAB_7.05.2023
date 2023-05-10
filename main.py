#1
def beebra(*args):
    ser=0
    for i in args:
        ser+=1
    print(sum(args)/ser)
beebra(1,2,3,4,5)

#2
def ratatatata(*args):
    lengs=[len(arg) for arg in args]
    return max(lengs)
print(ratatatata('egtyjtr','fae','wradwAEQFDW'))
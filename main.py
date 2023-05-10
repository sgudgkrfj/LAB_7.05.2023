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

#3
def ggg(*args):
    return ' '.join(args)
print(ggg("jvnkflkgj","kfjgntk"))

#4
def hhh(*args,**kwargs):
    f1=(["Emanuel",23], ["Max",17],["Gregor",15])
    dict={}
    for key,value in f1:
        dict[key]=value
    print(dict)
hhh()


#5
def combine_dicts(*args):
    result={}
    for dictionary in args:
        result.update(dictionary)
    return result
dict1={"kjldkf":23}
dict2={"fjgfk":2}
print(combine_dicts(dict1,dict2))
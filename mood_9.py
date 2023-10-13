''' Convert the given year into roman equivalent. Roman equivalents are M:1000, D:500, C:100,
L:50, X:10, V:5, I:1.'''


Y = int(input()) #year
yt = list(str(Y))
rom=[]
dig = len(yt)
if dig!=4:
    while True:
        if len(yt)==4:
            break
        else:
            yt.insert(0,0)
#roman func
def order(num,_1u,_5u,_10u):
    if num<5 and num!=0 and num!=4:
        for a in range(0,num):
            rom.append(_1u)
    elif num==4:
        rom.append(_1u)
        rom.append(_5u)
    elif num!=9 and num>=5:
        rom.append(_5u)
        for a in range(0,num-5):
            rom.append(_1u)
    elif num==9:
        rom.append(_1u)
        rom.append(_5u)
    else:
        pass
#thousands
M = int(yt[0])
for a in range(0,M):
    rom.append('m')
#hundreds
C = int(yt[1])
order(C,'c','d','m')
#tens
X = int(yt[2])
order(X,'x','l','c')
#units
I = int(yt[3])
order(I,'i','v','x')
#printing roman number
for i in rom:
    print(i)

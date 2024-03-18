seriesLen = input("Provide the length of Fibonacci series to print (>0): ")
seriesLen = int(seriesLen)
a=0
b=1
c=0
if(seriesLen>0):
    print(a)
if(seriesLen>1):
    print(b)
if(seriesLen>2):
    seriesLen = seriesLen - 2
    while(seriesLen>0):
        print(a+b)
        c=a
        a=b
        b=b+c
        #print('next value of a & b: ', a, '  --- ', b)
        seriesLen = seriesLen - 1
    print('End of Sequence !!')
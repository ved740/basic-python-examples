val = input('Please enter your value: ')
digitCount = len(val)
sum=0
for index in range(0,digitCount,1):
    #print('index: ', index)
    #print(val[index])
    if(type(int(val[index])) is int):
        sum += int(val[index])
else:
    print('Sum of Digits: ', sum)
from datetime import datetime

def find_factorial(iNum):
    if(type(iNum) is str):
        iNum=int(iNum)
    if(iNum == 0):
        return 0
    else:
        result=1
        while(iNum > 0):
            result *= iNum
            iNum -= 1
        return result
    
#print(find_factorial(5))
    
def check_strong_number(num):
    num=str(num)
    num_len = len(num)
    factSum=0
    for index in range(0,num_len):
        #print(num[index])
        factSum += find_factorial(num[index])
    #print(factSum)
    return factSum == int(num)

print(f'Start: {datetime.now()}')
for sample in range(100000000):
    if(check_strong_number(sample)):
        print(f'{sample} is a Strong Number')
print(f'End: {datetime.now()}')
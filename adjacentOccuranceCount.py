adjOcrCount = 0
intList = [1,2,2,3,4,4,4,10]
for index in range(0, len(intList) - 1):
    if(intList[index] == intList[index+1]):
        adjOcrCount += 1
print(f"Count of Adjacent Occurances: {adjOcrCount}")
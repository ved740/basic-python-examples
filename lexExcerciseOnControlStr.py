val = input('Please enter your value: ')
val = int(val)
print(val)
if(val%3==0 and val%5==0):
    print('Zoom')
elif(val%3==0):
    print('Zip')
elif(val%5==0):
    print('Zap')
else:
    print('Invalid')
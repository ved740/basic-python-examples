def check_value(message,num):
    msg=message[:num]
    print(msg)
    return len(msg)

result=check_value('Infosys',4)  
print("Result:", result)
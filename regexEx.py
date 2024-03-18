import re
if(re.search(r"A..l","Aopline")!=None):     #1True
    print("Pattern found:1")  
else:
    print("Pattern not found")  

if(re.search(r"A\dl","A2line")!=None): #2True
    print("Pattern found:2")
else:
    print("Pattern not found")

if(re.search(r"A\d*","A2234line")!=None): #3True
    print("Pattern found:3")
else:
    print("Pattern not found")

if(re.search(r"A\d+","Airline")!=None):
    print("Pattern found:")
else:            #4True
    print("Pattern not found: 4")

if(re.search(r"A\d?i","Airline")!=None): #5True
    print("Pattern found:5")
else: 
    print("Pattern not found:")

if(re.search(r"A\d{3}i","A223irline")!=None):   #6True
    print("Pattern found:6")
else:
    print("Pattern not found")

if(re.search(r"A[4-8]l","A2line")!=None):
    print("Pattern found:")
else: #7True
    print("Pattern not found:7")

if(re.search(r"^A","Airline")!=None):#True
    print("Pattern found:8")
else:
    print("Pattern not found")

if(re.search(r"e$","Airline")!=None):#True
    print("Pattern found:9")
else:
    print("Pattern not found")

if(re.search(r"\w$","Airline%")!=None):
    print("Pattern found:")
else:#True
    print("Pattern not found:10")

if(re.search(r"Air\s","Airline")!=None):
    print("Pattern found:")
else:#True
    print("Pattern not found:11")

if(re.search(r"Hell|Fell","Fellow")!=None):#True
    print("Pattern found:12")
else:
    print("Pattern not found")
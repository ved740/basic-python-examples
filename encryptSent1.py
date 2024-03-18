inputString = input('Enter a sentence: ')
inputString = inputString.split(' ')
result = []
for index in range(0, len(inputString)):
    if(index%2 == 0):
        result.append(inputString[index][::-1])
    else:
        #check not voewls, bring to first
        non_vowels = []
        vowels = []
        for char in inputString[index]:
            if char in 'aeiouAEIOU':
                vowels.append(char)
            else:
                non_vowels.append(char)
        encryptedString = ''.join(non_vowels + vowels)
        result.append(encryptedString)
print(' '.join(result))

#str = input("Enter string with character ,digit and special character :")


str = "Hello World"
lowerAlphabet="abcdefghijklmnopqrstuvwxyz"
alphabet=lowerAlphabet.upper()
for i in range(len(str)-1):
    for j in range(len(alphabet)-1):
        if  str[i] == alphabet[j]:
         str2 = str[i]
         print(str2)





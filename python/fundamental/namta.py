def namta(n):
    result = 0
    for i in range(1,11):
        result = i*n
        print(n,"X",i ,"=",n*i)
n=input("Enter any number: ")
n=int(n)
namta(n)

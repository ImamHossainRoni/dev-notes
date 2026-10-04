from functools import  reduce
nums = [3,2,6,8,4,6,9]
evens = list(filter(lambda n : n%2==0,nums))
sum = reduce(lambda a,b:a+b,evens)
print(sum)
def is_even(n):
    return n%2 ==0

nums = [45,67,23,3,7,8,90,44]
evens = list(filter(is_even,nums))
print(evens)

#Used Lambda instead of using function
odds = list(filter(lambda n:n%2==1,nums))
print(odds) 
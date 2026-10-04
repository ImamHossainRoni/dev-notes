
nums = [3,2,6,8,4,6,9]
evens = list(filter(lambda n : n%2==0,nums))
double = list(map(lambda n:n*2,evens))
print(double)
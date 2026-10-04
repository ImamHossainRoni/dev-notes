my_str = "madam"
my_str = my_str.casefold()
revr_str = reversed(my_str)

if list(my_str) == list(revr_str):
    print(my_str," is plaindrome !")
else:
    print(my_str," is not plaindrome ! ")

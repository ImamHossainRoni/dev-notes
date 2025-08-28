nums = [1, 3, 5, 3, 45, 91, 7]
it_nums = iter(nums)
# print(next(it_nums))

while it_nums:
    try:
        item = next(it_nums)
        print(item)
    except StopIteration:
        break

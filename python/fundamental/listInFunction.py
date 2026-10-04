def addNumbers(numbers):
   result = 0
   for number in numbers:
       result = result + number
   avr=result/3
   return avr

avr=addNumbers([1,2,3])
print(avr)

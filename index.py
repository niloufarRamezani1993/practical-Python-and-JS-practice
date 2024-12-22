import math
import pprint



# check if the number is Odd or Even

num = int(input("Enter a number please" + "\n"))

if num % 2 == 0 :
    print("It is Even")

else:
    print("It is Odd")


# write some items have integer numbers , by For and Foreach caculate the sum of them 
# if sum was bigger than 100 print It is not allow
# if it's equall 100 print It's in range

array = []
i = int(input("how many numbers?"))
for _ in range(i):
   a = int(input("enter a number"))
   array.append(a)
  

b = sum(array)

if b > 100 :
    print("it's not allowed")
elif b < 100 :
    print("It's in range")
else :
    print("it's fix a 100")



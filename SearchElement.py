# searching element in an array

import array as a
my_arr=a.array('i',[4,5,8,9,20,1])
print("Array Elements are: ")
for i in my_arr:
    print(i)

ele=int(input("Enter element that u want to search :"))

for i in range(len(my_arr)) :
    if my_arr[i]==ele:
        print("Element found at :",i+1," position")
    else:
        print("Element not found")

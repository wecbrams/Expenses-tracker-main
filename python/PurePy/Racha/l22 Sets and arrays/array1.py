import array as arr
array_num=arr.array("i",[1,2,3,5,3,7,8,9,3])

print("Original array",array_num)
count_3=array_num.count(3)
print("Number of occurrences of 3:",count_3)

array_num.reverse()
print("Reversed array: ", array_num)
def ONSquareTime(n):  #O(n2)
    iteration = 0
    for i in range(n):         
        for j in range(n):     
            iteration += 1
            print(f"Iteration {iteration}: (i={i}, j={j})")
    print("Total iterations done:", iteration, "\n")

# Try different inputs
ONSquareTime(3)
ONSquareTime(4)
ONSquareTime(5)
'''

3>> 0x0
0x1
0x2
0x3

1
'''
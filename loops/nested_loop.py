# range(n) = 0 to n-1
# range(m, n) = m to n-1
# range(m, n, inc/dec) = m to n-1 with incr/decr


for i in range(3): # initially i = 0 and possible values are : 0, 1, 2. It means this outer loop will be executed 3 times
    for j in range(2): # initially j = 0 and possible values are : 0, 1. It means this inner loop will be executed 2 times
        print("Hello, Inner loop", end="\n")
    print("Hey, Outer loop")


"""
Explanation

i = 0
    j = 0 --> Hello, Inner loop
    j = 1 --> Hello, Inner loop
i = 1
    j = 0 --> Hello, Inner loop
    j = 1 --> Hello, Inner loop
i = 2
    j = 0 --> Hello, Inner loop
    j = 1 --> Hello, Inner loop
"""


for i in range(3):
    for j in range(2):
        print("i = {} and j = {}".format(i, j))
print("\n")

"""
Output: 

i = 0 and j = 0
i = 0 and j = 1
i = 1 and j = 0
i = 1 and j = 1
i = 2 and j = 0
i = 2 and j = 1
"""



# break and continue in nested loop

for i in range(3): # 0, 1, 2
    for j in range(3): # 0, 1, 2
        if i == j: # first time 0==0 become True so break will execute and control will go out of inner loop
            break
        print(i, j)
print("\n")

"""
i = 0
    j = 0 break
    j = 1
    j = 2
i = 1
    j = 0
    j = 1 break
    j = 2
i = 2
    j = 0
    j = 1
    j = 2 break

"""

for i in range(3): # 0, 1, 2
    for j in range(3): # 0, 1, 2
        if i == j: # first time 0==0 become True so break will execute and control will go out of inner loop
            continue
        print(i, j)


"""
i = 0
    j = 0 continue
    j = 1
    j = 2
i = 1
    j = 0
    j = 1 continue
    j = 2
i = 2
    j = 0
    j = 1
    j = 2 continue

"""
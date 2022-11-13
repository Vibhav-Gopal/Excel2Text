import numpy as np
help = '''
For example: 
1 0 0
0 1 0
0 0 1
for the above matrix the first input would be \'1 0 0\' 
the second input would be \'0 1 0\' and so on
'''

objectives = int(input("How many objectives?\n"))
obj = objectives
mat = []
print("Enter the adjacency matrix")
print(help)
for i in range(obj):
    row = input()
    row = list(map(int, row.split()))
    mat.append(row)
mat = np.array(mat)
reach = mat + np.identity(obj)
reach = np.clip(reach,0,1)
reacht = reach
for i in range(100):
    n = i+1
    reacht=reach**n
    reacht = np.clip(reacht,0,1)
    if np.array_equal(reach, reacht) :
        print(f'n-value is {n+1}')
        print("Matrix is")
        for k in reacht:
            print(k)
        break
    else:
        reach = reacht

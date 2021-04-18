from heapq import merge
import pandas as pd

def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup

# Driver Code
R = [("Kumar", 2),
     ("Wess", 1),
     ("Terry", 1),
     ("Gowri", 2),
     ("Morgan", 3),
     ("Sachin", 3)
     ]  # EName,DeptNo

S = [("Design", 1),
     ("Production", 2),
     ("Administration", 3)
     ]  # DName,DeptNo

dfr = pd.DataFrame(R, columns=['EName', 'DeptNo'])
print(dfr)
print("\n")
dfs = pd.DataFrame(R, columns=['DName', 'DeptNo'])
print(dfs)
print("\n")
# printing the sorted list of tuples
# print(Sort_Tuple(R))
# print(Sort_Tuple(S))
tmp1 = Sort_Tuple(R)
dfsr = pd.DataFrame(tmp1, columns=['EName', 'DeptNo'])
print(dfsr)
print("\n")
tmp2 = Sort_Tuple(S)
dfss = pd.DataFrame(R, columns=['DName', 'DeptNo'])
print(dfss)
print("\n")
i = tmp1[0][1]
# print(i)
j = tmp2[0][1]
print("\n")  # print(j)
join = []

for i in range(0, 6):  
    for j in range(0, 3):
        # print(i,j)
        if tmp1[i][1] == tmp2[j][1]:
            join.append(tmp1[i])
            join.append(tmp2[j])
            break

# print(join)
# print("\n")

for i in range(0, len(tmp1) + len(tmp2) + 3):  # or (len(tmp1)*2)+1
    if i % 2 == 0:
        print(join[i][0], "  ", end='')
    else:
        print(join[i][0], "\n")
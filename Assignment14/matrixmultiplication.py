m=[[2, 2],
    [1, 1]]    
n=[[2, 2],
  [1, 1,]]
res=[[0, 0],
        [0, 0]]
for i in range(len(m)):

    for j in range(len(n[0])):

        for k in range(len(n)):
            res[i][j] += m[i][k]*n[k][j]
 
for r in res:
    print(r)

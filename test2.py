n  = [1,2,1,5,7,1,3,10]

for i in range(len(n)):
    for j in range(len(n)-1):
        if n[j] > n[j+1]:
          temp = n[j]
          n[j] = n[j+1]
          n[j+1] = temp
print n

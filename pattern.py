n=int(input())
#upper
#rows
for i in range(1,n+1):
    #space
    for j in range(n-i):
        print(' ',end="")
    #star
    for j in range((2*i)-1):
        print('*',end="")
    print()
for i in range(n,0,-1):

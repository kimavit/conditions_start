n= [int(i) for i in input().split()]
x= len(n)
if x==1:
    print(n[0])
else:
 for i in range (x-1):
    print ('', n [i+1] + n [i-1], end = '' )
 else:
    print('', n [-2] + n [0], end = '' )
result=1
n=int(input('enter the number to find factorial of'))
if n>1:
    for i in range(2,n+1):
        result*=i

    print(result)
elif n==1 or n==0:
    print(result)

else:
    print('factorial not defined')

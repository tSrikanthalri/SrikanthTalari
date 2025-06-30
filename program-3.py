a = int(input('enter the number: '))

if (a%2==0):
    a-= 1

for num in range(a):
    print(2*num+1,end = " ")

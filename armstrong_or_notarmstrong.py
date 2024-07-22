n=int(input(''))
sum=0
temp=n
while(n>0):
    rem=n%10
    sum+=rem*rem*rem
    n=n//10
if(temp==sum):
    print('armstrong')
else:
    print('are not armstrong')

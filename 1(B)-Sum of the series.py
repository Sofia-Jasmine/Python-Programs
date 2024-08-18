n=int(input('Enter a Value of n:'))
s=0
for i in range(1,n+1):
    a=(i**i)/i
    s=s+a
print ('The sum of series is',s)

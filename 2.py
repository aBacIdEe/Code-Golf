a,b=0,1
n=int(input())
for _ in range(n-1):
    a=a+b
    a,b=b,a
print(b)
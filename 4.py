x=input()
s=x[-1]
a=0
for _ in x:a=a+1 if _==s else a
print(a-1)
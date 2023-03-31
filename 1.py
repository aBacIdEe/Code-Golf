a=input()
l=len(a)
t=''
if l<3:t=a
else:t=a[0]+str(l-2)+a[-1]
print(t)
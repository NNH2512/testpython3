a=int(input('nhap a:'))
b=int(input('nhap b:'))
c=int(input('nhap c:'))
if a>b:
    temp=a
    a=b
    b=temp
if a>c:
    temp=a
    a=c
    c=temp
if b>c:
    temp=b
    b=c
    c=temp
print(a,b,c,sep=' ')
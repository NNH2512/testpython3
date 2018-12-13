def cachtinh():
    n=int(input('nhap so can tinh:'))
    fac=1
    for i in range(1,n+1):
        fac *=i
    print(str(n)+'!=',fac,sep=' ')
cachtinh()
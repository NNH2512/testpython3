year=int(input('nhap nam can tinh:'))
leap=False
if year%400==0:
    leap=True
elif year%100==0:
    leap=False
elif year%4==0:
    leap=True
if leap:
    print(str(year)+'うるう年')
else:
    print(str(year)+'うるう年じゃない')

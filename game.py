import random
print('0=gu,1=choki,2=pa-')
yourturn=int(input('nhap luot cua ban:'))
comp=random.randint(0,2)
if comp==0:
    compstr='comp =gu'
    if yourturn==0:
        yourturnstr='yourturn=gu'
        result='hoa'
    elif yourturn==1:
        yourturnstr='yourturn=choki'
        result='you lost'
    else:
        yourturnstr='yourturn=pa-'
        result='you win'
if comp==1:
    compstr='comp=choki'
    if yourturn==0:
        yourturnstr='tournturn=gu'
        result='you win'
    elif yourturn==1:
        yourturnstr='yourturn=choki'
        result='hoa'
    else:
        yourturnstr='yourturn=pa-'
        result='you lost'
if comp==2:
    compstr='comp=pa-'
    if yourturn==0:
        yourturnstr='yourturn=gu'
        result='you lost'
    elif yourturn==1:
        yourturnstr='yourturn=choki'
        result='you win'
    else:
        yourturnstr='yourturn=pa-'
        result='hoa'
print(compstr+yourturnstr+result)





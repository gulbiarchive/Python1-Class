t1, t2 = map(int, input().split())

if ((t1 >= 35) and (t2 >= 35)):
    print('폭염경보')
elif ((t1 >= 33) and (t2 >= 33)):
    print('폭염주의보')
else:
    print('이상무')
    
    
    
angle=[]

#09:00-90 degree
for i in range(0,12,1):
    angle=(90+i*30-i*2.5)
    print(angle%360)
    
print()

#10:00-60 degree
for i in range(0,12,1):
    angle=(60+i*30-i*2.5)
    print(angle%360)
    
print()

#11:00-30 degree
for i in range(0,12,1):
    angle=(30+i*30-i*2.5)
    print(angle%360)
    
print()


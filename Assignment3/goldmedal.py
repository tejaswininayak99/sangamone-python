names=[]
subjects=[]
eng=[]
maths=[]
physics=[]
chem=[]
bio=[]
engToppers=[]
mathsToppers=[]
physicsToppers=[]
chemToppers=[]
bioToppers=[]

strPath=open("D:\python\mark.txt","r")
t=strPath

for i in range(0,26,1):

        info=t.readline()
        list1=info.split(",")
        names.append(list1[0])
        
        list2=list1[3].split(":")
        subjects.append(list2[0])
        eng.append(list2[1])
                
        list2=list1[4].split(":")
        subjects.append(list2[0])
        maths.append(list2[1])
                   
        list2=list1[5].split(":")
        subjects.append(list2[0])
        physics.append(list2[1])
          
        list2=list1[6].split(":")
        subjects.append(list2[0])
        chem.append(list2[1])
         
        list2=list1[7].split(":")
        subjects.append(list2[0])
        bio.append(list2[1])
print(list2[0])
print(eng)
maxEng=max(eng)
print(maxEng)

print(list2[0])
print(maths)
maxMaths=max(maths)
print(maxMaths)

print(list2[0])
print(physics)
maxPhysics=max(physics)
print(maxPhysics)

print(list2[0])
print(chem)
maxchem=max(chem)
print(maxchem)

print(list2[0])
print(bio)
maxbio=max(bio)
print(maxbio)

for i in range(0,26,1):
    if eng[i]==maxEng:
        engToppers.append(names[i])
print(engToppers,"are the toppers in",subjects[0],"with marks of",maxEng)

for i in range(0,26,1):
    if maths[i]==maxMaths:
        mathsToppers.append(names[i])
print(mathsToppers,"are the toppers in",subjects[1],"with marks of",maxMaths)
        
for i in range(0,26,1):
    if physics[i]==maxPhysics:
        physicsToppers.append(names[i])
print(physicsToppers,"are the topppers in",subjects[2],"with marks of",maxPhysics)

        
for i in range(0,26,1):
    if chem[i]==maxchem:
        chemToppers.append(names[i])
print(chemToppers,"are the topppers in",subjects[3],"with marks of",maxchem)

for i in range(0,26,1):
    if bio[i]==maxbio:
        bioToppers.append(names[i])
print(bioToppers,"are the topppers in",subjects[4],"with marks of",maxbio)





  
##built for remove same maximum values
def samemax(a):
    a.sort()
    b=0
    temp=0
    while a[b-1]==a[b-2]:
        del a[b-1]
        a.sort()
        b=len(a)
        temp=a[b-1]
    if a[len(a)-1]==temp:
        del a[len(a)-1]
        a.sort()
    else:
        a[len(a)-1]==max(a)
        del(a[len(a)-1])
        a.sort()
#main program
def sheepnotice(a,n):
    print('begining balance xd gg',a)
    for i in range(n):
        print('MONTH',i+1)
        mx=max(a)
        print('my biggest sheep:',mx,'let fukin cut its hair')
        count1=len(a)
        #shearing
        samemax(a)
        count2=len(a)
        for _ in range(0,count1-count2):
            a.append(8)
        print('my sheeps after being sheard:',a)
        a=list(map(lambda x:x+50,a))
        print('after growth',a)
    bored(a,2)
def bored(a,s):
    total=0
    for i in a:
        total=total+i
    print('my flock has total size: ',total)
    print('my total fukin money  $',total*s)     
print('Hello my name is unknown and there is my sheep sizes xd')
#nhap 1 day size cuu vao day
size=[500,7,90,24,500,75,90]
sheepnotice(size,4)


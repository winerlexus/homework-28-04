  
##built for remove same maximum values
def samemax(a):
    temp=max(a)
    for i in range(len(a)) :
        if a[i]==temp:
            a[i]=8
#main program
def sheepnotice(a,n):
    print('begining balance xd gg',a)
    for i in range(n):
        print('MONTH',i+1)
        mx=max(a)
        print('my biggest sheep:',mx,'let fukin cut its hair')
        #shearing
        samemax(a)
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
size=[100,100,100,200,300,400,500,600,600,600]
sheepnotice(size,4)


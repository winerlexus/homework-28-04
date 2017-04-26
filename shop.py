
def c():
        a=input(print('enter new items: '))
        items.append(a)
        print('our items: ',items)
def r():
        print('our items:', items)
def u():
        a=int(input(print('update position')))
        b=input('which item do you want to update: ')
        items.insert(a,b)
        print('our items: ',items)
def d():
        a=int(input('delete position? '))
        del(items[a])
        print('our remaining:', items)
        

print('Welcome to our shop, what do you want (C,R,U,D)?')
a=input()
items=['T-shirt','Sweater']
if a=='c': c()
elif a=='r': r()
elif a=='u' : u()
else: d()



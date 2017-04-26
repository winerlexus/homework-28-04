from turtle import *
speed(0)
colors=['red', 'blue', 'brown', 'yellow', 'grey']
####turtle 01:
def mulshape(n):
    for i in range(n,2,-1):
        color(colors[i-n+4])
        for i2 in range(0,i):   
            forward(100)
            left(360/i)
mulshape(7)

###turtle 02:
def numsbox(n,width,long):
    for i in range(n,-1,-1):
        color(colors[i-n+4])
        for i2 in range(0,2):
            begin_fill()
            forward(width*i)
            left(90)
            forward(long)
            left(90)
            end_fill()
numsbox(5,50,100)

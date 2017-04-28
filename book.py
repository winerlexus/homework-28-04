###nested list?
a list in another list is called nested list

###list can contain both str and int

###excercise1:
####What is the Python interpreter’s response to the following?
```python
list(range(10, 0, -2))
```
> `>>>[10,8,6,4,2]`
###What happens if `start` < `stop` and `step` < 0?
> it will generate a empty `list`
Rules:
> Start<stop if step>0
> Start>stop if strep<0
    
###excercise2:
#### Consider this fragment of code:
```python
import turtle
tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
```
#### Does this fragment create one or two turtle instances?Does setting the color of `alex` also change the color of `tess`? Explain in detail.   
Line `tess.tutrle.Turtle()` create an object. `alex` will be refered to `tess`.
Any change in `alex` lead to change in `tess`.
###### so it will change the color of `tess` [x] just check

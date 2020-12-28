from math import *
def function(x):
    function = (tan(x) + cos(x))**0.5#input your function
    return(function)

#Input your upper,lower and interval variables
upper = 1
lower = 0
intervals = 4
h = (upper - lower)/ intervals  #The value of each step
z = intervals/2 # The number of even functions(z+1 is the number of odd functions)
ans = 0


def simpsonsrule():
    rule = 0
    x = lower + h#Calculates for all odd valures
    for i in range(1,int(z+1)):
        rule += 4*function(x)#adds all calculations to variable rule
        x += 2*h

    x = lower + 2*h#Calculates for all even values
    for i in range(1,int(z)):
        rule += 2*function(x)#adds all calculations to variable rule
        x += 2*h
    ans = (h/3)*(function(lower)+function(upper)+rule)#This is carrying out the formula
    return (ans)



def trapeziumrule():
    rule = 0
    x = lower
    rule += function(x)#adds lower value to rule
    x = upper
    rule += function(x)#adds upper value to rule
    for i in range(1,intervals):#all values inbetween
        x = lower + h*i
        rule += 2*(function(x))#adds these to the rule
    ans = (h/2)*rule#completes the function
    return(ans)

print(trapeziumrule())

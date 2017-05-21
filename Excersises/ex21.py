def add(a,b):
    print("Adding %d+%d"%(a,b))
    return a+b

def subtract(a,b):
    print("Subtracting %d-%d"%(a,b))
    return a-b

def multiply(a,b):
    print("Multiplying %d,%d"%(a,b))
    return a*b

print("lets do some math function")

age=add(1,2)
height=subtract(3,1)
weight=multiply(4,3)

print("Age:%d,height:%d,weight:%d"%(age,height,weight))

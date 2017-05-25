i=0
numbers=[]

while i<6:
    print("At the top i is %d"%i)
    numbers.append(i)

    i=i+1
    print("Print numbers now:",numbers)

print("The numbers:")

for num in numbers:
    print (num)

print("All at once:",numbers) 

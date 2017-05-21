the_count=[1,2,3,4,5]
fruits=['apples','oranges','pears','apricots']
change=[1,'pennis',2,'dimes',3,'quarters']

#comment
for number in the_count:
    print ("This is count %d"%number)

#again
for fruit in fruits:
    print("This friut is %s"%fruit)

#going through mixed list
for i in change:
    print("this is %r"%i)

#bulding our own lists

elements=[]
elements=range(0,6)
for i in range(0,6):
    print ("adding %r to the list"%i)
    elements.append(i)

for i in  elements:
    print("Value in our created list:%d"%i)

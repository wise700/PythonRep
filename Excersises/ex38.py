ten_things="These are the ten things of holy"

print("Ohh there not then things in list,lets fix it")

stuff=ten_things.split(" ")
print (stuff)
more_stuff=['oranges','apples','peaches','bagpack']

while len(stuff)<10:
    new_item=more_stuff.pop()
    print("adding item:%s"%new_item)
    stuff.append(new_item)

print("All stuffs:",stuff)

print (stuff[1])
print (stuff[-1])
print (stuff.pop())
print (''.join(stuff))
print('#'.join(stuff[3:5]))

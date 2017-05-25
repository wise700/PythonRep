states={
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

cities={
'CA':'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

#adding some more cities
cities['NY']='New York'
cities['OR']='portland'

#print out some cities
print ('-'*10)
print("Michigan's abbrevation is: ",states['Michigan'])
print("Florid's abbrevatio is:",states['Florida'])

#print every state abbrevation
print ('-'*10)
for state in states:
    print("abbrevation of %s is : %s"%(state,states[state]))
#print every city in state
print('-'*10)
for city,abb in cities.items():
    print("%s has the city %s"%(city,abb))

print ("Lets practice Everything")
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabbing')

poem="""
\t the lovely world
with logic
asdfsdf
vdfsdf\ns
dsf
"""

print ("------------------")
print (poem)
print ("------------------")

def secert_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates

start_point=10000
beans,jars,crates=secert_formula(start_point)

print("with a starting point of :%d"%start_point)
print("We'd have %d beans,%d jars,and %d crates"%(beans,jars,crates))

start_point=start_point/10

print("We can also do that this way:")
print("We'd have %d beans,%d jars,%d crates"%secert_formula(start_point))

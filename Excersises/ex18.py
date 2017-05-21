def print_two(*args):
    arg1,arg2=args
    print ("arg1:%r,arg2:%r"%(arg1,arg2))

#ok, args* is pointless
def print_two_again(arg1,arg2):
    print ("arg1:%r,arg2:%r"%(arg1,arg2))

#this takes just one argument
def print_one(arg1):
    print("arg1:%r"%arg1)

#this takes no arguments
def print_zero():
    print("I have no arguments to print")

print_two_again(1,2)
print_two(1,2)
print_one("one")
print_zero()

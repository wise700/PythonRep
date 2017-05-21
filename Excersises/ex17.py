from sys import argv
from os.path import exists

script,from_file,to_file=argv
print("Copying from %s to %s"%(from_file,to_file))

#df

in_file=open(from_file)
indata=in_file.read()

print("Input file is %d bytes long"%len(indata))

print("Does the output file exsist? %r"% exists(to_file))

print("ready, hit RETURN to continuw, ctl-c to abort")

input()

outfile=open(to_file,'w')
outfile.write(indata)

print("Alright, alldone")

outfile.close()
in_file.close()

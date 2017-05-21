file_name=input("Filename>")

print("Do you want %s to be truncated?, Press Enter to continue"%file_name)

target=open(file_name,'w')
target.truncate

line1=input("gimme line1:")
line2=input("gimme line2:")
line3=input("gimme line3:")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close

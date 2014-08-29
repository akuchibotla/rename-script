import sys
import os

if len(sys.argv) != 2:
	raise RuntimeError("Insufficient Arguments: must provide one and only one path")

path = str(sys.argv[1])
print path

files = os.listdir(path)

if files == 256:
	raise RuntimeError("Incorrect path")

counter = 0

for f in files:
	for i in range(len(f)):
		if f[::-1][i] == ".":
			extention = "." + f[::-1][:i][::-1]
	if path[-1] != "/":
		path += "/"
	bash_command = "mv " + path + f + " " + path + str(counter) + extention
	print bash_command
	val = os.system(bash_command)
	if val != 0:
		raise RuntimeError("Error in bash_command ", bash_command)
	print "Done"
	print ""
	counter += 1
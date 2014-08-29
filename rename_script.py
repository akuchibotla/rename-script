import sys
import os

if len(sys.argv) < 2:
	raise SystemExit("Insufficient Arguments: must provide an argument\n\nCorrect Format:\npython <path to script>/rename_script.py <path to files to be renamed> <optional prefix> <optional suffix>")

elif len(sys.argv) == 3:
	prefix = sys.argv[2]

elif len(sys.argv) == 4:
	prefix = sys.argv[2]
	suffix = sys.argv[3]

else:
	raise SystemExit("Insufficient Arguments: must provide at most 3 arguments in order\n\nCorrect Format:\npython <path to script>/rename_script.py <path to files to be renamed> <optional prefix> <optional suffix>")

path = str(sys.argv[1])
print path

files = os.listdir(path)

if files == 256:
	raise SystemExit("Incorrect path")

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
		raise SystemExit("Error in bash_command ", bash_command)
	print "Done"
	print ""
	counter += 1
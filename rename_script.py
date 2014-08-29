import sys
import os

prefix = ""
suffix = ""

# Raises error if too many arguments are provided
if len(sys.argv) < 2:
	raise SystemExit("Insufficient Arguments: must provide an argument\n\nCorrect Format:\npython <path to script>/rename_script.py <path to files to be renamed> <optional prefix> <optional suffix>")

# Sets prefix
elif len(sys.argv) == 3:
	prefix = sys.argv[2]

# Sets prefix and suffix
elif len(sys.argv) == 4:
	prefix = sys.argv[2]
	suffix = sys.argv[3]

# Raises Error when too many arguments are provided
elif len(sys.argv) > 4:
	raise SystemExit("Insufficient Arguments: must provide at most 3 arguments in order\n\nCorrect Format:\npython <path to script>/rename_script.py <path to files to be renamed> <optional prefix> <optional suffix>")

# Sets path
path = str(sys.argv[1])
print "Renaming files in ", path

# Prevents unwanted renaming
raw_input("Press Enter to continue")

files = os.listdir(path)

# If path doesn't exist
if files == 256:
	raise SystemExit("Path does not exist: ", path)

counter = 0

# Iterates through every file in path folder
for f in files:
	# Sets extention uniquely per file
	for i in range(len(f)):
		if f[::-1][i] == ".":
			extention = "." + f[::-1][:i][::-1]
	# Adds the needed backslash at the end of the path if there isn't one provided by the user
	if path[-1] != "/":
		path += "/"
	# Sets bash command to be a simple mv operation
	bash_command = "mv " + path + f + " " + path + prefix + str(counter) + suffix + extention
	print bash_command
	val = os.system(bash_command)
	# Verifies that the bash command is a legal operation
	if val != 0:
		raise SystemExit("Error in bash_command ", bash_command)
	print "Done"
	print ""
	counter += 1
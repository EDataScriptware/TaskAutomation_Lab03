# Name: Edward Riley
# Professor: Erik Golen
# Course: Task Automation
# Assignment: Lab3 - Task2
# Date: 03/24/19

# Import necessary packages
import sys, os

# File name (md5.txt) will be read through and checked.
file_name = sys.argv[1]
# We set up an array
L=[]
# The file location is set up to save us the trouble of manually clicking every directory
file_location = "/usr/bin/"
broken = 0

# We want to open the file to only read it
open_file = open(file_name,'r')

# For each line that we read in the file, it will be split up and stored in L array
for line in open_file:
	line = line.strip()
	L.append(line.split(' '))

	# For each file that we read in L array, we will begin hash process
for file in L:
	# For each file that we need to hash will be stored in big file 
	big_file = file_location + file[0]

	# We begin the process to start hashing
	test = os.system("md5sum " + big_file + "| awk '{print $1}' > hash.txt")

	# While we have hash.txt open, we begin to "read" hash
	with open('hash.txt') as hashfilereader:
		for hash in hashfilereader:
			
			hash = hash.strip()
			if str(hash) != str(file[1]):
				broken +=1
				#We "convert" the original to str hash
				print str(file[0]) + "  MD5 original = " + str(file[1]) + ", MD5 new = " + str(hash)
open_file.close()

# To tell us when the program is done computing.
print "All Completed!"

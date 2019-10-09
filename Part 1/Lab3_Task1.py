# Name: Edward Riley
# Professor: Erik Golen
# Course: Task Automation
# Assignment: Lab3 - Task1
# Date: 03/24/19

# We import necessary package
import sys

# We develop a function to read data
def read_data(file_name, L):
	
	true_or_false = False
	file_open = open(file_name,'r')

	for line in file_open:
		if line == "@DATA\n":
			true_or_false = True

	 	elif true_or_false:
			line = line.strip()
			L.append(line.split(","))

			

# We developed a function to read Minimum, Maximum, and Average function
def process_numeric_field(L, field):

	minimum_ = L[0][0]
	maximum_ = 0
	average = 0
	
	for val in L:

		if val[field-1] < minimum_:
			minimum_ = val[field-1]

		if val[field-1] > maximum_:
			maximum_ = val[field-1]

		average = average + float(val[field-1])

	true_average = average/len(L)
	
	return minimum_, maximum_, true_average



def count_iris_types(L):

	setosa = 0
	versicolor = 0
	virginica = 0 	

	for val in L:

		if val[4] == "Iris-setosa":
			setosa += 1
		
		if val[4] == "Iris-versicolor":
			versicolor += 1

		if val[4] == "Iris-virginica":
			virginica += 1

	return setosa, versicolor, virginica

L = []
input_file = sys.argv[1]
 
read_data(input_file,L)

sepal_length_minimum, sepal_length_maximum, sepal_length_average = process_numeric_field(L,1)
sepal_width_minimum, sepal_width_maximum, sepal_width_average = process_numeric_field(L,2)
petal_length_minimum, petal_length_maximum, petal_length_average = process_numeric_field(L,3)
petal_width_minimum, petal_width_maximum, petal_width_average = process_numeric_field(L,4)
setosa, versicolor, virginica = count_iris_types(L)
 

print "Sepal Length: min = " + str(sepal_length_minimum) + ", max = " + str(sepal_length_maximum) + ", average = " + str(round(sepal_length_average,1))
print "Sepal Width: min = " + str(sepal_width_minimum) + ", max = " + str(sepal_width_maximum) + ", average = " + str(round(sepal_width_average,1))
print "Petal Length: min = " + str(petal_length_minimum) + ", max = " + str(petal_length_maximum) + ", average = " + str(round(petal_length_average,1))
print "Petal Width: min = " + str(petal_width_minimum) + ", max = " + str(petal_width_maximum) + ", average = " + str(round(petal_width_average,1))
print "Iris Types: Iris Setosa = " + str(setosa) + ", Iris Versicolor = " + str(versicolor) + ", Iris Virginica = " + str(virginica) 


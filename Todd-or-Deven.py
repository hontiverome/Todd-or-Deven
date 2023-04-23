# Write a method in python that will create two seperate text files 
# after reading the source text file named integers.txt that cotains 20 integers. 
# The first output will be named double.txt containing the square of all even integers found in integers.txt  
# the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt

# define the method/function
# read and write the input and output files
with open("integers.txt", "r") as integer_file, open ("squared_even.txt", "w") as even_file, open ("cubed_odd.txt", "w") as odd_file:
    
# put the numbers from the read file into a list and convert it into integers
# iterate the list
# identify whether integer is even or odd using mod
# if even, square it, and write it to "squared_even.txt" file
# if odd, cube it, and write it to "cubed_odd.txt" file
# Write a method in python that will create two seperate text files 
# after reading the source text file named integers.txt that cotains 20 integers. 
# The first output will be named double.txt containing the square of all even integers found in integers.txt  
# the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt

# define the method/function
# read and write the input and output filesd
import time
def sEven_cOdd_itegers():
    with open("integers.txt", "r") as integer_file, open ("squared_even.txt", "w") as even_file, open ("cubed_odd.txt", "w") as odd_file:
        # put the numbers from the read file into a list and convert it into integers
        integers=[line.strip()for line in integer_file]
        integer_list=[int(j) for j in integers]
        # iterate the list
        for num in integer_list:
            # identify whether integer is even or odd using mod
            # if even, square it, and write it to "squared_even.txt" file
            if num%2==0:
                squared=num**2
                even_file.write(str(squared)+'\n')
            # if odd, cube it, and write it to "cubed_odd.txt" file
            else:
                cubed=num**3
                odd_file.write(str(cubed)+'\n')
def check_contents():
    with open("integers.txt", "r") as integer_file:
        contents=str(input("Would you like to see the contents of 'numbers.txt?' (y or n)\n"))
        while True:
            if contents=='y':
                integers=[lines.strip() for lines in integer_file]
                integer_list=[int(j) for j in integers]
                print(integer_list)
                break
            elif contents=='n':
                break
            else:
                print("invalid")
                contents=str(input("Would you like to see the contents of 'numbers.txt?' (y or n)\n"))
                continue
        
def open_text():
    with open ("squared_even.txt", "r") as even_file, open ("cubed_odd.txt", "r") as odd_file:
        response=str(input("\nWould you like to print out the contents of the text files? (y or n only):\n "))
        while True:
            if response=='y':
                print_response=str(input("\nWhat text file would you like to see? (even, odd, exit):\n "))
                if print_response=='even':
                    print("You chose even.")
                    time.sleep(0.5)
                    even_result=("Here is the squared even list.\n")
                    for i in range(len(even_result)):
                        print(even_result[i], end='', flush=True)
                        time.sleep(0.1)
                    for line in even_file:
                        print(line.strip().rjust(25)+'\n')
                    print('__________________________________________________________________________________________________')
                elif print_response=='odd':
                    print("You chose odd.")
                    time.sleep(0.5)
                    even_result=("Here is the cubed odd list.\n")
                    for i in range(len(even_result)):
                        print(even_result[i], end='', flush=True)
                        time.sleep(0.1)
                    for line in odd_file:
                        print(line.strip().rjust(25)+'\n')
                    print('__________________________________________________________________________________________________')
                elif print_response=='exit':
                    print("\nThank you.")
                    exit()
                else:
                    print("Invalid")
                    print("____________________________________________________________________________________________________")
            elif response=='n':
                print("\nThank you.")
                exit()
            else:
                print("Invalid")
                print("____________________________________________________________________________________________________")

# Execute the code
sEven_cOdd_itegers()
check_contents()
open_text()

# HONTIVEROS JEROME ANDREI O.
# BSCPE 1-5
# Write a method in python that will create two seperate text files 
# after reading the source text file named integers.txt that cotains 20 integers. 
# The first output will be named double.txt containing the square of all even integers found in integers.txt  
# the second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt

# define the method/function
# read and write the input and output filesd
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

        
def open_text():
    with open ("squared_even.txt", "r") as even_file, open ("cubed_odd.txt", "r") as odd_file:
        response=str(input("\nWould you like to print out the contents of the text files? (y or n only):\n "))
        while True:
            if response=='y':
                print_response=str(input("\nWhat text file would you like to see? (even, odd, exit):\n "))
                if print_response=='even':
                    for line in even_file:
                        print(line.strip().rjust(25)+'\n')
                    print('__________________________________________________________________________________________________')
                elif print_response=='odd':
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
open_text()

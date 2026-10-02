# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    # ADD a Docstring for this function
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    x_str = input("give me x: ")
    x = int(x_str)
    
    y_str = input("give me y: ")
    y = int(y_str)
    
    return x,y
"""This function "read_two_ints()" takes two parameters, x and y.
it intakes them as a string and turns them into an integer"""

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    mult_result = a*b
    print("mult result:", mult_result)
    add_result = a+b
    print("add result:", add_result)
    return(mult_result/add_result)
    
"""This function takes two parameters, a and b.
it defines mult_result and a*b and prints it
it defines add_result as a+b and prints it
it returns the result of (a*b)/(a+b), or (mult_result/add_result)"""

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    print("****************")
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print("="*16)

"""this function prints the results from the above calculations"""

def main ():
"""this function calls all the functions I defined that need to run to create my final result.
they have to run in "main" because that's where the main code is hosted."""

    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    x, y = read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    # TODO: add your call instead of this line
    xy_multadd = compute_multadd(x,y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;
    print_fancy(x, y, xy_multadd)
    


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()

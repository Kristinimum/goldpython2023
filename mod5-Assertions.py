#assertions are certain assumptions in our program that we think should always be true. 
#assertions are used for debugging and testing and doc code but not for validating user input
#assertion is not an error handling tool.
def calculate_inverse(number):
    assert (number != 0), 'Got 0 as number!'
    return 1/number
    
calculate_inverse

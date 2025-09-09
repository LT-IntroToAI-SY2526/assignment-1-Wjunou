# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[I am currently in highschool programing calss. I have experince with Jave, Html, Css and Bootstrap.
 Can you please create 6-7 practice problems that cover the basics of pythonas well as explanations]

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [What is the correct syntax to output 'Hello, World' in Python?]
[console.log('Hello, World')


print('Hello, World')


System.out.println('Hello, World')


echo('Hello, World')]

PROBLEM 2[Which data type is used to store a sequence of characters in Python?]
[
str


int


float


bool
]

PROBLEM 3[What will be the output of the following code? x = 5 print(x * 2)]
[
2


7


25


10
]
PROBLEM 4[Which of the following is a valid Python list?]
[{1, 2, 3}


<1, 2, 3>


[1, 2, 3]


(1, 2, 3)]
PROBLEM 5[What does the following code do?

fruits = ['apple', 'banana', 'cherry'] for fruit in fruits: print(fruit)]
[Sorts the list alphabetically


Prints the length of the list


Prints each fruit in the list


Adds a new fruit to the list]
PROBLEM 6[Which keyword is used to define a function in Python?]
[function


fun


def


define]
PROBLEM 7[What will be the output of the following code?

def greet(): return 'Hello'

print(greet())]
[greet


None


Error


Hello]

Example:Write  fucntion called factoria that takes in integer and returns the factorial.
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""
def factorial(n: int) -> int:
    """Calculate the factorial of a given integer.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Iterative factorial:")
print(f"factorial(0) = {factorial(0)}")  # Expected: 1
print(f"factorial(1) = {factorial(1)}")  # Expected: 1
print(f"factorial(5) = {factorial(5)}")  # Expected: 120
print(f"factorial(6) = {factorial(6)}")  # Expected: 720
print(f"factorial(10) = {factorial(-10)}")  

    
# Test error handling
print("\nError handling:")
try:
    factorial(-1)
except ValueError as e:
    print(f"Error: {e}")


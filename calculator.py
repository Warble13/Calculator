def userinput():
    """
    Takes the user input and determins what equation to run

    Arguments:
    -None

    Returns:
    -equation (list) The equation the user inputted

    """
    output = None
    equationinput = input("Input your equation. ")
    equation = list(equationinput.split())
    equation[1] = int(equation[1])
    equation[2] = int(equation[2])
    if equation[0] == '+':
        add(equation, output)
    elif equation[0] == '-':
        subtract(equation, output)
    elif equation[0] == '/':
        divide(equation, output)
    elif equation[0] == '*':
        multiply(equation, output)
    elif equation[0] == '**':
        exponent(equation, output)
    else:
        userinput()
    return equation

def multiply(equation, output):
    """
    Multiplies the two numbers together

     Arguments:
    - equation (list) What the user inputted
    - output (None) What the answer will be.

    Returns:
    - None

    """
    output = equation[1] * equation[2]
    print(str(output))

def divide(equation, output):
    """
    Divides the first number by the second

     Arguments:
    - equation (list) What the user inputted
    - output (None) What the answer will be.

    Returns:
    - None
    """
    output = equation[1] / equation[2]
    print(str(output))

def add(equation, output):
    """
    Adds the two numbers.

     Arguments:
    - equation (list) What the user inputted
    - output (None) What the answer will be.

    Returns:
    - None

    """
    output = equation[1] + equation[2]
    print(str(output))

def subtract(equation, output):
    """
    Subtracts the second number from the first.

    Arguments:
    - equation (list) What the user inputted
    - output (None) What the answer will be.

    Returns:
    - None

    """
    output = equation[1] - equation[2]
    print(str(output))

def exponent(equation, output):
    """
    Multiplys the first number to a power of the second number.

    Arguments:
    - equation (list) What the user inputted
    - output (None) What the answer will be.

    Returns:
    - None
    """
    output = equation[1] ** equation[2]
    print(str(output))

def main():
    """
    Runs the program

    Arguments:
    - None

    Returns:
    - None

    """
    while True:
        userinput()
    
main()

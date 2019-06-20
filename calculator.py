def userinput():
    output = None
    equationinput = input("Input your equation. ")
    equation = list(equationinput.split())
    equation[1] = int(equation[1])
    equation[2] = int(equation[2])
    if equation[0] == '+':
        add(equation, output)
    if equation[0] == '-':
        subtract(equation, output)
    if equation[0] == '/':
        divide(equation, output)
    if equation[0] == '*':
        multiply(equation, output)
    if equation[0] == '**':
        exponent(equation, output)
    return equation

def multiply(equation, output):
    output = equation[1] * equation[2]
    print(str(output))

def divide(equation, output):
    output = equation[1] / equation[2]
    print(str(output))

def add(equation, output):
    output = equation[1] + equation[2]
    print(str(output))

def subtract(equation, output):
    output = equation[1] - equation[2]
    print(str(output))

def exponent(equation, output):
    output = equation[1] ** equation[2]
    print(str(output))

def main():
    while True:
        userinput()
    
main()

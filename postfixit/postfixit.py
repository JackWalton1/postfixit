# Name:         Jack Walton
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Postfix-It
# Term:         Winter 2021

from typing import Optional


def main() -> None:
    """
    Iteratively prompt the user for an infix expression and display both the
    postfix equivalent and, on the next line, the result as a float (even if it
    is a whole number) rounded to 3 decimal places. Assume the infix expression
    is properly formatted.
    """
    while True:
        try:
            infix = input(">>> ")
            # insert all code for main below this line

            postfix = build_postfix(infix)
            print(postfix)

            solution = solve_postfix(postfix)
            print(solution)

        except EOFError:  # loop breaks with CTRL+d
            break
    print()  # empty line prints before program ends
    # end of main (no return statement is equivalent to |return None|)



def is_operator(string: str) -> bool:
    """ function to return a bool pertaining to 
    whether operator(True) or opperand(False)
    """
    if string == "+" or string == "-":
        return True
    elif string == "*" or string == "/":
        return True
    elif string == "^":
        return True
    else:
        return False



def is_number(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False



def prec(string: str) -> Optional[int]:
    """ giving a value to precedence for PEMDAS
    but more like EMDASP in order to exclude 
    parentheses from being built on posftix eq.
    """
    if string == "+" or string == "-":
        return 1
    elif string == "*" or string == "/":
        return 2
    elif string == "^":
        return 3
    else:
        return 0



def build_postfix(infix: Optional[str]) -> Optional[str]:
    """ inputs string of infix equation (spaces required)
    and outputs a string of postfix version of equation
    »»» infix = "(( 1 + 2 ) * 3 - ( 4 - 5 ) * ( 6 + 7 ))"
    »»» build_postfix(infix)
    "1 2 + 3 * 4 5 - 6 7 + * -"
    """
    stack = []
    inf_list = infix.split(" ")
    postfix = []
    # number of consecutive operators (not split by parentheses)
    # num_operators = 0
  
    for char in inf_list:
        # if negative or float, skips over this
        if is_number(char): 
            postfix.append(char)

        elif char == "(" or char == "^":
            stack.append(char)

        elif char == ")":
            value = stack.pop()
            while value != "(":
                postfix.append(value)
                value = stack.pop()

        elif is_operator(char):
            if len(stack) > 0:
                top_char = stack[-1]
            
                while prec(top_char) >= prec(char) and len(stack) > 0:
                    postfix.append(top_char)
                    stack.pop()
                    if len(stack) > 0:
                        top_char = stack[-1]
                            
            stack.append(char)

    while len(stack) > 0:
        postfix.append(stack.pop())

    return " ".join(postfix)
 
# infix = "( ( 1 + 2 ) * 3 ) ^ 2"
# infix = "( ( 1 + 2 ) * 3 ) ^ 2"
# infix = "( ( ( 3 * 6 ) * ( 2 - 4 ) ) + 7 )"
# infix = "1 + 2 * 3 + 2"
# infix = "( 1 + 2 ) * 3 - ( 41 - 5 ) * ( 6 + 7 )"
# infix = "-1 + 2 * 3 - 4.1 - 5 * 6 + 7"
# print(build_postfix(infix))



def solve_postfix(postfix: Optional[str]) -> Optional[float]:
    post_list = postfix.split(" ")
    stack = []
    evaluated = 0

    while len(post_list) > 0:

        if not is_operator(post_list[0]):
            stack.append(post_list.pop(0))

        else: # if postlist[0] is an operator
            operator = post_list[0]
            if operator == "^":
                evaluated = float(stack[-2]) ** float(stack[-1])
            
            elif operator == "*":
                evaluated = float(stack[-2]) * float(stack[-1])

            elif operator == "/":
                evaluated = float(stack[-2]) / float(stack[-1])

            elif operator == "+":
                evaluated = float(stack[-2]) + float(stack[-1])

            elif operator == "-":
                evaluated = float(stack[-2]) - float(stack[-1])

            post_list.pop(0)
            stack.pop()
            stack.pop()
            stack.append(str(evaluated))

    # total = "{:.3f}".format(float(stack[0]))
    total = "{:.3f}".format(float(stack[0]))

    return total

# postfix = "1 2 + 3 * 2 ^"
# postfix = "1 2 + 3 * 4 5 - 6 7 + * -"
# postfix = "8 4 3 ^ /"
# postfix = "-1 2 3 * + 4.1 - 5 6 * - 7 +"
# print(solve_postfix(postfix))



# do not add code below this line
if __name__ == "__main__":  # runs main with command |python3 postfixit.py|
    main()


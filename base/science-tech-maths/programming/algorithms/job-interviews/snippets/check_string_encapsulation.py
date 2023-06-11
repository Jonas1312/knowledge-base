"""
You must implement a function that determines whether a string has a valid encapsulation.
A valid encapsulation must respect the logic of opening and closing parenthesis AND brackets,
for instance the string "[(Hello)-(World)]" has a valid encapsulation,
whereas the string "[(Hello)-(World])" has not.
"""

from collections import deque  # append, pop, appendleft, popleft


def check_encapsulation(string):
    stack = deque()
    for x in string:
        if x in ("(", "["):
            stack.append(")" if x == "(" else "]")
        elif x in (")", "]"):
            if stack.pop() != x:
                return False
    return True


def main():
    print(check_encapsulation("[(Hello)-(World)]"))  # true
    print(check_encapsulation("[(Hello)-(World])"))  # false
    print(check_encapsulation("[(h]]]]])-(w])"))  # false
    print(check_encapsulation("(Hello)[(Wintics)()]()"))  # true
    print(
        check_encapsulation("This string can have no brackets nor parenthesis!")
    )  # true


if __name__ == "__main__":
    main()

# Project 2: Evaluating Expressions Using Stacks

## Overview

For this project, you will implement a program to evaluate a postfix
(Reverse Polish or RPN) expression. To make the program more versatile,
you'll also provide code to convert prefix (Polish or PN) expressions to postfix
expressions.  In this way, your program will be able to evaluate prefix and postfix expressions. 
Many language translators (e.g. compiler)
do something similar to convert expressions into code that is easy to
execute on a computer.

For this assignment, you will use an implementation of the Abstract Data
Type Stack. Your programs should work with either implementation from
Lab 2 – the one based on a linked data structure or the one based on
Python’s List data type, but for consistency with grading, use the
stack_array.py implementation.  You must add, commit, and push a correct
implementation of this file.

Notes:

* Postfix expressions will only consist of numbers (integers, reals,
  positive or negative) and the five operators separated by spaces.  You
  may assume a capacity of 30 for the Stack will be sufficient for any
  expression that your programs will be required to handle.
* In addition to the operators + - * / shown in class, your programs
  should handle the exponentiation operator.  In this assignment, the
  exponential operator will be denoted by \**.  For example, 2\**3=8 and
  3\**2=9.  (https://en.wikipedia.org/wiki/Exponentiation)
* Every class and function must come with a brief purpose statement in
  its docstring. In separate comments you should explain the arguments
  and what is returned by the function or method.
* You must provide test cases that completely test all functions.
* Use descriptive names for data structures and helper functions.  You
  must name your files and functions (methods) as specified in the
  starter code provided to you.

## Modules and Functions
Your code will be contained in these files:
* stack_array.py
* stack_tests.py
* exp_eval.py
* exp_eval_testcases.py

 
## Algorithms

### Evaluating a Postfix (RPN) Expression

While RPN will look strange until you are familiar with it, here you can
begin to see some of its advantages for programmers. One such advantage
of RPN is that it removes the need for parentheses. RPN has no notion of
precedence, the operators are processed in the order they are
encountered. This makes evaluating RPN expressions fairly
straightforward and is a perfect application for a stack data structure,
just follow these steps:

* Process the expression from left-to-right
* When a value is encountered:
  * Push the value onto the stack
* When an operator is encountered:
  * Pop the required number of values from the stack
  * Perform the operation
  * Push the result back onto the stack
* Return the last value remaining on the stack

For example, given the expression 5 1 2 + 4 ** + 3 - :

```
Input Type      Stack   Notes
5     Value     5       Push 5 onto stack
1     Value     1 5     Push 1 onto stack
2     Value     2 1 5   Push 2 onto stack
+     Operator  3 5     Pop two operands (1, 2), perform operation (1+2=3), and push result onto stack
4     Value     4 3 5   Push 4 onto stack
**    Operator  81 5    Pop two operands (3, 4), perform operation (3**4=81), and push result onto stack
+     Operator  86      Pop two operands (5, 81), perform operation (5+81=86), and push result onto stack
3     Value     3 86    Push 3 onto stack
−     Operator  83      Pop two operands (86, 3), perform operator (86−3=83), and push result onto stack
      Result    83
```

### Converting Prefix Expressions (PN)  to Postfix

* Read the Prefix expression in reverse order (from right to left)
  * When an operand is encountered, push it onto the stack
  * When an operator is encountered:
    * Pop two operands/strings rom the stack: op1 = pop(), op2 = pop()
    * Create a string by concatenating the two operands/strings and the
      operator after them: string = op1 + op2 + operator (remember space
      separation between tokens).
    * Push the resultant string back to the stack
* Repeat the above steps until end of Prefix expression
* The one string remaining on the Stack is the resultant Postfix expression

For example, given the Prefix expression: * - 3 / 2 1 - / 4 5 6


```
Input  Action                        Stack          Notes
6      Push ‘6’ onto stack           ‘6’            Read from right to left
5      Push '5' onto stack           '5' '6'
4      Push ‘4’ onto stack           ‘4’ ‘5’ ‘6’
/      Pop ‘4’, ‘5’, combine         ‘4 5 /’ ‘6’    Keep tokens space separated
       with /, push onto stack
-      Pop ‘4 5 /’, ‘6’, combine     ‘4 5 / 6 -’
        with -, push onto stack
1      Push 1 onto stack             ‘1’ ‘4 5 / 6 -’
2      Push 2 onto stack             ‘2’ ‘1’ ‘4 5 / 6 -’
/      Pop ‘2’,’1’, combine          ‘2 1 /’ ‘4 5 / 6 -’
        with /, push onto stack
3      Push 3 onto stack             ‘3’ ‘2 1 /’ ‘4 5 / 6 -’
-      Pop ‘3’,‘2 1 /’, combine      ‘3 2 1 / -’ ‘4 5 / 6 -’
         with -, push onto stack
*      Pop ‘3 2 1 / -’,‘4 5 / 6 -’,  ‘3 2 1 / - 4 5 / 6 - *’
         combine with *, push onto
          stack
end    Pop entire stack to output                    Result: ‘3 2 1 / - 4 5 / 6 - *’
```

## Tests

* Write sufficient tests using unittest to ensure full functionality and
  correctness of your program.
* Make sure that your tests test each branch of your program and any
  edge conditions.  You do not need to test for correct input in the
  assignment, other than what is specified above.
* postfix_eval(input_str) should raise a ValueError if a divisor is 0.
  postfix_eval(input_str) should raise a PostfixFormatException if the
  input is not well-formed.  Specifically, it should raise this
  exception with the following messages in the following conditions:
  * “Invalid token” if one of the tokens is neither a valid operand nor
    a valid operator.
  * “Insufficient operands” if the expression does not contain
    sufficient operands.
  * “Too many operands” if the expression contains too many operands.
  * Note: to raise an exception with a message: raise
    PostfixFormatException(“Here is a message”)
* You may assume that when prefix_to_postfix(input_str) is called
  that input_str is a well formatted, correct prefix expression
  containing only numbers, the specified operators, and that the tokens
  are space separated.  You may use the Python functions split and join.
* postfix_eval(input_str) should raise a ValueError if a divisor is 0.

## Submission

Submit by pushing your code to github.  



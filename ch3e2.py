"""A function object is a value you can assign to a variable or pass as an argument. For
example, do_twice is a function that takes a function object as an argument and calls it twice:"""
def do_twice(f,val="shivam"):
    f(val)
    f(val)
def print_spam(s):
    print('spam'+s)
do_twice(print_spam)
"""Modify do_twice so that it takes two arguments, a function object and a value, and calls the
function twice, passing the value as an argument.
"""
""" Define a new function called do_four that takes a function object and a value and calls the
function four times, passing the value as a parameter. There should be only two statements in
the body of this function, not four.
"""
def do_four(s,val1="sham"):
    for _ in range(0,4):
        s(val1)
def print_spam1(s1):
    print('spam'+s1)
do_four(print_spam1)
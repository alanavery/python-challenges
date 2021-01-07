# You'll need to use a couple of built in functions to alphabetize a string.
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def string_sort(string):
    b = sorted(string)
    c = ''.join(b)
    print(c)


string_sort('string')

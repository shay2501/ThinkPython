#Exercise 1
print("Exercise 1")
def right_justify(s):
  padding = 70 - len(s) - 1
  print(' ' * padding, s)

right_justify("Shannon")

#Exercise 2
print("Exercise 2")
def do_twice_noarg(f):
    f()
    f()

def do_twice(f, v):
    f(v)
    f(v)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def print_spam():
    print('spam')

def do_four_noarg(f):
    do_twice_noarg(f)
    do_twice_noarg(f)

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

#do_twice(print_spam)
do_twice(print_twice, 'spam')
print("------------------")
do_four(print_twice, 'spam')

#Exercise 3
print("Exercise 3")
def print_row_col_start():
    print('+ - - - -', end='')

def print_row_end():
    print('+')

def print_col():
    print('/        /        ', end='')

def print_col_end():
    print('/')

#print 4 by 4
do_four_noarg(print_row_col_start)
print_row_end()
do_twice_noarg(print_col)
print_col_end()
do_four_noarg(print_row_col_start)
print_row_end()
do_twice_noarg(print_col)
print_col_end()
do_four_noarg(print_row_col_start)
print_row_end()

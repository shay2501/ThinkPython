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
def print_row_start():
    print('+ - - - -', end='')

def print_row_end():
    print('+')

def print_col():
    print('/        /        ', end='')

def print_col_end():
    print('/')

def print_2col_row_start():
    do_twice_noarg(print_row_start)
    print_row_end()

def print_2_col():
    print_col()
    print_col_end()

def print_2col_full():
    print_2col_row_start()
    do_four_noarg(print_2_col)

def print_4_col():
    do_twice_noarg(print_col)
    print_col_end()

def print_4col_full():
    do_four_noarg(print_row_start)
    print_row_end()
    do_four_noarg(print_4_col)

#print 2 by 2
do_twice_noarg(print_2col_full)
do_twice_noarg(print_row_start)
print_row_end()

#print 4 by 4
do_four_noarg(print_4col_full)
do_four_noarg(print_row_start)
print_row_end()

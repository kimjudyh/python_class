#!/usr/bin/env python3
# with a parameter (attempt)
def hooty_test(choice):
    new_choice = choice + 5
    return new_choice

# trying another parameter function
def hooty_square(my_num):
    squared = my_num*my_num
    return squared

def hooty_add(my_num):
    added = my_num + 365
    return added

# new function that prints mrow
def hooty_mrow():
    print("mrow")
    return

hooty_mrow()

def hooty_baa():
    print("baa")
    return "baa"

def hooty_moo():
    what_noise = input("moo, baa, or mrow?\n")
    if what_noise.lower() == "moo":
        print("mooooo")
    elif what_noise.lower() == "baa":
        noise = hooty_baa()
    elif what_noise.lower() == "mrow":
        hooty_mrow()
    return

hooty_moo()

#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

def bubblesort(list):
  is_sorted = False;
  while not is_sorted:
    #Exit out if this never changes, e.g. no swaps.
    is_sorted = True;
    i = 1;
    while i < len(list):
      if (list[i-1] > list[i]):
        temp = list[i-1];
        list[i-1] = list[i];
        list[i] = temp;
        is_sorted = False;
      i += 1
    return list;

def main():
  print bubblesort([3, 1, 5, 6]);

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
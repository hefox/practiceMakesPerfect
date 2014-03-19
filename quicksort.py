#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

def quicksort(list):
  _quicksort(list, 0, len(list) -1)
  return list

def _quicksort(list, leftIndex, rightIndex):
  if rightIndex > leftIndex:
    pivotIndex = leftIndex + int ((rightIndex - leftIndex) / 2)
    newPivotIndex = partition(list, leftIndex, rightIndex, pivotIndex)
    _quicksort(list, leftIndex, newPivotIndex - 1)
    _quicksort(list, newPivotIndex + 1, rightIndex)

def partition(list, leftIndex, rightIndex, pivotIndex):
  value = list[pivotIndex]
  # Moves pivote to end to keep out of way
  swap(list, pivotIndex, rightIndex)
  i = leftIndex;
  storeIndex = leftIndex
  # Move all the smaller elements left
  while i < rightIndex:
    if list[i] <= value:
      # store index is replaces with small values always.
      swap(list, storeIndex, i)
      storeIndex += 1
    i += 1
  swap(list, storeIndex, rightIndex)
   return storeIndex

def swap(list, pos1, pos2):
  if (pos1 != pos2):
    temp = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = temp


def main():
  print quicksort([3, 1, 5, 6, 8, 2, 9, 3, 200, 50, 1000, 35, 1])

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
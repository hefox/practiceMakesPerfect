#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys


def mergeSort(list):
  if len(list) == 1:
    return list
  middle = int(len(list) / 2)
  return merge(mergeSort(list[0:middle]), mergeSort(list[middle:len(list)]))

def merge(list1, list2):
  list1Index = 0
  list2Index = 0;
  returnList = []
  while list1Index != len(list1) or list2Index != len(list2):
    # Have not reached the end of line for either lists.
    if list1Index != len(list1) and list2Index != len(list2):
      if list1[list1Index] < list2[list2Index]:
        returnList.append(list1[list1Index])
        list1Index += 1
      else:
        returnList.append(list2[list2Index])
        list2Index += 1
    # One of them has reached their end, find it and take that one.
    else:
      if list1Index != len(list1):
        returnList.append(list1[list1Index])
        list1Index += 1
      else:
        returnList.append(list2[list2Index])
        list2Index += 1
  return returnList

def main():
  print mergeSort([3, 1, 5, 6, 8, 2, 9, 3, 200, 50, 1000, 35, 1])

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
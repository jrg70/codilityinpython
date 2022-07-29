""" A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000]."""

def solution(A):
    """
    Check whether A is a permutation
    :array A: Is the list of numbers to check for permutation
    :return 0 or 1: 1 if permutation, 0 if not
    """
  if len(A) == 0:
    return 0
  
  dict = {}
  for i in A:
    if i in dict:
      return 0
    dict[i] = True
  
  if len(A) != len(dict):
    return 0

  for i in range(1,len(A)+1):
    if i not in A:
      return 0
  return 1

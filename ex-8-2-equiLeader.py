"""A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000]."""

def solution(A):
  if len(A) == 1:   # if only one element, it is the dominator itself
    return(0)
  
  Copy = A.copy()
  Copy.sort()
  occ = 1
  n = 0
  leader = 0
  
  for i in range(0,len(Copy)-1):
    if Copy[i] != Copy[i+1]: #in the sorted list different numbers are listed
      occ = 1
    else: # the same number is twice add 1 to the occurrence
      occ+=1
    if occ > int(len(Copy)/2):
      leader = Copy[i]
      break
  for i in range(0,len(A)):
    if A[i] == leader:
        n+=1
  Eleader = 0
  occ = 0
  for i in range(0,len(A)):
    if A[i] == leader:
        occ += 1
    if (i+1<2*occ and len(A)-i-1 < 2*(n-occ)):
        Eleader +=1
  return Eleader
  return -1
  

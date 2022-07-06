"""A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647]."""


def slowlution(N): #only gives 64% since performance suffers from going thorugh every number 
  c = 0
  for i in range(1,N+1):
    if N%i == 0:
      c+=1
  return c

def fastlution(N): # faster 100%, making use of the fact that the total number must be twice the amount that in the square root (or -1 that number). 10-2 makes it much clearer and it is more intuitive why we use the square root
  c = 0
  for i in range(1,int(N**0.5)+1):
    if N%i == 0:
      c+=1
    if N==int(N**0.5)*int(N**0.5):
      return c*2-1
    else:
      return c*2


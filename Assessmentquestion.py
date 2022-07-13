# Three questions in total

# 1. Compute the specifity/sensitivity based on two binary strings:

def solution(A,B,q):
  if q == True: # spec
    TN = 0
    FP = 0
    for i in range(0, len(A)):
      if A[i] == 0 and B[i] == 0:
        TN += 1
      elif A[i] == 0 and B[i] == 1:
        FP += 1
    return TN/(TN+FP)
  else: # sens
    TP = 0
    FN = 0
    for i in range(0, len(A)):
      if A[i] == 1 and B[i] == 1:
        TP += 1
      elif A[i] == 1 and B[i] == 0:
        FN += 1
    return TP/(TP+FN)

  # 2. Compute the letter that appears twice in a word unde rthe assumption all are disticnt expect one, i.e. "codility" computes "i" or "aba" computes "a".
  
  def solution(S):
  dict = {}
  for i in range(0,len(S)):
    if S[i] not in dict:
      dict[S[i]] = 0
    else:
      dict[S[i]] += 1
  return dict

solution("aba")

# 3. You are given a number e.g. 14, the sum of its digits is 1+4=5, this times two is 10, this back into digits again would be 19. For any given input number  N
# compute that described way. Another example was 999 -> 9+9+9= 27 -> 27*2 = 54 -> 999999. 
# Since we multiply with 2 the last digits must be 0,2,4,6 or 8.
# 2 -> 11
# 4 -> 13
# 6 -> 15
# 8 -> 17
# 10 -> 19
# 12 -> 39
# 14 -> 59
# 16 -> 79
# 18 -> 99
# 20 -> 299

def Q(num): #calculates the sum of the digits
    result = 0
    while num:
        result += num % 10
        num = int(num / 10)
    return result

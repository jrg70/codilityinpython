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

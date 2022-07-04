"""A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")"."""

string = "()"

# idea for ever opening bracket we have the clsoing one coming - fast

def fastlution(S):
    s = []
    for k in S:
        if k in "([{":
            s.append(k)
        else:
            if len(s) == 0:
                return 0
            if k == ')' and s[-1] == '(':
                s.pop()
            if k == ']' and s[-1] == '[':
                s.pop()
            if k == '}' and s[-1] == '{':
                s.pop()
    if len(s) == 0:
        return 1
    else:
        return 0
string = "({[]()[]})"
solution(string)



# split the string mirror the brackets with ascii transformation - slow but fun


def slowlution(S):
  if len(S) == 0 or len(S)%2 == 1:
    return 0
  else:
    half = int(len(S)/2)
    str1, str2 = S[:half], S[half:][::-1]
    dict = {"(":1, "{":2, "[":2, "]":-2, "}":-2,")":-1}
    str = ""
    for i in range(0,half):
      if str2[i] == list(dict.keys())[0]:
        str = str + chr(ord(str2[i])+dict[list(dict.keys())[0]])
      elif str2[i] == list(dict.keys())[1]:
        str = str + chr(ord(str2[i])+dict[list(dict.keys())[1]])
      elif str2[i] == list(dict.keys())[2]:
        str = str + chr(ord(str2[i])+dict[list(dict.keys())[2]])
      elif str2[i] == list(dict.keys())[3]:
        str = str + chr(ord(str2[i])+dict[list(dict.keys())[3]])
      elif str2[i] == list(dict.keys())[4]:
        str = str + chr(ord(str2[i])+dict[list(dict.keys())[4]])
      else:
        str = str + chr(ord(str2[i])+dict[list(dict.keys())[5]])
    if str == str1:
      return 1
    return 0



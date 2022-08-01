def  solution(A):
        # Last day +30 because of the comparison 
        M = A[-1] + 30
        price = [0] * (M + 1)
        day = [0] * (M)
        a = 0

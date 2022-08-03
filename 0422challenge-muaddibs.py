def  solution(A):
        # Last day +30 because of the comparison 
        M = A[-1] + 30
        price = [0] * (M + 1)
        day = [0] * (M)
        a = 0
        while (a < len(A)) :
            day[A[a]] = 1
            a += 1   
        i = M - 1
        while (i > -1):
            if (day[i] == 0) :
                price[i] = price[i + 1]
            else:
                price[i] = min(2 + price[i + 1],min(7 + price[i + 7],25 + price[i + 30]))
            i -= 1
        print(day, price)    
        return price[1]

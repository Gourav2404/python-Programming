# cook your dish here
dp = {0:0,1:1,2:2}

def gold_coins(n):
    if n in dp:
        return dp[n]
    else:
        dp[n] = max(n,gold_coins(n//2)+gold_coins(n//3)+gold_coins(n//4))
        return dp[n]
        
while 1:
    try:
        n = int(input())
        print(gold_coins(n))
    except:
        break
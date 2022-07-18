# cook your dish here
t = int(input())
for i in range(t):
    x,y,z = map(int,input().split())
    total_time = x*y
    if(x<=3):
        count = x//3
        break_time = count*z
        ans = total_time
        print(ans)
    else:
        if(x%3 != 0):
            count = x//3
            break_time = count*z
            ans = total_time + break_time
            print(ans)
        else:
            count = x//3-1
            break_time = count*z
            ans = total_time + break_time
            print(ans)
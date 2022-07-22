# cook your dish here
p1,p2,p3,p4 = map(int, input().split())

weeks = [p1,p2,p3,p4]
counter = 0
for x in weeks:
    if x <= 100:
        if x >= 10:
            counter+=1

print (counter)
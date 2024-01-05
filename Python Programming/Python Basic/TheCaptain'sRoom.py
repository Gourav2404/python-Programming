
from collections import Counter

K = int(input()) 
room_numbers = Counter(map(int, input().split(' ')))
#print(room_numbers)

for k in room_numbers:
    #print(k , room_numbers[k]) 
    if room_numbers[k] == 1: 
        print(k)
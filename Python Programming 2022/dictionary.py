tel = {'jack': 4098, 'sape': 4139}
print(tel)
print(type(tel))

print(tel['jack'])
tel['irv'] = 4125
del tel ['sape']
print(tel)
print(sorted(tel))
print("as" in tel)
print('jack' in tel)

test = {x : x**2 for x in range(1,11)}
print(test)

#Looping Techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
print(knights.items())
for k , v in knights.items() :
    print(k,v)

for i , v in enumerate(['tic','tak','toe']):
    print(i,v)
# cook your dish here
no_test = int(input());
for i in range(no_test):
    scores = input()
    scores = scores.split()
    print(int(scores[0]) - int(scores[1]));

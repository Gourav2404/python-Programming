sample = int(input())
for number in range(sample):
    phone = input()
    first_digit = ['9', '8', '7']
    if len(phone) == 10:
        if phone[0] in first_digit and phone.isdigit():
            print('YES')
        else:
            print('NO')

    else:
        print('NO')

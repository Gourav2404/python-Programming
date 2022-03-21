def swap_case(s):
    m = ""
    for i in s:

        if i.isupper():
            m += i.lower()
        else:
            m += i.upper()
    # print(m)

    return m


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

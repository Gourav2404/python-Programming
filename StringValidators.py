if __name__ == '__main__':
    s = input()
    for i in range(len(s)):
        if(s[i].isalnum()):
            print(True)
            break
    # return False ;
        # print(False)

    for i in range(len(s)):
        if(s[i].isalpha()):
            print(True)
            break
        # return False
        # print(False)

    for i in range(len(s)):
        if(s[i].isdigit()):
            print(True)
            break
        # return False;

    for i in range(len(s)):
        if(s[i].islower()):
            print(True)
            break
        # return False;

    for i in range(len(s)):
        if(s[i].isupper()):
            print(True)
            break
        # return False;
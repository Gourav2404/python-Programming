def minion_game(string):
    # your code goes here
    s = len(string)
    stuart, kevin = 0, 0

    for i in range(s):
        if string[i] in 'AEIOU':
            kevin += s-i
        else:
            stuart += s-i

    if kevin == stuart:
        print("Draw")

    elif kevin > stuart:
        print(f"Kevin {kevin}")

    else:
        print(f"Stuart {stuart}")


if __name__ == '__main__':
    s = input()
    minion_game(s)

def merge_the_tools(string, k):
    # your code goes here

    for i in range(0, len(string), k):
        indexes = string[i: i + k]
        string_output = []

        for j in indexes:
            if j not in string_output:
                string_output.append(j)

        print(''.join(string_output))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

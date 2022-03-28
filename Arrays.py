import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    numarr = numpy.array(arr[::-1], float)
    return numarr


arr = input().strip().split(' ')
result = arrays(arr)
print(result)

def addZeroToEnd(ar, s):
    count = 0

    for i in range(s):
        if ar[i] != 0:
            ar[count] = ar[i]
            count += 1
    while count < s:
        ar[count] = 0
        count += 1
ar = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
s = len(ar)
addZeroToEnd(ar, s)
print("Array after pushing all zeros to end of array:")
print(ar)

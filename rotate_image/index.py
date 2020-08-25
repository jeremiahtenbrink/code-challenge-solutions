def rotateImage(a):
    print(a)
    length = len(a)
    for i1 in range(length):
        for i2 in range(length):
            item = a[i1].pop()
            a[length -1 - i2] = [item] + a[length -1 -i2]
        print(a)

    return a



rotateImage([[1,2,3],  [4,5,6],  [7,8,9]])
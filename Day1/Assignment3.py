def fibonacci():
    a, b = 2, 3
    print(a, b, end=" ")
    while True:
        c = a + b
        if c > 100:
            break
        print(c, end=" ")
        a, b = b, c

fibonacci()
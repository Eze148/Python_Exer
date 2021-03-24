def search(x):
    a = 100
    z = 0
    y = 0
    while(x != y):
        y = (a + z) // 2
        if (x == y):
            break
        print('Is this number larger than', +y, ' (y/n)?: ')
        w = input()
        if(w == 'y'):
            z = y
        elif(w == 'n'):
            a = y
    print("Input number is: ", +y)
    
search(33)

if __name__ == '__main__':
    n = int(input())
    
    i = 0
    while (i < n):
        print(i * i)
        i += 1
    #or you could do
    for i in range(0, n):
        print(i * i)
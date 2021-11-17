def fibonacci(n):
    count = 0
    n1 = 0
    n2 = 1
    while count < n:
        print(n1)
        nactz = n1 + n2
        n1 = n2
        n2 = nactz
        count += 1

num = int(input('How many elements of the Fibonacci sequence do you want: '))
fibonacci(num)
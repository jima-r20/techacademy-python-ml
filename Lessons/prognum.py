def fibo(num):
    if num <= 2:
        return 1
    else:
        return fibo(num - 2) + fibo(num - 1)
        
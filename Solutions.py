def armstrong(num):
    sum=0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")

# Fibonacci Series
def fibonacci(nterms):
    n1=0; n2=1
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print(f"Fibonacci sequence upto {nterms} : {n1}")
    else:
        print("Fibonacci sequence:")
        count = 0
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1, n2 = n2, nth
            count += 1

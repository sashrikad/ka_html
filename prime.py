n = 6
counter = 2
prime = True

while counter < n:
    m = n % counter
    print("counter", counter)
    if m ==  0 :
        print("Divisible by ", counter)
        print("breaking the loop")
        prime=False
        break
    else:
        print("Not divisible by ",counter)
        print("Increasing the counter")
        counter = counter +1

if prime == True:
    print("It's a prime number")
else:
    print("It's NOT a prime number")
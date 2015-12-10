# Bancho Petrov
# Started on 13.09.2013
# Reached Level 1 (25 solved problems) on 10.11.2013
# Reached Level 2 (50 solved problems) on 23.04.2014

import math
import itertools
import random
import time

def prime_generator(y): # apparently this algorithm can only go up to 10**7
    p = dict()
    for i in range(2, y):
        p[i] = True
    for i in p:
        factors = range(i, y, i)
        for f in factors[1:]:
            p[f] = False
    return p

def is_prime(n):
    n = abs(int(n))
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def Multiples_of_3_and_5(): #1
    the_sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            the_sum+=i
    return the_sum

def Even_Fibonacci_numbers(): #2
    the_sum = 0
    fib = [1, 2]
    for i in range(38):
        x = fib[i] + fib[i+1]
        if x >= 4000000:
            break
        else:
            fib.append(x)
    for i in fib:
        if i % 2 == 0:
            the_sum+=i
    return the_sum

def Prime_factors(): #3
    n = 0
    p = 10000
    list_of_primes_below_p = [2]
    while n<=p-1:
        n=n+1
        for b in range(2,n):
                if n%b==0:
                    break
                if b==(n-1):
                    list_of_primes_below_p.append(n)
    x = 600851475143
    prime_factors_of_x = []
    for i in list_of_primes_below_p:
        if x % i == 0:
            prime_factors_of_x.append(i)
    return prime_factors_of_x

def Largest_palindrome_product(): #4
    x = 900
    palindrome_list = []
    while x < 1000:
        for i in range(900, 1000):
            prod = i * x
            y = str(prod)
            z = []
            for digit in y:
                z.append(eval(digit))
            if z[0] == z[-1] and z[1] == z[-2] and z[2] == z[-3]:
                print str(i)+" * "+str(x)+" is a palindrome"
                palindrome_list.append(prod)
        x+=1
    return str(max(palindrome_list))

def Smallest_multiple(): #5
    n = 2520 + 1
    while True:
        for i in range(1, 21):
            if n % i == 0 and i == 20:
                return n
            elif n % i == 0:
                pass
            elif n % i != 0:
                break
        n+=1

def Sum_square_difference(): #6
    sum_of_squares = 0
    square_of_sums = 0
    n = 1
    while n <= 100:
        sum_of_squares += n**2
        n += 1
    n = 1
    while n <= 100:
        square_of_sums += n
        n += 1
    square_of_sums = square_of_sums**2
    return abs(sum_of_squares - square_of_sums)

def zehntausenderste_prime(): #7
    n = 0
    x = 1
    while x < 10001:
        n += 1
        for i in range(2,n):
                if n%i==0:
                    break
                if i==(n-1):
                    x += 1
                    prime = n
    return prime

def Largest_product_in_series(): #8
    x = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    y = []
    products = []
    for digit in x:
        y.append(eval(digit))
    for i in range(1000-4):
        z = y[i] * y[i+1] * y[i+2] * y[i+3] * y[i+4]
        products.append(z)
    return max(products)

def Special_Pythagorean_triplet(): #9
    m = 0
    while m < 50:
        for i in range(50):
            # The following is Euclid's formula.
            a = m**2 - i**2
            b = 2*m*i
            c = m**2 + i**2
            if a > 0 and b > 0 and c > 0 and a + b + c == 1000:
                triplet = (a, b, c)
                print triplet
                return a*b*c
        m+=1

def Summation_of_primes(x): #10
    # Unfortunately this function ran for about four and a half hours and
    # still couldn't give me the answer for x = 2,000,000.
    n = 1
    answer = 2
    while n < x:
        # n+=1
        n+=2 # This way I skip all even numbers. Hopefully it becomes at least
        # a bit quicker..
        for i in range(2, n):
            if n % i == 0:
                break
            if i == n-1:
                answer+=n
    return answer

def Summation_of_primes_sieve(x): #10
    # This is using the sieve of Eratosthenes.
    nums = range(2, x+1)
    for i in nums:
        factors = range(i, x+1, i)
        for f in factors[1:]:
            if f in nums:
                nums.remove(f)
    return sum(nums)
    # Still not as quick as I was expecting. The next one, however, is.

def Summation_primes_using_sieve_and_dict(limit): #10
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn):
        primes[i] = True
    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return sum([i for i in primes if primes[i]==True])

def Largest_product(): #11
    x = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
    x = x.split()
    products = []
    for m in range(len(x)):
        if x[m].startswith("0"):
            x[m] = x[m][-1]
    for i in range(len(x)-63):
        if i % 19 == 0 or i+1 % 19 == 0 or i+2 % 19 == 0:
            pass
        else:
            products.append(eval(x[i]) * eval(x[i+21]) * eval(x[i+42]) * eval(x[i+63]))
    for i in range(len(x)-57):
        if i % 19 == 0 or i-1 % 19 == 0 or i-2 % 19 == 0:
            pass
        else:
            products.append(eval(x[i]) * eval(x[i+19]) * eval(x[i+38]) * eval(x[i+57]))
    return max(products)

def Highly_divisible_triangular_number(x): #12
    t_num = 0
    cycles = 0
    while True:
        num_of_divisors = 0
        cycles+=1
        t_num+=cycles
        for i in range(1, int(t_num**0.5)+1):
            if t_num % i == 0:
                num_of_divisors+=2
        if num_of_divisors > x:
            return t_num

def Longest_Collatz_sequence(n): #14
    rec_len = 0
    init_x = 0
    for x in range(2, n):
        new_len = 1
        y = x
        while x != 1:
            if x % 2 == 0:
                x = x / 2
                new_len+=1
            elif x % 2 != 0:
                x = 3 * x + 1
                new_len+=1
        if new_len > rec_len:
            rec_len = new_len
            init_x = y
    return init_x, rec_len

def Number_letter_counts(): #17
    letters = 106
    for i in range(20, 1000):
        if len(str(i)) == 2 and i >= 20:
            if str(i)[0] == "5" or str(i)[0] == "6" or str(i)[1] == "4":
                letters+=5
            if str(i)[0] == "2" or str(i)[0] == "3" or str(i)[0] == "8" or str(i)[0] == "9":
                letters+=6
            if str(i)[0] == "7":
                letters+=7
                
            if str(i)[1] == "1" or str(i)[1] == "2" or str(i)[1] == "6":
                letters+=3
            if str(i)[1] == "4" or str(i)[1] == "5" or str(i)[1] == "9":
                letters+=4
            if str(i)[1] == "3" or str(i)[1] == "7" or str(i)[1] == "8":
                letters+=5
        # by now (below 100), letters = 835
        
        if len(str(i)) == 3:
            if str(i)[0] == "1" or str(i)[0] == "2" or str(i)[0] == "6":
                letters+=10
            if str(i)[0] == "4" or str(i)[0] == "5" or str(i)[0] == "9":
                letters+=11
            if str(i)[0] == "3" or str(i)[0] == "7" or str(i)[0] == "8":
                letters+=12

            if str(i)[1] == "5" or str(i)[1] == "6" or str(i)[1] == "4":
                letters+=8
            if str(i)[1] == "2" or str(i)[1] == "3" or str(i)[1] == "8" or str(i)[1] == "9":
                letters+=9
            if str(i)[1] == "7":
                letters+=10

            if str(i)[1] == "1":
                if str(i)[2] == "0":
                    letters+=6
                if str(i)[2] == "1" or str(i)[2] == "2":
                    letters+=9
                if str(i)[2] == "5" or str(i)[2] == "6":
                    letters+=10
                if str(i)[2] == "3" or str(i)[2] == "4" or str(i)[2] == "9" or str(i)[2] == "8":
                    letters+=11
                if str(i)[2] == "7":
                    letters+=12
            if str(i)[1] == "0":
                if str(i)[2] == "1" or str(i)[2] == "2" or str(i)[2] == "6":
                    letters+=6
                if str(i)[2] == "4" or str(i)[2] == "5" or str(i)[2] == "9":
                    letters+=7
                if str(i)[2] == "3" or str(i)[2] == "7" or str(i)[2] == "8":
                    letters+=8
            if eval(str(i)[1]) > 1:
                if str(i)[2] == "1" or str(i)[2] == "2" or str(i)[2] == "6":
                    letters+=3
                if str(i)[2] == "4" or str(i)[2] == "5" or str(i)[2] == "9":
                    letters+=4
                if str(i)[2] == "3" or str(i)[2] == "7" or str(i)[2] == "8":
                    letters+=5

    letters+=len("onethousand")
    return letters

def Counting_Saturdays(): #19
    date = 1
    month = 1
    year = 1901
    day = 2
    Saturdays = 0
    while year <= 2000:
        if date == 1 and day == 6:
            Saturdays+=1
            
        if day == 7:
            day = 1
        else:
            day+=1
            
        if date == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
            date = 1
            month+=1
        elif date == 30 and (month == 4 or month == 6 or month == 9 or month == 11):
            date = 1
            month+=1
        elif date == 28 and month == 2 and year % 4 != 0:
            date = 1
            month+=1
        elif date == 29 and month == 2 and year % 4 == 0:
            date = 1
            month+=1
        elif date == 31 and month == 12:
            date = 1
            month = 1
            year+=1
        else:
            date+=1
    return Saturdays

def Factorial_digit_sum(): #20
    x = 1
    for i in range(2, 101):
        x = x * i
    y = str(x)
    answer = 0
    for digit in y:
        answer+=eval(digit)
    return answer

def Amicable_numbers(): #21
    a_nums = []
    x = 1
    while x < 10000:
        sum_1 = 1
        sum_2 = 1
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                sum_1+=i
                if x/i != i:
                    sum_1+=x/i
        if sum_1 != 1 and sum_1 > x:
            for k in range(2, int(sum_1**0.5) + 1):
                if sum_1 % k == 0:
                    sum_2+=k
                    if sum_1/k != k:
                        sum_2+=sum_1/k
        if x == sum_2 and x != sum_1:
            a_nums.extend([x, sum_1])
        x+=1
    print a_nums
    return sum(a_nums)

def Names_scores(): #22
    a = open("names.txt", "r")
    a = a.read()
    a = a.split(",")
    for i in range(len(a)):
        a[i] = eval(a[i])
    x = 1
    while x > 0:
        x = 0
        temp = ""
        for i in range(1, len(a)):
            if ord(a[i-1][0]) > ord(a[i][0]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                x+=1
            if ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) > ord(a[i][1]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                x+=1
            if len(a[i-1]) > 2 and len(a[i]) > 2:
                if ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) > ord(a[i][2]):
                    temp = a[i-1]
                    a[i-1] = a[i]
                    a[i] = temp
                    x+=1
            if len(a[i-1]) > 2 and len(a[i]) == 2 and ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                x+=1
            if len(a[i-1]) > 3 and len(a[i]) > 3:
                if ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) > ord(a[i][3]):
                    temp = a[i-1]
                    a[i-1] = a[i]
                    a[i] = temp
                    x+=1
            if len(a[i-1]) > 3 and len(a[i]) == 3 and ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                x+=1
            if len(a[i-1]) > 4 and len(a[i]) > 4:
                if ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) > ord(a[i][4]):
                    temp = a[i-1]
                    a[i-1] = a[i]
                    a[i] = temp
                    x+=1
            if len(a[i-1]) > 4 and len(a[i]) == 4 and ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                x+=1
            if len(a[i-1]) > 5 and len(a[i]) > 5:
                if ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]) and ord(a[i-1][5]) > ord(a[i][5]):
                    temp = a[i-1]
                    a[i-1] = a[i]
                    a[i] = temp
                    x+=1
            if len(a[i-1]) > 5 and len(a[i]) == 5 and ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                x+=1
            if len(a[i-1]) > 6 and len(a[i]) > 6:
                if ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]) and ord(a[i-1][5]) == ord(a[i][5]) and ord(a[i-1][6]) > ord(a[i][6]):
                    temp = a[i-1]
                    a[i-1] = a[i]
                    a[i] = temp
                    x+=1
            if len(a[i-1]) > 6 and len(a[i]) == 6 and ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]) and ord(a[i-1][5]) == ord(a[i][5]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                x+=1
            if len(a[i-1]) > 7 and len(a[i]) > 7:
                if ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]) and ord(a[i-1][5]) == ord(a[i][5]) and ord(a[i-1][6]) == ord(a[i][6]) and ord(a[i-1][7]) > ord(a[i][7]):
                    temp = a[i-1]
                    a[i-1] = a[i]
                    a[i] = temp
                    x+=1
            if len(a[i-1]) > 7 and len(a[i]) == 7 and ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]) and ord(a[i-1][5]) == ord(a[i][5]) and ord(a[i-1][6]) == ord(a[i][6]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                x+=1
            if len(a[i-1]) > 8 and len(a[i]) > 8:
                if ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]) and ord(a[i-1][5]) == ord(a[i][5]) and ord(a[i-1][6]) == ord(a[i][6]) and ord(a[i-1][7]) == ord(a[i][7]) and ord(a[i-1][8]) > ord(a[i][8]):
                    temp = a[i-1]
                    a[i-1] = a[i]
                    a[i] = temp
                    x+=1
            if len(a[i-1]) > 8 and len(a[i]) == 8 and ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]) and ord(a[i-1][5]) == ord(a[i][5]) and ord(a[i-1][6]) == ord(a[i][6]) and ord(a[i-1][7]) == ord(a[i][7]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                x+=1
            if len(a[i-1]) > 9 and len(a[i]) > 9:
                if ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]) and ord(a[i-1][5]) == ord(a[i][5]) and ord(a[i-1][6]) == ord(a[i][6]) and ord(a[i-1][7]) == ord(a[i][7]) and ord(a[i-1][8]) == ord(a[i][8]) and ord(a[i-1][9]) > ord(a[i][9]):
                    temp = a[i-1]
                    a[i-1] = a[i]
                    a[i] = temp
                    x+=1
            if len(a[i-1]) > 9 and len(a[i]) == 9 and ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]) and ord(a[i-1][5]) == ord(a[i][5]) and ord(a[i-1][6]) == ord(a[i][6]) and ord(a[i-1][7]) == ord(a[i][7]) and ord(a[i-1][8]) == ord(a[i][8]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                x+=1
            if len(a[i-1]) > 10 and len(a[i]) > 10:
                if ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]) and ord(a[i-1][5]) == ord(a[i][5]) and ord(a[i-1][6]) == ord(a[i][6]) and ord(a[i-1][7]) == ord(a[i][7]) and ord(a[i-1][8]) == ord(a[i][8]) and ord(a[i-1][9]) == ord(a[i][9]) and ord(a[i-1][10]) > ord(a[i][10]):
                    temp = a[i-1]
                    a[i-1] = a[i]
                    a[i] = temp
                    x+=1
            if len(a[i-1]) > 10 and len(a[i]) == 10 and ord(a[i-1][0]) == ord(a[i][0]) and ord(a[i-1][1]) == ord(a[i][1]) and ord(a[i-1][2]) == ord(a[i][2]) and ord(a[i-1][3]) == ord(a[i][3]) and ord(a[i-1][4]) == ord(a[i][4]) and ord(a[i-1][5]) == ord(a[i][5]) and ord(a[i-1][6]) == ord(a[i][6]) and ord(a[i-1][7]) == ord(a[i][7]) and ord(a[i-1][8]) == ord(a[i][8]) and ord(a[i-1][9]) == ord(a[i][9]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                x+=1
    for i in range(len(a)):
        if len(a[i]) == 2:
            x+= (ord(a[i][0]) + ord(a[i][1]) - 2*64) * (i+1)
        if len(a[i]) == 3:
            x+= (ord(a[i][0]) + ord(a[i][1]) + ord(a[i][2]) - 3*64) * (i+1)
        if len(a[i]) == 4:
            x+= (ord(a[i][0]) + ord(a[i][1]) + ord(a[i][2]) + ord(a[i][3]) - 4*64) * (i+1)
        if len(a[i]) == 5:
            x+= (ord(a[i][0]) + ord(a[i][1]) + ord(a[i][2]) + ord(a[i][3]) + ord(a[i][4]) - 5*64) * (i+1)
        if len(a[i]) == 6:
            x+= (ord(a[i][0]) + ord(a[i][1]) + ord(a[i][2]) + ord(a[i][3]) + ord(a[i][4]) + ord(a[i][5]) - 6*64) * (i+1)
        if len(a[i]) == 7:
            x+= (ord(a[i][0]) + ord(a[i][1]) + ord(a[i][2]) + ord(a[i][3]) + ord(a[i][4]) + ord(a[i][5]) + ord(a[i][6]) - 7*64) * (i+1)
        if len(a[i]) == 8:
            x+= (ord(a[i][0]) + ord(a[i][1]) + ord(a[i][2]) + ord(a[i][3]) + ord(a[i][4]) + ord(a[i][5]) + ord(a[i][6]) + ord(a[i][7]) - 8*64) * (i+1)
        if len(a[i]) == 9:
            x+= (ord(a[i][0]) + ord(a[i][1]) + ord(a[i][2]) + ord(a[i][3]) + ord(a[i][4]) + ord(a[i][5]) + ord(a[i][6]) + ord(a[i][7]) + ord(a[i][8]) - 9*64) * (i+1)
        if len(a[i]) == 10:
            x+= (ord(a[i][0]) + ord(a[i][1]) + ord(a[i][2]) + ord(a[i][3]) + ord(a[i][4]) + ord(a[i][5]) + ord(a[i][6]) + ord(a[i][7]) + ord(a[i][8]) + ord(a[i][9]) - 10*64) * (i+1)
        if len(a[i]) == 11:
            x+= (ord(a[i][0]) + ord(a[i][1]) + ord(a[i][2]) + ord(a[i][3]) + ord(a[i][4]) + ord(a[i][5]) + ord(a[i][6]) + ord(a[i][7]) + ord(a[i][8]) + ord(a[i][9]) + ord(a[i][10]) - 11*64) * (i+1)
    return x

def Non_abundant_sums(): #23
    book = {x:True for x in range(1, 28124)}
    book[24] = False
    abndt = [12]
    i = 12
    while i < 28124:
        i+=1
        for m in range(len(abndt)):
            if i % abndt[m] == 0:
                abndt.append(i)
                for j in abndt:
                    if j+i < 28124:
                        book[j+i] = False
                break
        if i not in abndt:
            divs = 1
            for k in range(2, int((i**0.5))+1):
                if i % k == 0:
                    divs+=k
                    if i/k != k:
                        divs+=i/k
            if divs > i:
                abndt.append(i)
                for l in abndt:
                    if l+i < 28124:
                        book[l+i] = False
    answer = 0
    for p in range(1, 28124):
        if book[p]:
            answer+=p
    return answer

def thousandth_digit_Fibonacci_number(): #25
    fib = [1, 1]
    i = 2
    while len(str(max(fib))) < 1000:
        fib.append(fib[i-2]+fib[i-1])
        i+=1
    return i

def Quadratic_primes(): #27
    primes = dict()
    for i in range(2, 1000000):
        primes[i] = True
    for i in primes:
        factors = range(i,1000000, i)
        for f in factors[1:]:
            primes[f] = False
    rec_n = 0
    for a in range(2000):
        if a > 999:
            a-=999
            a = a * (-1)
        for b in range(2000):
            if b > 999:
                b-=999
                b = b * (-1)
            prime_candidate = 2 # so I can enter the loop
            n = 0
            while primes[prime_candidate]:
                prime_candidate = n**2 + a*n + b
                n+=1
                if prime_candidate < 2:
                    break
            if n > rec_n:
                rec_n = n
                coefficients = a, b
    print rec_n
    return coefficients

def Distinct_powers(): #29
    terms = []
    x = 0
    for a in range(2, 101):
        for b in range(2, 101):
            x = a**b
            if x not in terms:
                terms.append(x)
    return len(terms)

def Number_spiral_diagonals(): #28
    answer = 0
    x = 1
    y = range(1, 1001+1, 2)
    for i in range(len(y)):
        y[i] = y[i]**2
    while x < 1002001:
        for i in range(len(y)-1):
            if x >= y[i] and x < y[i+1]:
                answer+=x
                x+=(y[i]**0.5)+1
                break
    answer+=1002001
    return int(answer)

def Digit_fifth_powers(): #30
    rare_ones = []
    for i in range(10, 10**6):
        x = []
        y = 0
        for digit in str(i):
            x.append(eval(digit))
        for m in range(len(x)):
            y+=x[m]**5
        if y == i:
            rare_ones.append(y)
    print rare_ones
    return sum(rare_ones)

def Pandigital_products(): #32
    x = 9876 +1
    answers = []
    while x > 0:
        x-=1
        divs = []
        for i in range(1, int(x**0.5)+1):
            if x % i == 0:
                divs.append(i)
                divs.append(x/i)
        for m in divs:
            for k in range(len(divs)-1):
                clue = True
                y = str(m) + str(divs[k+1]) + str(m*divs[k+1])
                if len(y) == 9:
                    for l in range(1, 10):
                        if not str(l) in y:
                            clue = False
                            break
                    if clue:
                        if not m*divs[k+1] in answers:
                            print m, divs[k+1]
                            answers.append(m*divs[k+1])
                        break
            if x in answers:
                break
    print answers
    return sum(answers)

def Digit_canceling_fractions(): #33
    for i in range(10, 100):
        for j in range(10, 100):
            x = 1
            while x <= i and x <= j:
                x+=1
                if float(i)/float(j) < 1 and i % x == 0 and j % x == 0 and not x == 10:
                    if str(i)[0] == str(j)[0] and str(i/x) == str(i)[1] and str(j/x) == str(j)[1]:
                        print str(i) + "/" + str(j) + "  x=" + str(x)
                    if str(i)[0] == str(j)[1] and str(i/x) == str(i)[1] and str(j/x) == str(j)[0]:
                        print str(i) + "/" + str(j) + "  x=" + str(x)
                    if str(i)[1] == str(j)[0] and str(i/x) == str(i)[0] and str(j/x) == str(j)[1]:
                        print str(i) + "/" + str(j) + "  x=" + str(x)
                    if str(i)[1] == str(j)[1] and str(i/x) == str(i)[0] and str(j/x) == str(j)[0]:
                        print str(i) + "/" + str(j) + "  x=" + str(x)
    print "49/98  x=12.25 doesn't show up using this code"
    print "fortunately, it was given in the task description"

def Digit_factorials(): #34
    answers = []
    for i in range(10, 10**5):
        y = []
        for digit in str(i):
            y.append(math.factorial(eval(digit)))
        if sum(y) == i:
            answers.append(i)
    print answers
    return sum(answers)

def Double_base_palindromes(): #36
    answers = []
    for i in range(1000000):
        x = len(str(i))
        y = ""
        while x > 0:
            x-=1
            y = y.__add__(str(i)[x])
        if not y.startswith("0"):
            y = eval(y)
        b = eval(bin(i)[2:])
        x = len(str(b))
        z = ""
        while x > 0:
            x-=1
            z = z.__add__(str(b)[x])
        if not z.startswith("0"):
            z = eval(z)
        if i == y and b == z and i not in answers:
            answers.append(i)
    print answers
    return sum(answers)

def Circular_primes(): #35
    primes = dict()
    for i in range(2, 1000000):
        primes[i] = True
    for i in primes:
        factors = range(i,1000000, i)
        for f in factors[1:]:
            primes[f] = False
    answers = []
    for i in range(2, len(primes)):
        if primes[i]:
            x = []
            for digit in range(len(str(i))):
                x.append(eval(str(i)[digit]))
            rotations = []
            for m in range(len(x)):
                x.insert(0, x.pop())
                rotations.append(list(x))
            t = True
            for m in range(len(rotations)):
                s = ""
                for k in range(len(rotations[m])):
                    s = s.__add__(str(rotations[m][k]))
                if not s.startswith("0"):
                    s = eval(s)
                    if not primes[s]:
                        t = False
            if t:
                answers.append(i)
    print answers
    return len(answers)

def Lexicographic_permutations(): #24
    all_permutations = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    return all_permutations[999999]

def Truncatable_primes(): #37
    primes = dict()
    for i in range(2, 1000000):
        primes[i] = True
    for i in primes:
        factors = range(i,1000000, i)
        for f in factors[1:]:
            primes[f] = False
    answers = []
    for i in range(10, 1000000):
        if not "0" in str(i) and primes[i]:
            validator = True
            x = []
            for digit in str(i):
                x.append(digit)
            for m in range(len(str(i))-1):
                x.pop(0)
                y = ""
                for k in range(len(x)):
                    y = y.__add__(x[k])
                y = eval(y)
                if y == 0 or y == 1:
                    validator = False
                elif not primes[y]:
                    validator = False
            x = []
            for digit in str(i):
                x.append(digit)
            for m in list(reversed(range(len(str(i))-1))): #the reversed thing is totally pointless here
                x.pop()
                y = ""
                for k in range(len(x)):
                    y = y.__add__(x[k])
                y = eval(y)
                if y == 0 or y == 1:
                    validator = False
                elif not primes[y]:
                    validator = False
            if validator:
                answers.append(i)
    print answers
    return sum(answers)

def Pandigital_multiples(): #38
    possible_answers = []
    for i in range(10000):
        con_prod = ""
        validator = True
        for m in range(1, 50):
            con_prod = con_prod.__add__(str(i*m))
            if len(con_prod) == 9:
                for k in "123456789":
                    if k not in con_prod:
                        validator = False
                        break
                if validator:
                    possible_answers.append(eval(con_prod))
            if len(con_prod) > 9:
                break
    print possible_answers
    return max(possible_answers)

def Integer_right_triangles(): #39
    rec_n = 0
    answer = 0
    combinations_of_answer = []
    for i in range(10, 1001):
        n = 0
        current_combinations = []
        for a in range(1, i-1):
            for b in range(1, i-a):
                c = i - (a + b)
                if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                    if sorted([a, b, c]) not in current_combinations:
                        n+=1
                        tupLe = sorted([a, b, c])
                        current_combinations.append(tupLe)
        if n > rec_n:
            print i, "   n =", n
            print current_combinations, "\n"
            rec_n = n
            answer = i
            combinations_of_answer = current_combinations
    return answer

def Champernownes_constant(): #40
    pretty_long_str = ""
    for i in range(1, 200000):
        pretty_long_str = pretty_long_str.__add__(str(i))
    answer = 1
    for i in range(1, 7):
        y = pretty_long_str[(10**i)-1]
        answer = answer * eval(y)
    return answer

def Pandigital_prime(): #41
    pandigits = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7]))
    pans = []
    for i in pandigits:
        s = ""
        for j in i:
            s = s.__add__(str(j))
        pans.append(eval(s))
    primes_d = prime_generator(32000)
    primes = []
    for i in range(2, len(primes_d)):
        if primes_d[i]:
            primes.append(i)
    answer = 0
    for i in pans:
        v = True
        for j in primes:
            if j > int(i**0.5):
                break
            if i % j == 0:
                v = False
                break
        if v:
            answer = i
    return answer

def Coded_triangle_numbers(): #42
    triangle_numbers = [0]
    for i in range(1, 26):
        triangle_numbers.append(triangle_numbers[i-1] + i)
    pos = dict()
    n = 1
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        pos[i] = n
        n+=1
    fob = open("words.txt", "r")
    words_str = fob.read()
    fob.close()
    words = words_str.split(",")
    for i in range(len(words)):
        words[i] = eval(words[i])
    answer = 0
    for i in words:
        word_value = 0
        for j in i:
            word_value += pos[j]
        if word_value in triangle_numbers:
            answer += 1
    return answer

def Sub_string_divisibility(): #43
    pandigits = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    pandigitals = []
    for i in range(len(pandigits)/10, len(pandigits)):
        s = ""
        for j in pandigits[i]:
            s = s.__add__(str(j))
        pandigitals.append(eval(s))
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    answers = []
    for i in pandigitals:
        s = str(i)
        v = True
        y = 0
        for x in range(1, 8):
            if s[x] == "0":
                if eval(s[x+1:x+3]) % primes[y] != 0:
                    v = False
                    break
            elif eval(s[x:x+3]) % primes[y] != 0:
                v = False
                break
            y+=1
        if v:
            answers.append(i)
    print answers
    return sum(answers)

def Pentagon_numbers(): #44
    pen_nums = []
    for n in range(3000):
        pen_nums.append((n*(3*n-1))/2)
    smallest_d = 10**10 #I just needed some big number here
    for x in range(1, len(pen_nums)):
        for y in range(x+1, len(pen_nums)):
            test1 = ((24*(pen_nums[x]+pen_nums[y])+1)**0.5+1)/6
            test2 = ((24*abs(pen_nums[x]-pen_nums[y])+1)**0.5+1)/6
            if str(test1)[-2:] == ".0" and str(test2)[-2:] == ".0":
                d = abs(pen_nums[x]-pen_nums[y])
                if d < smallest_d:
                    smallest_d = d
                    pair = (pen_nums[x], pen_nums[y])
    if smallest_d == 10**10:
        print "fail"
    else:
        print pair
        return smallest_d

def TriPenHex(): #45
    x = 100000
    tri = []
    for n in range(x):
        tri.append((n*(n+1))/2)
    pen = []
    for n in range(x):
        pen.append((n*(3*n-1))/2)
    hexa = []
    for n in range(x):
        hexa.append(n*(2*n-1))
    for i in tri:
        if i in pen and i in hexa:
            return i

def Goldbachs_other_conjecture(): #46
    primes = prime_generator(10000)
    for i in range(3, len(primes), 2):
        if primes[i] == False:
            v = False
            for j in range(2, i):
                if primes[j]:
                    x = (i-j)/2.
                    if str(x**0.5)[-2:] == ".0":
                        v = True
                        break
            if not v:
                return i

def Distinct_primes_factors(): #47
    primes_d = prime_generator(50000)
    primes = []
    for i in primes_d:
        if primes_d[i]:
            primes.append(i)
    for i in range(200000):
        if i not in primes:
            x = 0
            while x <= 3:
                prime_factors_of_i_plus_x = []
                for j in primes:
                    if (i+x) % j == 0:
                        prime_factors_of_i_plus_x.append(j)
                if len(prime_factors_of_i_plus_x) != 4:
                    break
                x += 1
            if x == 4:
                return i

def Self_powers(): #48
    series = 0
    for i in range(1, 1001):
        series += i**i
    return str(series)[-10:]

def Prime_permutations(): #49
    primes_d = prime_generator(10000)
    primes = []
    for i in primes_d:
        if primes_d[i]:
            primes.append(i)
    arth_progs = []
    for i in range(168, len(primes)):
        for j in range(i+2, len(primes)):
            if str((primes[i]+primes[j])/2.)[-2:] == ".0":
                if primes_d[(primes[i]+primes[j])/2.]:
                    x, y, z = primes[i], (primes[i]+primes[j])/2, primes[j]
                    condition = True
                    prog = [x, y, z] * 2
                    for n in range(3):
                        for digit in str(prog[n]):
                            if digit not in str(prog[n+1]) or digit not in str(prog[n+2]):
                                condition = False
                                break
                    if condition:
                            arth_progs.append((x, y, z))
    return arth_progs

def Consecutive_prime_sum(): #50
    primes_d = prime_generator(1000000)
    primes = []
    for i in primes_d:
        if primes_d[i]:
            primes.append(i)
    longest_seq = 0
    for h in range(len(primes)):
        x = primes[h]
        for i in range(h+1, len(primes)):
            x += primes[i]
            if x >= 1000000:
                break
            if primes_d[x]:
                seq = 0
                for j in range(h, i+1):
                    seq += 1
                if seq > longest_seq:
                    longest_seq = seq
                    longest_sum = x
                    starting_point = primes[h]
    print "The starting point of the sequence is " + str(starting_point)
    print "It's lenght is " + str(longest_seq)
    return longest_sum

def Prime_digit_replacements(): #51 <-- under construction
    dictPrimes = prime_generator(600)
    dictPrimes[0] = False
    dictPrimes[1] = False
    primes = []
    for i in dictPrimes:
        if dictPrimes[i]:
            primes.append(i)
    tested = {}
    for i in range(60000):
        tested[i] = False
    for i in range(len(primes)):
        if not tested[primes[i]]:
            for j in range(len(str(primes[i]))):
                a = []
                for k in str(primes[i]):
                    a.append(k)
                x = 0
                for k in "0123456789":
                    a[j] = k
                    b = ""
                    for l in a:
                        b = b.__add__(l)
                    if b != "09":
                        tested[eval(b)] = True
                        if dictPrimes[eval(b)]:
                            x += 1
                if x >= 7:
                    return primes[i]

def Permuted_multiples(): #52
    x = 10
    while True:
        x += 1
        if str(x)[0] != "1":
            x = x * 5 #in order to skip the numbers that don't start with a 1
        is_x_it = True #if it passes the tests in the next loop, then it's it
        for n in range(2, 6):
            for i in str(x):
                if not i in str(x*n) or len(str(x)) != len(str(x*n)):
                    is_x_it = False
                    break
            if not is_x_it:
                break
        if is_x_it:
            return x

def Combinatoric_selections(): #53
    tStart = time.time()
    count = 0
    def f(x):
        return math.factorial(x)
    for n in range(10, 101):
        for r in range(1, n):
            if f(n)/(f(r)*f(n-r)) > 10**6:
                count += 1
    print "Run Rime = " + str(time.time() - tStart)
    return count

def Poker_hands(): #54
    fob = open("poker.txt", "r")
    value = {"T" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14}
    for i in range(2, 11):
        value[str(i)] = i
    rank = {"High Card" : 0, "One Pair" : 1, "Two Pairs" : 2, "Three of a Kind" : 3, "Straight" : 4, "Flush" : 5, "Full House" : 6, "Four of a Kind" : 7, "Straight Flush" : 8, "Royal Flush" : 9}
    player_1_wins = 0
    def tie_breaker(x, y):
        for i in range(5):
            if x[4-i] > y[4-i]:
                return 0
            elif x[4-i] < y[4-i]:
                return 1
    for i in range(1000):
        line = fob.readline()
        for times_thru_loop in range(2):
            if times_thru_loop == 0:
                n = 0
            else:
                n = 15
            card_values = []
            for j in range(n, n+13, 3):
                card_values.append(value[line[j]])
            card_suits = []
            for j in range(n+1, n+14, 3):
                card_suits.append(line[j])
            cards_same_suit = True
            for j in range(4):
                if card_suits[j] != card_suits[j+1]:
                    cards_same_suit = False
                    break
            card_values.sort()
            hay_str8 = True
            for j in range(5):
                if card_values[j] - j != card_values[0]:
                    hay_str8 = False
                    break
            hay_4ofk = False
            for j in range(2, 15):
                if card_values.count(j) == 4:
                    hay_4ofk = True
                    rep_card = j
                    break
            hay_3ofk = False
            if not hay_4ofk:
                for j in range(2, 15):
                    if card_values.count(j) == 3:
                        hay_3ofk = True
                        rep_card = j
                        break
            hay_two_pairs = False
            if not hay_4ofk and not hay_3ofk:
                x = 0
                for j in range(2, 15):
                    if card_values.count(j) == 2:
                        x += 1
                if x == 2:
                    hay_two_pairs = True
                    rep_cards = []
                    for j in range(2, 15):
                        if card_values.count(j) == 2:
                            rep_cards.append(j)
            hay_one_pair = False
            if not hay_two_pairs:
                for j in range(2, 15):
                    if card_values.count(j) == 2:
                        hay_one_pair = True
                        if hay_3ofk:
                            smaller_rep_card = j
                        else:
                            rep_card = j
            
            if hay_str8 and cards_same_suit and card_values[4] == 14:
                hand = "Royal Flush"
            elif hay_str8 and cards_same_suit:
                hand = "Straight Flush"
            elif hay_4ofk:
                hand = "Four of a Kind"
            elif hay_3ofk and hay_one_pair:
                hand = "Full House"
            elif cards_same_suit:
                hand = "Flush"
            elif hay_str8:
                hand = "Straight"
            elif hay_3ofk:
                hand = "Three of a Kind"
            elif hay_two_pairs:
                hand = "Two Pairs"
            elif hay_one_pair:
                hand = "One Pair"
            else:
                hand = "High Card"
            
            if times_thru_loop == 0:
                cards_1 = card_values
                player_1 = rank[hand]
                if rank[hand] == 7 or rank[hand] == 3 or rank[hand] == 1:
                    rep_card_1 = rep_card
                if rank[hand] == 6:
                    rep_card_1 = rep_card
                    smaller_rep_card_1 = smaller_rep_card
                if rank[hand] == 2:
                    rep_cards_1 = rep_cards
            else:
                cards_2 = card_values
                player_2 = rank[hand]
                if rank[hand] == 7 or rank[hand] == 3 or rank[hand] == 1:
                    rep_card_2 = rep_card
                if rank[hand] == 6:
                    rep_card_2 = rep_card
                    smaller_rep_card_2 = smaller_rep_card
                if rank[hand] == 2:
                    rep_cards_2 = rep_cards

        if player_1 > player_2:
            player_1_wins += 1
        elif player_1 == player_2:
            p = rank[hand]
            if p == 8 or p == 5 or p == 4 or p == 0:
                if tie_breaker(cards_1, cards_2) == 0:
                    player_1_wins += 1
            if p == 7 or p == 3 or p == 1:
                if rep_card_1 > rep_card_2:
                    player_1_wins += 1
                elif rep_card_1 == rep_card_2:
                    if tie_breaker(cards_1, cards_2) == 0:
                        player_1_wins += 1
            if p == 6:
                if rep_card_1 > rep_card_2:
                    player_1_wins += 1
                elif rep_card_1 == rep_card_2:
                    if smaller_rep_card_1 > smaller_rep_card_2:
                        player_1_wins += 1
            if p == 2:
                if rep_cards_1[1] > rep_cards_2[1]:
                    player_1_wins += 1
                elif rep_cards_1[1] == rep_cards_2[1]:
                    if rep_cards_1[0] > rep_cards_2[0]:
                        player_1_wins += 1
                    elif rep_cards_1[0] == rep_cards_2[0]:
                        if tie_breaker(cards_1, cards_2) == 0:
                            player_1_wins += 1

    fob.close()
    return player_1_wins


def Lychrel_numbers(): #55
    def palindrome_test(a):
        x = 0
        y = -1
        is_palindrome = True
        while x < len(str(a))/2:
            if str(a)[x] != str(a)[y]:
                is_palindrome = False
                break
            x += 1
            y -= 1
        if is_palindrome:
            return True
        else:
            return False

    def reverse(x):
        if str(x)[::-1].startswith("0"):
            s = str(x)[::-1]
            while s[0] == "0":
                s = s[1:]
            return eval(s)
        return eval(str(x)[::-1])

    lychrel_numbers = []
    for i in range(1, 10000):
        x = i
        p = False
        for j in range(50):
            if palindrome_test(x + reverse(x)):
                p = True
                break
            x = x + reverse(x)
        if not p:
            lychrel_numbers.append(i)
    return len(lychrel_numbers)


def Powerful_digit_sum(): #56
    max_digit_sum = 0
    for i in range(1, 101):
        for j in range(1, 101):
            digit_sum = 0
            for digit in str(i**j):
                digit_sum += eval(digit)
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
    return max_digit_sum

def Square_root_convergents(): #57
    p = [1]
    q = [1]
    count = 0
    for i in range(1, 1000):
        p.append(p[i-1] + 2 * q[i-1])
        q.append(p[i-1] + q[i-1])
        if len(str(p[i])) > len(str(q[i])):
            count += 1
    return count

def Spiral_primes(): #58
    n = 3
    x = 1
    prime_diag_values = 0
    total_diag_values = 1
    while True:
        while x != n**2:
            x += n-1
            if is_prime(x):
                prime_diag_values += 1
        total_diag_values += 4
        if (prime_diag_values * 100.)/total_diag_values < 10:
            return n
        n += 2
        #print (prime_diag_values * 100.)/total_diag_values

def Prime_pair_sets(): #60 <-- currently not working
    primes_d = prime_generator(100000)
    primes = []
    for i in primes_d:
        if primes_d[i]:
            primes.append(i)
    for i in range(len(primes)):
        pair_set = [primes[i]]
        for j in range(i+1, len(primes)):
            test_passed = True
            x = str(primes[j])
            for k in range(len(pair_set)):
                y = str(pair_set[k])
                if not is_prime(eval(x+y)) or not is_prime(eval(y+x)):
                    test_passed = False
            if test_passed:
                pair_set.append(primes[j])
        if len(pair_set) == 5:
            print pair_set
            return sum(pair_set)

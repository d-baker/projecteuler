prev_result = 2

# loop through dividends and divisors
def loop(num_nums):
    global prev_result
    print 2

    for potential_prime in range(3, num_nums, 2):
            for divisor in range(2, potential_prime+1):
                    if potential_prime % divisor != 0:
                            if divisor==potential_prime -1 :
                                #print potential_prime
                                prev_result = sum(potential_prime, prev_result)
                    else:
                        break


# add together primes returned by loop()
# https://oeis.org/A007504 prime sums
def sum(cur_result, prev_result):
    cur_result = cur_result + prev_result
    print cur_result
    return cur_result






if __name__ == "__main__":
    loop(20000)
